import numpy as np
import pandas as pd
from shapely.geometry import Polygon, Point, MultiPolygon
import geopandas as gp
import os, sys
from shapely import wkt
import shutil


def lonlat_to_point(lon, lat):
    asting = "POINT" + " (" + lon + " " + lat + ")"
    return asting


boundary_path = "world-administrative-boundaries-countries.geojson"
calif = gp.read_file(boundary_path)
polygon = calif["geometry"].iloc[0]

loadpath = '~/aggregate_data/nodes'
suc_path = '~/aggregate_data/america_nodes'
fai_path = '~/aggregate_data/fail'
file_dir = os.listdir(loadpath)
success_list = pd.DataFrame()
failed_list = pd.DataFrame()
os.makedirs(suc_path)
os.makedirs(fai_path)

for file in file_dir:
    copyname = file
    lonlat = file.split('_')
    lonlat[4] = lonlat[4].split('.')[0] + '.' + lonlat[4].split('.')[1]
    lat = str((float(lonlat[1]) + float(lonlat[2])) / 2)
    lon = str((float(lonlat[3]) + float(lonlat[4])) / 2)
    poi = lonlat_to_point(lon, lat)
    point = wkt.loads(poi)
    if polygon.contains(point):
        shutil.copyfile(loadpath + '/' + file, suc_path + '/' + copyname)
    else:
        shutil.copyfile(loadpath + '/' + file, fai_path + '/' + copyname)
