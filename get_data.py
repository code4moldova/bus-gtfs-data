import json
import csv
import datetime
import urllib.request

# Constants
AGENCY_ID = 'PUA'
JSON_DATA_URL = 'https://nimbus.wialon.com/api/locator/5f59baffc37144a3939d21bd8acc5e45/data'

def get_gtfs_csv_writer(file):
	return csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


def gen_agency_data(file_name):
	with open(file_name, mode='w') as agency_file:
		csv_writer = get_gtfs_csv_writer(agency_file)

		csv_writer.writerow(['agency_id','agency_name','agency_url','agency_timezone','agency_lang','agency_phone'])
		csv_writer.writerow([AGENCY_ID,'I.M. Parcul Urban de Autobuze', 'https://www.autourban.md/', 'Europe/Chisinau', 'ro', '022-556-030'])


def gen_stops_data(file_name, json_data, active_stops):
	with open(file_name, mode='w') as stops_file:
		csv_writer = get_gtfs_csv_writer(stops_file)

		csv_writer.writerow(['stop_id','stop_name','stop_lat','stop_lon'])

		for stop in json_data['stops']:
			if stop['tp'] == 1: #tp - transport type, tp==1 -> BUS
				if stop['id'] in active_stops:
					csv_writer.writerow([stop['id'],stop['n'],stop['p'][0]['y'],stop['p'][0]['x']])


def gen_routes_data(file_name, json_data):
	with open(file_name, mode='w') as routes_file:
		csv_writer = get_gtfs_csv_writer(routes_file)

		csv_writer.writerow(['route_id','agency_id','route_short_name','route_long_name','route_type'])

		for route in json_data['routes']:
			if route['tp'] == 1: #BUS route
				csv_writer.writerow([route['id'], AGENCY_ID, route['n'], route['d'], 3]) #route_type == 3 -> bus route


def gen_trips_data(file_name, json_data):
	with open(file_name, mode='w') as trips_file:
		csv_writer = get_gtfs_csv_writer(trips_file)

		csv_writer.writerow(['route_id','service_id','trip_id','trip_short_name'])

		for route in json_data['routes']:
			if route['tp'] == 1:
				for trip in route['tt']:
					#TODO(marcel): for now ignore trips for which the service_id is not specified, discuss later how to handle
					if trip['ptrn'] is None:
						continue

					csv_writer.writerow([route['id'], trip['ptrn'], trip['id'], route['n']])


def gen_stop_times_data(file_name, json_data, active_stops): #active_stops is a set that will store the set of all stops used in at least one trip
	with open(file_name, mode='w') as stop_times_file: 
		csv_writer = get_gtfs_csv_writer(stop_times_file)

		csv_writer.writerow(['trip_id','arrival_time','departure_time','stop_id','stop_sequence'])

		for route in json_data['routes']:
			if route['tp'] == 1:
				for trip in route['tt']:
					assert(len(route['s']) == len(trip['t'])) # should have the same number of stops as time stamps on the trip

					#TODO(marcel): for now ignore trips for which the service_id is not specified, discuss later how to handle
					if trip['ptrn'] is None:
						continue

					for i in range(len(trip['t'])):
						if trip['t'][i] is None: #TODO(marcel): clarify if missing time for a stop means that the BUS doesn't stop at this stop for this trip
							continue	

						seconds = int(trip['t'][i])

						hours = seconds // 3600
						seconds -= hours*3600

						minutes = seconds // 60
						seconds -= minutes*60
						

						bus_time = "{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds)
						csv_writer.writerow([trip['id'], bus_time, bus_time, route['s'][i], i])

						active_stops.add(route['s'][i])


def gen_calendar_data(file_name, json_data):
	with open(file_name, mode='w') as calendar_file: 
		csv_writer = get_gtfs_csv_writer(calendar_file)

		csv_writer.writerow(['service_id','monday','tuesday','wednesday','thursday','friday','saturday','sunday','start_date','end_date'])

		# hard code calendar data from https://nimbus.wialon.com/api/locator/5f59baffc37144a3939d21bd8acc5e45/data 
		# as there is no way to programatically map this data to the format in calendar.txt

		start_date = '20200101'
		end_date = '20211231'

		# Luni-Vineri
		csv_writer.writerow([2234, 1, 1, 1, 1, 1, 0, 0, start_date, end_date])

		#Sambata - Duminica
		csv_writer.writerow([2235, 0, 0, 0, 0, 0, 1, 1, start_date, end_date])

		#Sambata
		csv_writer.writerow([2358, 0, 0, 0, 0, 0, 1, 0, start_date, end_date])

		#Vara (iulie - august) lucru
		csv_writer.writerow([2696, 1, 1, 1, 1, 1, 0, 0, '20210701', '20210831'])

		#Luni-Sambata
		csv_writer.writerow([2533, 1, 1, 1, 1, 1, 1, 0, start_date, end_date])

		#Duminica
		csv_writer.writerow([2359, 0, 0, 0, 0, 0, 0, 1, start_date, end_date])

def gen_calendar_dates_data(file_name, json_data):
	with open(file_name, mode='w') as calendar_dates_file:
		csv_writer = get_gtfs_csv_writer(calendar_dates_file)

		csv_writer.writerow(['service_id','date','exception_type'])

		for service in json_data['patterns']:
			for additional_date in service['in']:
				csv_writer.writerow([service['id'],additional_date.replace('-',''),1])

			for exception_date in service['ex']:
				csv_writer.writerow([service['id'],exception_date.replace('-',''),2])


if __name__ == "__main__":
	json_data = json.loads(urllib.request.urlopen(JSON_DATA_URL).read().decode())

	gen_agency_data('agency.txt')
	
	active_stops = set()
	gen_stop_times_data('stop_times.txt', json_data, active_stops)

	gen_stops_data('stops.txt', json_data, active_stops)

	gen_routes_data('routes.txt', json_data)

	gen_trips_data('trips.txt', json_data)

	gen_calendar_data('calendar.txt', json_data)

	gen_calendar_dates_data('calendar_dates.txt', json_data)