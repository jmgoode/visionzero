import csv
import shapely
import geopandas as gpd
#import matplotlib.pyplot as plt

infile = open('data/fatality_yearly_clean.csv','ra')
final = open('data/final.csv','w')

reader = csv.reader(infile,delimiter=',')
writer = csv.writer(final)

header = next(reader, None)
writer.writerow(('FID', 'Join_Count', 'TARGET_FID','Fatalities','PedFatalit','BikeFatali','MVOFatalit','YR','NODEID','Lon', 'Lat','STREET1','STREET2','InBikeZone'))

bike_priority_districts = gpd.read_file('data/initiatives/bike_priority_districts.json')
bpd_geo = bike_priority_districts['geometry'] #geoseries of

#make a point
def make_point(lon_row, lat_row):
    lon = float(row[lon_row])
    lat = float(row[lat_row])
    point = shapely.geometry.Point(lon, lat)
    return point
#
# def checker(type, p):
#     if type == 'Polygon':
#         check_point_in_polygon(p)
#
def check_point_in_polygon(point, zones):
    point_list = []
    for zone in zones:
        if zone.contains(point):
            point_list.append(point)
            break
        else:
            pass

    if len(point_list) > 0:
        writer.writerow((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],lon,lat,row[11],row[12],1))
    else:
        writer.writerow((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],lon,lat,row[11],row[12],0))

for row in reader:
    point = make_point(9,10)
    check_point_in_polygon(point, bpd_geo)

infile.close()
final.close()
