import pandas as pd
import psycopg2 as pg
import geocoder
import googlemaps
import geopandas
import geojson
from shapely.geometry import Point
from geopandas import GeoDataFrame
from geojson import Feature, FeatureCollection
from geojsonio import display


connection = pg.connect("dbname=test")
facilities_df = pd.read_sql_query('SELECT * FROM "facilities"',connection)

#gets api key from secret file
my_key=open('secr', 'r').read()

#accesses googlemaps API
gmaps = googlemaps.Client(key=my_key)


#getting lat/long from geocoder api
facilities_df['latitude'] = facilities_df['address'].apply(geocoder.google).apply(lambda x: x.lat)
facilities_df['longitude'] = facilities_df['address'].apply(geocoder.google).apply(lambda x: x.lng)


# converts lat and long points to coordinate point data type
geo = [Point(xy) for xy in zip(facilities_df.longitude, facilities_df.latitude)]

# sets to geodataframe
#crs = coordinates reference system- google uses epsg:4326
crs = {'init': 'epsg:4326'}

#gets facilities place name from csv/df
site=facilities_df['name']

#geodataframe parameters in documentation
geo_df = GeoDataFrame(site, crs=crs, geometry=geo) 
# fixes json formatting and puts it back into geodataframe
#listcomprehension to serialize json - a list of the dict
# would not need these two lines if json was correct format
l1 = [geojson.dumps(i, sort_keys=True) for i in geo] 
geo_df = GeoDataFrame(l1, crs=crs, geometry=geo) 

# displays to geojsonio
display(geo_df.to_json())