import csv, shapely, sys, os
import geopandas as gpd
#import matplotlib.pyplot as plt

#make a point from CSV
def extract_point(row):
    lon = float(row[header_dict['Lon']])
    lat = float(row[header_dict['Lat']])
    point = shapely.geometry.Point(lon, lat)
    return point

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

def check_point_in_linestring(row,point,lines):
    point_list = []
    for line in lines:
        #if line.contains(point):
        if line.distance(point) < 1e-8:
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

def check_point_equals_point(row,point,points):
    point_list = []
    for p in points:
        #if line.contains(point):
        if p.almost_equals(point,decimal=2):
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

for file in os.listdir('../initiatives'):
    infile = open('in.csv')
    reader = csv.reader(infile, delimiter=',')
    path = '../initiatives/' + file
    input_file = gpd.read_file(path)
    outfile = open('out.csv','w')
    writer = csv.writer(outfile)

    #add a column
    header = next(reader, None) #read in header row
    column_name = file.split('.')[0] #extract desired column name specificed in command line sys.argv[2]

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

    # get geometry type (polygon, linestring, point, etc.)
    object_type = str(input_file.geometry[0].geom_type) #extract object type from file

    if object_type == 'Polygon':
        zones = input_file.geometry

        for row in reader:
            point = extract_point(row) #creates shapely Point object
            check_point_in_polygon(row, point, zones) #checks to see if point in polygon and writes 1 to column if True, 0 if false

    elif object_type == 'LineString':
        lines = input_file.geometry

        for row in reader:
            point = extract_point(row) #creates shapely Point object
            check_point_in_linestring(row, point, lines) #checks to see if point in polygon and writes 1 to column if True, 0 if false

    elif object_type == 'Point':
        points = input_file.geometry
        for row in reader:
            point = extract_point(row) #creates shapely Point object
            check_point_equals_point(row, point, points) #checks to see if point in polygon and writes 1 to column if True, 0 if false

    infile.close()
    outfile.close()

    os.remove('in.csv')
    os.rename('out.csv','in.csv')
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
# bike_priority_districts = gpd.read_file('data/initiatives/bike_priority_districts.json')
# # # bpd_geo = bike_priority_districts['geometry'] #geoseries of

# initiatives = os.listdir(sys.argv[2])
# for item in initiatives:
#     if item.endswith('json'):
#         print(item)
