from dataclasses import dataclass
from os import path

import requests
import mercantile


@dataclass
class Tile:
	x: float
	y: float
	zoom: float


def tile(lng, lat, zoom):
	t = mercantile.tile(lng, lat, zoom)
	return Tile(t.x, t.y, t.z)


def tiles(lng_min, lng_max, lat_min, lat_max, zoom):
	ll = tile(lng_min, lat_min, zoom)
	ur = tile(lng_max, lat_max, zoom)
	for x in range(ll.x, ur.x + 1):
		for y in range(ur.y, ll.y + 1):
			yield Tile(x, y, zoom)


def fetch(url, path):
	# NOTE the stream=True parameter below
	with requests.get(url, stream=True) as r:
		r.raise_for_status()
		with open(path, "wb") as f:
			for chunk in r.iter_content(chunk_size=8192):
				# If you have chunk encoded response uncomment if
				# and set chunk_size parameter to None.
				# if chunk:
				f.write(chunk)


def swiss_image_url(tile):
	return f"https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.swissimage/default/current/3857/{tile.zoom}/{tile.x}/{tile.y}.jpeg"


def swiss_image_path(dir, tile):
	return path.join(dir, f"{tile.zoom}_{tile.x}_{tile.y}.jpeg")


def fetch_tiles(lng_min, lng_max, lat_min, lat_max, zoom):
	dir = "./data"
	for tile in tiles(lng_min, lng_max, lat_min, lat_max, zoom):
		url = swiss_image_url(tile)
		fetch(url, swiss_image_path(dir, tile))


if __name__ == "__main__":
	fetch_tiles(
		8.52066219474682, 8.535932881047017, 47.33494362929852, 47.34898819750819, 19
	)
