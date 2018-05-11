from shapely.geometry import Point, Polygon, LineString
import csv
import ast
import geopandas as gpd


#speed_humps = gpd.read_file('data/speed_humps.json.txt')
#print(speed_humps.head())

infile_crash = open('data/clean/fatality_yearly_clean.csv', 'r')
reader_crash = reader = csv.reader(infile_crash,delimiter=',')
#infile_geo = open('data/')

outfile_crash = open('data/clean/point_data_test.csv','w')

writer_crash = csv.writer(outfile_crash)

header = next(reader,None)
print(header)
writer_crash.writerow(('Points'))

points_list = []

def point_to_Point(row_num):
    raw_point = row[row_num]
    x,y = ast.literal_eval(raw_point)
    print(x,y)
    point = Point(x,y)
    return point

for row in reader:
    p = point_to_Point(9)
    points_list.append(p)
#    if speed_humps.intersects(p):
#        print('y')
#    else:
#        print('n')
