import pandas as pd
import sys
import geopandas as gpd
import csv
import shapely

#intersections base (base.csv)
intersections = open(sys.argv[1]) #read in NYC intersections shapefile
intersections_reader = csv.reader(intersections, delimiter=',')

# infile csv (clean fatalities/injuries csv)
accidents = open(sys.argv[2])
accidents_reader = csv.reader(accidents, delimiter=',')

#outfile csv
outfile = open(sys.argv[3],'w') #read in output csv file
writer = csv.writer(outfile)

#row dicts
header1 = next(intersections_reader, None) #read in header row
enum_header = enumerate(header1)
i_header_dict = {}
for num,index in enum_header:
    i_header_dict[index] = num

header2 = next(accidents_reader, None) #read in header row
enum_header = enumerate(header2)
a_header_dict = {}
for num,index in enum_header:
    a_header_dict[index] = num

out_header = ('NODEID','Lon','Lat','Fatalities','PedFatalit','BikeFatali', 'MVOFatalit')
#writer.writerow(out_header) #write header row

accident_list = []
for a_row in accidents_reader:
    accident_list.append(a_row[a_header_dict['NODEID']])

#
for i_row in intersections_reader:
    i_node = i_row[i_header_dict['NODEID']]
    accidents = open(sys.argv[2])
    accidents_reader = csv.reader(accidents, delimiter=',')
    for a_row in accidents_reader:
        if a_node == i_node:
            print(a_node, i_node)
        else:
            pass
    # if count < 5000:
    #     if i_node in accident_list:
    #         print(True, i_node)
    #     else:
    #         pass
#         for a_row in accidents_reader:
#             a_node = a_row[a_header_dict['NODEID']]
#             print(a_node, i_node)
            # if a_node == i_node:
            #     print(a_node, i_node)
            # else:
            #     pass
                #print(a_node, type(a_node), i_node, type(i_node))
    #         if a_node == i_node:
    #             print(a_node, i_node)
    #             break
    #         else:
    #             pass
    # #
    # match = False
    # for line in reader:
    #     if int(line[header_dict['NODEID']]) == node_id:
    #         match = True
    #         writer.writerow((node_id, lon, lat, line[header_dict['Fatalities']], line[header_dict['PedFatalit']],line[header_dict['BikeFatali']],line[header_dict['MVOFatalit']]))
    #         break
    #     else:
    #         pass
    # if match:
    #     pass
    # else:
    #     writer.writerow((node_id, lon, lat, 0,0,0,0))

intersections.close()
accidents.close()
outfile.close()
