"""
Indicators Summary Project - Google Earth Engine Interface
	W. R. Emanuel, University of Maryland, College Park
	E-Mail: wemanuel@umd.edu
	Gmail: wemanuel@gmail.com
"""

import logging

import ee

# Create a logging service.
# smrylogger = logging.getLogger("smry")
# smrylogger.setLevel(logging.WARNING)

def ee_create_ecorgns_map():
	"""
	ee_create_ecorgns_map( )

	Create an ee.Image for ecoregions features.

	ee_create_ecorgns_map( ) returns a mapid.
	"""

	# Get ecoregion polygons from fusion table as a Feature Collection.
	eco_rgns_table = "ft:1y5dwrUABGxCr0xQ7MPo7LSpvQhVx4vKomQ8HK_im"
	eco_rgns = ee.FeatureCollection(eco_rgns_table)

	img = ee.Image(0).mask(0)
	img = img.paint(eco_rgns, "000000", 2)

	# Get map ID.
	mapid = img.getMapId()
# 	smrylogger.debug("ee_create_ecorgns_map()|mapid: %s", mapid)

	return mapid
