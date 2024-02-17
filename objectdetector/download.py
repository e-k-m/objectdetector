from dataclasses import dataclass
from os import path
from io import BytesIO

import requests
import mercantile
from PIL import Image


@dataclass
class Tile:
	x: float
	y: float
	zoom: float


def tile(lng, lat, zoom):
	t = mercantile.tile(lng, lat, zoom)
	return Tile(t.x, t.y, t.z)


def tile_sets(lng_min, lng_max, lat_min, lat_max, zoom) -> tuple[Tile]:
	ll = tile(lng_min, lat_min, zoom)
	ur = tile(lng_max, lat_max, zoom)
	for x in range(ll.x, ur.x + 1, 3):
		for y in range(ur.y, ll.y + 1, 3):
			yield (
				(Tile(x, y, zoom), Tile(x + 1, y, zoom), Tile(x + 2, y, zoom)),
				(Tile(x, y + 1, zoom), Tile(x + 1, y + 1, zoom), Tile(x + 2, y + 1, zoom)),
				(Tile(x, y + 2, zoom), Tile(x + 1, y + 2, zoom), Tile(x + 2, y + 2, zoom)),
			)


def fetch(url):
	with requests.get(url) as r:
		r.raise_for_status()
		return Image.open(BytesIO(r.content))
		
		
def fetch_tiles(tile_set):
	image = Image.new(mode="RGB", size=(3 * 256, 3 * 256))
		
	for y, row in enumerate(tile_set):
		for x, tile in enumerate(row):
			i = fetch(swiss_image_url(tile))
			image.paste(i, (x * 256, y * 256))
		
	return image

def swiss_image_url(tile):
	return f"https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.swissimage/default/current/3857/{tile.zoom}/{tile.x}/{tile.y}.jpeg"


def swiss_image_path(dir, tile):
	return path.join(dir, f"{tile.zoom}_{tile.x}_{tile.y}.jpeg")


def fetch_region(lng_min, lng_max, lat_min, lat_max, zoom):
	dir = "./data"
	for tile_set in tile_sets(lng_min, lng_max, lat_min, lat_max, zoom):
		image = fetch_tiles(tile_set)
		image.save(swiss_image_path(dir, tile_set[0][0]))
		

if __name__ == "__main__":
	"""
	fetch_region(
		8.52066219474682, 8.535932881047017, 47.33494362929852, 47.34898819750819, 19
	)
	
	fetch_region(
		8.566414803323, 8.583797890802714, 47.331792062829464, 47.34822627430168, 19
	)
	"""
	
	fetch_region(
		8.487021280295124, 8.564874147631457, 47.360823841065354, 47.390922659290425, 19
	)
