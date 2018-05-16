import pandas as pd
import sys

#load CSV into pandas DF
df = pd.read_csv(sys.argv[1], sep=',')

#filter for only 2016 values
df1 = df[df['YR'] == 2016]

#keep only certain columns
cols_to_keep = ['FID', 'YR', 'NODEID','Lon','Lat', 'Fatalities', 'PedFatalit','BikeFatali','MVOFatalit']
df1 = df1[cols_to_keep]

#change to fatality/injury from continuous to categorical
#we don't care about # of fatalities or injuries. just whether one occured
df1['Fatalities'] = df1['Fatalities'].apply(lambda x: 1 if x >= 1 else 0)
df1['PedFatalit'] = df1['PedFatalit'].apply(lambda x: 1 if x >= 1 else 0)
df1['BikeFatali'] = df1['BikeFatali'].apply(lambda x: 1 if x >= 1 else 0)
df1['MVOFatalit'] = df1['MVOFatalit'].apply(lambda x: 1 if x >= 1 else 0)

#write out to csv
df1.to_csv(sys.argv[2], index=False)

#
# node_matches = []
#
# #load CSV into a Pandas dataframe
#
# #filter out all non-2016 values
#
# #iterate DF nodes
# for intersection in df:
#     match = 0
#     for fatality in fatalities:
#         if fatality['nodeID'] == intersection['nodeID']:
#             match += 1
#             row = ('NodeID, Lon, Lat, Fatality, Bike, MVO, Type, Year')
#             writerow(row)
#         else:
#             pass
#
#     if match == 0:
#         #perform attribute calculations
#         writerow('A,B,C')
#
# for intersection in df:
#     if node in node_matches:
#
#
# #NodeID, Lon, Lat, Fatality, Types, Attributes
