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

bike_priority_districts = gpd.read_file('data/bike_priority_districts.json')
bpd_geo = bike_priority_districts['geometry'] #geoseries of

for row in reader:
    lon = float(row[9])
    lat = float(row[10])
    point = shapely.geometry.Point(lon, lat)
    point_list = []

    for zone in bpd_geo:
        if zone.contains(point):
            point_list.append(point)
            break
        else:
            pass

    if len(point_list) > 0:
        writer.writerow((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],lon,lat,row[11],row[12],1))
    else:
        writer.writerow((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],lon,lat,row[11],row[12],0))

infile.close()
final.close()
