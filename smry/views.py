"""
smry Application Views
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com

Version 3.2

Version 3.2 Deployed to moses on 26 Jul 2015.

Version 3.1 incorporates sessions in place of cookies.

Version 3.0 incorporates access to Google Earth Engine.

Version 2.0 addresses numerous errors and reorganizes methods
for filtering database objects.

Version 1.8 incorporates site variables.
    Version 1.8.1 incorporates a descriptive text option into
    site models and a corresponding form..

Version 1.7 incorporates about text items.

Version 1.6 incorporates arbitrary text items that are not related
to specific data or images.

Version 1.5 incorporates plots of VCF (tree cover fraction)
distributions by land cover type.
"""

import os
import logging
import pickle

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django import forms

# Import the Earth Engine API and configuration module.
import ee
import config

from smry.models import TextItem, Region, Map, Chart, Legend
from smry.rgn_forms import YearForm_MODIS_LandCover, YearForm_CDL
from smry.rgn_forms import RegionForm, RegionYearForm_MODIS_LandCover
from smry.rgn_forms import YearForm_NLCD

import site_attr
import geo_data_attrs
import text_items
from rgn_images import RegionImages
import palettes
import ee_smry

# Absolute path to subdirectory containing data files.
# A pickle archive in this directory contains summaries of
# land cover by area.
DATA_PATH = "/home/thenan6/public_html/Indicators/static/smry/data"

# Dictionary to map region names to abbreviations. This mapping
# is used to resolve selected discrepancies between region names
# and file names containing data or images for corresponding
# regions.
rgn_to_abbrv = {"Alaska": "AlaskaWH", "Great Plains": "GrtPlns",
                "Midwest": "MidWest", "Northeast": "NorthEast",
                "Northwest": "NorthWest", "Southeast": "SouthEast",
                "Southwest": "SouthWest", "Hawaii": "Hawaii",
                "PuertoRico": "PuertoRicoVirginIS", 
                "Puerto Rico": "PuertoRicoVirginIS",
                "USA48": "USA48",
                "Conterminous 48 U.S. States": "USA48"}
abbrv_to_rgn = {"AlaskaWH": "Alaska", "GrtPlns": "Great Plains",
                "MidWest": "Midwest", "NorthEast": "Northeast",
                "NorthWest": "Northwest", "SouthEast": "Southeast",
                "SouthWest": "Southwest", "Hawaii": "Hawaii",
                "PuertoRicoVirginIS": "PuertoRico", 
                "PuertoRicoVirginIS": "Puerto Rico",
                "USA48": "Conterminous 48 U.S. States"}

# Dictionaries to specify text replacement in html strings.
del_p = {"<p>": "", "</p>": ""}

# Create a logging service.
smrylogger = logging.getLogger("smry")
smrylogger.setLevel(logging.DEBUG)

def index(request):
    """
    index(request)
    
    Site Front Page.

    Presents introductory text and a map of NCA regions. A form
    allows selection of a region. On submit, user is redirected
    to the rgn_smry view at the selected region.
    """
#     smrylogger.debug("INDEX VIEW")

    # Initialize a session.
    site_attr.init_session(request)

    attr_dct = site_attr.set_attrs(request, "modis_lnd_cvr")    
    smrylogger.debug("index( )|attr_dct: %s", attr_dct)

    # Region selection form.
    if request.method == "POST":
        rgn_form = RegionForm(request.POST)        
        if rgn_form.is_valid():
            # Update attributes.
            for key in rgn_form.cleaned_data.keys():
                attr_dct[key] = rgn_form.cleaned_data[key]
#             smrylogger.debug("index( )|attr_dct: %s", attr_dct)

            # Set session attributes to dictionary items.
            site_attr.set_session_attr(request, attr_dct)

            # Create response to redirect to region summary.
            response = HttpResponseRedirect("rgn_smry/")
    else:
        # Create an instance of class RegionForm.
        rgn_form = RegionForm(initial = {
                            "region": abbrv_to_rgn[attr_dct["region"]],
                            "dscrpt_txt": (attr_dct["dscrpt_txt"] == "True")})

        # Get introductory text from the database and process to html.
        intro_text = text_items.get_txt_html("index", "intro_text")
        intro_text_1 = text_items.get_txt_html("index", "intro_text_1",
                            replace = {"<p>": "", "</p>": "<br /><br />"})

        # Load the region summary template.
        index_template = loader.get_template("smry/index.html")
        context = RequestContext(request, {"form": rgn_form,
                    "form_help": rgn_form.form_help,
                    "intro_text": intro_text,
                    "intro_text_1": intro_text_1})
        response = HttpResponse(index_template.render(context))

    return response

def rgn_smry(request):
    """
    rgn_smry(request)
    
    Regional summary view.
    """
#     smrylogger.debug("REGIONAL SUMMARY VIEW")

    # Set attributes.
    attr_dct = site_attr.set_attrs(request, "modis_lnd_cvr")

    # Create an instance of class Region_Region_Form.
    rgn_form = RegionYearForm_MODIS_LandCover(initial = {
                            "region": attr_dct["region"],
                            "year": attr_dct["year"],
                            "dscrpt_txt": attr_dct["dscrpt_txt"]})

    if request.method == "POST":
        # Create an instance of class RegionYearForm and populate
        # with request data.
        rgn_form = RegionYearForm_MODIS_LandCover(request.POST)

        if rgn_form.is_valid():
            # Update attributes.
            for key in rgn_form.cleaned_data.keys():
                attr_dct[key] = rgn_form.cleaned_data[key]
            # logging 1
#             smrylogger.debug("1 rgn_smry( )|attr_dct: %s", attr_dct)

            # Set attributes in session to dictionary items.
            site_attr.set_session_attr(request, attr_dct)
            # logging 2
#             smrylogger.debug("2 rgn_smry( )|attr_dct: %s", attr_dct)
#         else:
            # logging 3
#             smrylogger.debug("3 rgn_smry( )|Warning: rgn_form is invalid")
    else:
        # Create an instance of class RegionForm.
        rgn_form = RegionYearForm_MODIS_LandCover(initial = {
                                "region": attr_dct["region"],
                                "year": attr_dct["year"],
                                "dscrpt_txt": attr_dct["dscrpt_txt"]})
    
    if attr_dct["dscrpt_txt"]:
        # Get descriptive text from the database.
        intro_txt_html = text_items.get_txt_html("rgn_smry",
                                                    "rgn_smry_intro")
        trends_txt_html = text_items.get_txt_html("rgn_smry",
                                    "trends", replace = del_p)
        vcf_txt_html = text_items.get_txt_html("rgn_smry",
                                    "vcf", replace = del_p)
    else:
        intro_txt_html = ""
        trends_txt_html = ""
        vcf_txt_html = ""

    # Get file name attributes from the database.
    # logging 4
#     smrylogger.debug("4 rgn_smry( )|attr_dct: %s", attr_dct)
    # Expand USA48 to full region name.
    if attr_dct["region"] == "USA48":
        region_name = abbrv_to_rgn[attr_dct["region"]]
    else:
        region_name = attr_dct["region"]
    rgn_img = RegionImages()
    rgn_img.rgn_smry_images(region_name, attr_dct["year"])

    # Create distribution table data as a list.
    table_list = create_distr_table_list(attr_dct["region"], attr_dct["year"])

    # Create request context from attributes.    
    dct = rgn_img.attr.dct
    for key in attr_dct.keys():
        dct[key] = attr_dct[key]
    dct["rgn_name"] = attr_dct["region"]
    dct["intro_txt"] = str(intro_txt_html)
    dct["trends_txt"] = str(trends_txt_html)
    dct["vcf_txt"] = str(vcf_txt_html)
    dct["form"] = rgn_form
    dct["form_help"] = rgn_form.form_help
    dct["table_list"] = table_list

    rgn_img = None

    # Load the region summary template.
    rgn_template = loader.get_template("smry/rgn_smry.html")

    # Create context and render.
    context = RequestContext(request, dct)
    response = HttpResponse(rgn_template.render(context))

    return response

def rgn_map(request):
    """
    rgn_map(request)
    
    Display a single map image for the specified region and year.
    """
#     smrylogger.debug("REGIONAL MAP VIEW")

    # Set attributes to session values.
    attr_dct = site_attr.get_session_attr(request)

    rgn_form = RegionYearForm_MODIS_LandCover(request.POST, initial = {
                            "region": attr_dct["region"],
                            "year": attr_dct["year"],
                            "dscrpt_txt": attr_dct["dscrpt_txt"]})
    # 1
#     smrylogger.debug("1 rgn_map( )|rgn_form.initial: %s", rgn_form.initial)

    if request.method == "POST":
        # Create an instance of class RegionYearForm and populate
        # with request data.
        rgn_form = RegionYearForm_MODIS_LandCover(request.POST)

        if rgn_form.is_valid():
            # Update attributes.
            for key in rgn_form.cleaned_data.keys():
                attr_dct[key] = rgn_form.cleaned_data[key]

            # Set attributes in session to dictionary items.
            site_attr.set_session_attr(request, attr_dct)
            # 2
#             smrylogger.debug("2 rgn_map( )|attr_dct: %s", attr_dct)
#        else:
            # 3
#             smrylogger.debug("3 rgn_map( )|Warning: rgn_form is invalid")
    else:
        # Create an instance of class RegionYearForm.
        rgn_form = RegionYearForm_MODIS_LandCover(initial = {
                            "region": attr_dct["region"],
                            "year": attr_dct["year"],
                            "dscrpt_txt": attr_dct["dscrpt_txt"]})

    # Get file name attributes from the database.
    # Expand USA48 to full region name.
    if attr_dct["region"] == "USA48":
        region_name = abbrv_to_rgn[attr_dct["region"]]
    else:
        region_name = attr_dct["region"]
    img = RegionImages()
    img.rgn_map_images(region_name, attr_dct["year"])

    # Create request context from attributes.  
    dct = img.attr.dct
    for key in attr_dct.keys():
        dct[key] = attr_dct[key]
    dct["rgn_name"] = region_name    
    dct["form"] = rgn_form
    dct["form_help"] = rgn_form.form_help

    img = None

    # Load the region map template.
    template = loader.get_template("smry/rgn_map.html")

    # Create context and render.
    context = RequestContext(request, dct)
    response = HttpResponse(template.render(context))

    return response

def rgn_pie_charts(request):
    """
    rgn_pie_charts(request)
    
    Display pie charts at four years.
    """

#     smrylogger.debug("REGION PIE CHARTS VIEW")

    # Set attributes to session values.
    attr_dct = site_attr.get_session_attr(request)
    # 1
#     smrylogger.debug("1 rgn_pie_charts( )|attr_dct: %s", attr_dct)

    if request.method == "POST":
        # Create an instance of class Region_Year_Form and populate
        # with request data.
        rgn_form = RegionYearForm_MODIS_LandCover(request.POST)

        if rgn_form.is_valid():
            # Update attributes.
            for key in rgn_form.cleaned_data.keys():
                attr_dct[key] = rgn_form.cleaned_data[key]
            # 2
#             smrylogger.debug("2 rgn_pie_charts( )|attr_dct: %s", attr_dct)

            # Set attributes in session to dictionary items.
            site_attr.set_session_attr(request, attr_dct)
    else:
        # Create an instance of class RegionForm.
        rgn_form = RegionYearForm_MODIS_LandCover(initial = {
                            "region": attr_dct["region"],
                            "year": attr_dct["year"],
                            "dscrpt_txt": attr_dct["dscrpt_txt"]})

    # 3
#     smrylogger.debug("3 rgn_pie_charts( )|attr_dct: %s", attr_dct)

    # Create year list for pie charts.
    chart_year_list = create_year_list(int(attr_dct["year"]),
                                            2001, 2012, 2)

    # Create an instance of class RegionImages for access to
    # pie chart attributes.
    rgn_img = RegionImages(img_size = "500px")

    # Get pie chart file names.
    # Expand USA48 to full region name.
    if attr_dct["region"] == "USA48":
        region_name = abbrv_to_rgn[attr_dct["region"]]
    else:
        region_name = attr_dct["region"]
    filenames = []

    # Iterate over year list.
    for year in chart_year_list:
        filename = rgn_img.chart_filter(region_name, year, "LC",
                                        rgn_img.img_size, "piechart")
        filenames.append(filename)

    # Create request context from attributes.        
    dct = {}
    for key in attr_dct.keys():
        dct[key] = attr_dct[key]
    dct["rgn_name"] = attr_dct["region"]
    dct["chart_year_list"] = chart_year_list
    dct["filenames"] = filenames
    dct["form"] = rgn_form
    dct["form_help"] = rgn_form.form_help

    rgn_img = None

    # Load the region map template.
    template = loader.get_template("smry/rgn_pie_charts.html")

    # Create context and render.
    context = RequestContext(request, dct)
    response = HttpResponse(template.render(context))

    return response

def land_cover(request):
    """
    land_cover(request)
    
    Global maps of the MODIS land cover data product (MCD12Q), rendered by the
    Google Earth Engine.
    """
    smrylogger.debug("LAND COVER VIEW")

    # Set attributes.
    attr_dct = site_attr.set_attrs(request, "modis_lnd_cvr")

    # Create an instance of YearForm.
    year_form = YearForm_MODIS_LandCover(request.POST,
                            initial = {"year": attr_dct["year"],
                            "opacity": attr_dct["opacity"],
                            "dscrpt_txt": attr_dct["dscrpt_txt"]})
    # 1
    smrylogger.debug("1 land_cover( )|year_form.initial: %s", year_form.initial)

    if request.method == "POST":
        # Create an instance of class YearForm and populate with
        # request data.
        year_form = YearForm_MODIS_LandCover(request.POST)

        if year_form.is_valid():
            # Update attributes.
            for key in year_form.cleaned_data.keys():
                attr_dct[key] = year_form.cleaned_data[key]

            # Set attributes in session to dictionary items.
            site_attr.set_session_attr(request, attr_dct)
            # 2
            smrylogger.debug("2 land_cover( )|attr_dct: %s", attr_dct)
        else:
            # 3
            logmsg = "3 land_cover( )|Warning: year_form is invalid"
            smrylogger.debug(logmsg)            

    else:
        # Create an instance of class YearForm.
        year_form = YearForm_MODIS_LandCover(initial = {
                            "year": attr_dct["year"],
                            "opacity": attr_dct["opacity"],
                            "dscrpt_txt": attr_dct["dscrpt_txt"]})    

    # Initialize Earth Engine. The configuration file config.py
    # contains credentials.
    ee.Initialize(config.EE_CREDENTIALS, config.EE_URL)
    
    # Get color palette.
    palette_str = palettes.igbp_lndcvr()

    # Create Image name.
    img_name = "MODIS/051/MCD12Q1/" + str(attr_dct["year"]) + "_01_01"
    # 4
    smrylogger.debug("4 land_cover( )|img_name: %s", img_name)

    # Get map ID.
    img = ee.Image(img_name).select(["Land_Cover_Type_1"])
    mapid = img.getMapId({'min': 0, 'max': 17, "palette": palette_str})
    # 5
    smrylogger.debug("5 land_cover( )|mapid: %s", mapid)

    # Get ecoregions map ID.
    mapid_eco_rgns = ee_smry.ee_create_ecorgns_map()
    # 6
    smrylogger.debug("6 land_cover( )|mapid_eco_rgns: %s", mapid_eco_rgns)

    # Create request context from attributes.
    # Mapid and token for base map.
    dct = {"mapid": mapid["mapid"], "token": mapid["token"]}

    # Mapid and token for ecoregions FeatureCollection.
    dct["mapid_eco_rgns"] = mapid_eco_rgns["mapid"]
    dct["token_eco_rgns"] = mapid_eco_rgns["token"]

    for key in attr_dct.keys():
        dct[key] = attr_dct[key]

    # Set opacity attribute.
    dct["opacity"] = 0.01 * float(dct["opacity"])

    dct["heading"] = "Global MODIS Land Cover"
    dct["form"] = year_form
    dct["form_action"] = "smry/land_cover/"
    dct["form_help"] = year_form.form_help
    # 7
    smrylogger.debug("7 land_cover( )|dct: %s", dct)

    # Load the ee map template.
    template = loader.get_template("land_cover/ee_map.html")

    # Create context and render.
    context = RequestContext(request, dct)
    response = HttpResponse(template.render(context))

    return response

def cdl(request):
    """
    cdl(request)
    
    USDA NASS Cropland Data Layer (CDL)
    """
#     smrylogger.debug("CDL VIEW")
   
    # Set attributes.
    attr_dct = site_attr.set_attrs(request, "nass_cdl")

    # Form with current year.
    year_form = YearForm_CDL(request.POST,
                initial = {"year": attr_dct["year"],
                "opacity": attr_dct["opacity"],
                "dscrpt_txt": attr_dct["dscrpt_txt"]})
    # 1
#     smrylogger.debug("1 cdl( )|year_form.initial: %s", year_form.initial)

    if request.method == "POST":
        # Create an instance of class YearForm and populate with
        # request data.
        year_form = YearForm_CDL(request.POST)

        if year_form.is_valid():
            # Update attributes.
            for key in year_form.cleaned_data.keys():
                attr_dct[key] = year_form.cleaned_data[key]

            # Set attributes in session to dictionary items.
            site_attr.set_session_attr(request, attr_dct)
            # 2
#             smrylogger.debug("2 cdl( )|attr_dct: %s", attr_dct)
#        else:
            # 3
#             smrylogger.debug("3 cdl( )|Warning: year_form is invalid")

    else:
        # Create an instance of class RegionForm.
        year_form = YearForm_CDL(initial = {"year": attr_dct["year"],
                                "opacity": attr_dct["opacity"],
                                "dscrpt_txt": attr_dct["dscrpt_txt"]})

    # Initialize Earth Engine. The configuration file config.py
    # contains credentials.
    ee.Initialize(config.EE_CREDENTIALS, config.EE_URL)
    
    # Get color palette.
    palette_str = palettes.cdl_palette()
 
    # Derive the image name.
    img_name = "USDA/NASS/CDL/" + str(attr_dct["year"])
    # 4
#     smrylogger.debug("cdl( )|img_name: %s", img_name)
   
    # Get map ID.
    img = ee.Image(img_name).select(["cropland"])
    mapid = img.getMapId({'min': 0, 'max': 255,
                            "palette": palette_str})
    # 5
#     smrylogger.debug("5 cdl( )|mapid: %s", mapid)

    # Get ecoregions map ID.
    mapid_eco_rgns = ee_smry.ee_create_ecorgns_map()
    # 6
#     smrylogger.debug("6 cdl( )|mapid_eco_rgns: %s", mapid_eco_rgns)

    # Create request context from attributes.
    # Mapid and token for base map.
    dct = {"mapid": mapid["mapid"], "token": mapid["token"]}

    # Mapid and token for ecoregions FeatureCollection.
    dct["mapid_eco_rgns"] = mapid_eco_rgns["mapid"]
    dct["token_eco_rgns"] = mapid_eco_rgns["token"]

    for key in attr_dct.keys():
        dct[key] = attr_dct[key]

    # Set opacity attribute.
    dct["opacity"] = 0.01 * float(dct["opacity"])

    dct["heading"] = "USDA NASS Cropland Data Layer"
    dct["form"] = year_form
    dct["form_action"] = "smry/cdl/"
    dct["form_help"] = year_form.form_help
    # 7
#     smrylogger.debug("6 cdl( )|dct: %s", dct)

    # Load the ee map template.
    template = loader.get_template("land_cover/ee_map.html")

    # Create context and render.
    context = RequestContext(request, dct)
    response = HttpResponse(template.render(context))

    return response

def nlcd(request):
    """
    nlcd(request)
    
    National Land Cover Database (NLCD)
    """
#     smrylogger.debug("NLCD VIEW")
   
    # Set attributes.
    attr_dct = site_attr.set_attrs(request, "nlcd")

    # Form with current year.
    year_form = YearForm_NLCD(request.POST,
                initial = {"year": attr_dct["year"],
                "opacity": attr_dct["opacity"],
                "dscrpt_txt": attr_dct["dscrpt_txt"]})
    # 1
#     smrylogger.debug("1 nlcd( )|year_form.initial: %s", year_form.initial)

    if request.method == "POST":
        # Create an instance of class YearForm and populate with
        # request data.
        year_form = YearForm_NLCD(request.POST)

        if year_form.is_valid():
            # Update attributes.
            for key in year_form.cleaned_data.keys():
                attr_dct[key] = year_form.cleaned_data[key]

            # Set attributes in session to dictionary items.
            site_attr.set_session_attr(request, attr_dct)
            # 2
#             smrylogger.debug("2 nlcd( )|attr_dct: %s", attr_dct)
#        else:
            # 3
#             smrylogger.warning("nlcd( )|Warning: year_form is invalid")

    else:
        # Create an instance of class RegionForm.
        year_form = YearForm_NLCD(initial = {"year": attr_dct["year"],
                                "opacity": attr_dct["opacity"],
                                "dscrpt_txt": attr_dct["dscrpt_txt"]})

    # Initialize Earth Engine. The configuration file config.py
    # contains credentials.
    ee.Initialize(config.EE_CREDENTIALS, config.EE_URL)
    
    # Get color palette.
    palette_str = palettes.nlcd_palette()
 
    # Derive the image name.
    img_name = "USGS/NLCD/NLCD" + str(attr_dct["year"])
    # 4
#     smrylogger.debug("4 nlcd( )|img_name: %s", img_name)
   
    # Get map ID.
    img = ee.Image(img_name).select(["landcover"])
    mapid = img.getMapId({'min': 0, 'max': 255,
                            "palette": palette_str})
    # 5
#     smrylogger.debug("5 nlcd( )|mapid: %s", mapid)

    # Get ecoregions map ID.
    mapid_eco_rgns = ee_smry.ee_create_ecorgns_map()
    # 6
#     smrylogger.debug("6 nlcd( )|mapid_eco_rgns: %s", mapid_eco_rgns)

    # Create request context from attributes.
    # Mapid and token for base map.
    dct = {"mapid": mapid["mapid"], "token": mapid["token"]}

    # Mapid and token for ecoregions FeatureCollection.
    dct["mapid_eco_rgns"] = mapid_eco_rgns["mapid"]
    dct["token_eco_rgns"] = mapid_eco_rgns["token"]

    for key in attr_dct.keys():
        dct[key] = attr_dct[key]

    # Set opacity attribute.
    dct["opacity"] = 0.01 * float(dct["opacity"])

    dct["heading"] = "U.S. National Land Cover Database"
    dct["form"] = year_form
    dct["form_action"] = "smry/nlcd/"
    dct["form_help"] = year_form.form_help
#     smrylogger.debug("cdl( )|dct: %s", dct)

    # Load the ee map template.
    template = loader.get_template("land_cover/ee_map.html")

    # Create context and render.
    context = RequestContext(request, dct)
    response = HttpResponse(template.render(context))

    return response

def ee_create_map():
    """
    ee_create_map()
    
    Create a map image on Earth Engine.
    
    ee_create_map() returns the image object.
    """

    lnd_cvr_img = ee.Image("MODIS/051/MCD12Q1/2001_01_01")
    
    # Select band containing the IGBP classification image.
    # Mask all vallues > 17.
    lnd_cvr_img = lnd_cvr_img.select(["Land_Cover_Type_1"])
    lnd_cvr_img = lnd_cvr_img.mask(lnd_cvr_img.lt(18))

#     smrylogger.debug("ee_create_map( )|lnd_cvr_img: %s", lnd_cvr_img)

    return lnd_cvr_img

def about(request):
    """
    about(request)
    
    About view.
    """
#     smrylogger.debug("ABOUT VIEW")
    html = text_items.get_txt_html("about", "about")    
#     smrylogger.debug("html: %s", html)
    title = "U.S. Land Cover Indicators"

    about_template = loader.get_template("smry/about.html")
    context = RequestContext(request, {"title": title, "about_text": html})
    response = HttpResponse(about_template.render(context))

    return response

def fill_attr(src_dct, trg_dct):
    """
    fill_attr(src_dct, trg_dct)
    
    Fill attributes in the source dictionary that do not
    appear in the target. Where a key in the source does not
    appear in the target, the source attribute is copied to
    the target.
    
    fill_attr( ) returns the target dictionary object.
    """
    # Get dictionary keys.
    src_keys = sorted(src_dct.keys())
    trg_keys = trg_dct.keys()
    
    # Iterate over target keys.
    for key in src_keys:
        if not key in trg_keys:
            trg_dct[key] = src_dct[key]
    
#     smrylogger.debug("fill_attr( )|trg_keys: %s", src_keys) 
#     smrylogger.debug("fill_attr( )|trg_keys: %s", sorted(trg_dct.keys()))

    return trg_dct

def create_distr_table_list(region, year):
    """
    create_distr_table_list(region, year)
    
    For the specified region and year, Create a table summarizing
    land cover distribution as a list object. Source data are
    contained in a pickle archive.
    
    create_distr_table_list() returns the list object.
    """

    # Access pickle archive.
    pfile_name = os.path.join(DATA_PATH, "nca_region_smry.p")
    distr_dct = get_distr_dct(pfile_name)
    key_1 = distr_dct.keys()[0]
#     smrylogger.debug("Distribution Dictionary: %s", key_1)


    # Extract legend from Legend objects to lists.
    legend_dct = get_legend_dct()

    # Get fraction of total land cover for the specified region and year.
    rgn_abbvr = rgn_to_abbrv[region]
    year_int = int(year)
    prc_lst = distr_dct[rgn_abbvr][year_int]["prc"]

    # Assemble table elements.
    max_key = 16
    table_list = []
    for key in sorted(legend_dct.keys()):
        if key <= max_key:
            table_list.append((key, legend_dct[key][0], "%6.3f" % prc_lst[key]))
    return table_list

def get_distr_dct(pfile_name):
    """
    get_distr_dct(pfile_name):
    
    Get land cover distribution data from the pickle archive with file name
    pfile_name into a dictionary.
    
    get_distr_dct() returns a dictionary object extracted from the pickle
    archive.
    """
    pfile_name = os.path.join(DATA_PATH, "nca_region_smry.p")
        
    # Access pickle archive.
    try:
        pfile = open(pfile_name, "rb")
        distr_dct = pickle.load(pfile)
    except pickle.PickleError:
        msg = "Error accessing pickle archive."
        error.quit_prg(prg, msg)
    
    pfile.close()
    
    return distr_dct

def get_legend_dct():
    """
    get_legend_dct()
    
    Get legend data from Legend objects into a dictionary.
    """
    
    # Extract legend from Legend objects to lists.
    legend_objs = Legend.objects.all()
    
    # Iterate over Legend objects to extract data into a
    # dictionary mapping names to keys.
    legend_dct = {}
    for obj in legend_objs:
        legend_dct[obj.key] = [obj.name, obj.short_name]
    
    return legend_dct

def create_year_list(year, year_min, year_max, incr):
    """
    create_year_list(year_min, year_max, incr)
    """
    val = year
    val_list = [val]
    for i in range(1, 4):
        if (val + incr) > year_max:
            next = year_min + (val + incr - year_max - 1)
        else:
            next = val + incr
        val = next
        val_list.append(next)
    year_list = []
    for val in sorted(val_list):
        year_list.append(str(val))
    return year_list















































