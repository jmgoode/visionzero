import csv, shapely, sys, os
import geopandas as gpd
#import matplotlib.pyplot as plt

#read in input CSV file
# infile = open('data/clean/fatality_yearly_clean.csv')
infile = open(sys.argv[1])
reader = csv.reader(infile, delimiter=',')

outfile = open(sys.argv[3],'w')
writer = csv.writer(outfile)

# bike_priority_districts = gpd.read_file('data/initiatives/bike_priority_districts.json')
# # # bpd_geo = bike_priority_districts['geometry'] #geoseries of

# initiatives = os.listdir(sys.argv[2])
# for item in initiatives:
#     if item.endswith('json'):
#         print(item)

#read in data (using file path as sys.argv[1])
try:
    input_file = gpd.read_file(sys.argv[2])
except:
    print('Input file not found, please try again')
    sys.exit()

#add a column
header = next(reader, None) #read in header row
column_name = sys.argv[4] #extract desired column name specificed in command line sys.argv[2]
if column_name in header: #if the column name already exists
    pass
else:
    header.append(column_name) #add column label
    writer.writerow(header)
    #writer.writerow(('FID', 'Join_Count', 'TARGET_FID','Fatalities','PedFatalit','BikeFatali','MVOFatalit','YR','NODEID','Lon', 'Lat','STREET1','STREET2','InBikeZone'))

#make row dictionary (e.g. header_dict['BikeZone'] == 3)
enum_header = enumerate(header)
header_dict = {}
for num,index in enum_header:
    header_dict[index] = num

# # bike_priority_districts = gpd.read_file('data/initiatives/bike_priority_districts.json')
# # bpd_geo = bike_priority_districts['geometry'] #geoseries of
#
# point in polygon function
def check_point_in_polygon(row, point, zones):
    point_list = []
    for zone in zones:
        if zone.contains(point):
            point_list.append(point)
            break
        else:
            pass

    if len(point_list) > 0:
        row.append(1)
        writer.writerow(row)
        #writer.writerow((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],lon,lat,row[11],row[12],1))
    else:
        row.append(0)
        writer.writerow(row)
        #writer.writerow((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],lon,lat,row[11],row[12],0))

# get geometry type (polygon, linestring, point, etc.)
object_type = str(input_file.geometry[0].geom_type) #extract object type from file

#make a point
def extract_point(row):
    lon = float(row[header_dict['Lon']])
    lat = float(row[header_dict['Lat']])
    point = shapely.geometry.Point(lon, lat)
    return point

if object_type == 'Polygon':
    zones = input_file.geometry

for row in reader:
    point = extract_point(row) #creates shapely Point object
    check_point_in_polygon(row, point, zones) #checks to see if point in polygon and writes 1 to column if True, 0 if false

infile.close()
outfile.close()

#
# for row in reader:
#     lon = float(row[9])
#     lat = float(row[10])
#     point = shapely.geometry.Point(lon, lat)
#     check_point_in_polygon(row, point, zones)
#
#
# def checker(type, p):
#     if type == 'Polygon':
#         check_point_in_polygon(p)
#
