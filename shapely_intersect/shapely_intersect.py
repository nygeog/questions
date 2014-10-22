import pandas as pd 
from shapely.geometry import Point, mapping, shape
from fiona import collection
#from shapely.ops import intersection
import shapely.ops

bufSHP = 'data/h1_buf.shp'
intSHP = 'data/h1_buf_int_ct.shp'
ctSHP  = 'data/nyct2010.shp'
with collection(bufSHP, "r") as input:
    schema = input.schema.copy()
    with collection(intSHP, "w", "ESRI Shapefile", schema) as output:
        shapes = []
        for f in input:
            shapes.append(shape(f['geometry']))
        merged = shapes.intersection(ctSHP)
        output.write({
            'properties': {
                'uid': point['properties']['uid']
                },
            'geometry': mapping(merged)
            })