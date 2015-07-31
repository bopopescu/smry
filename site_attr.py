"""
Site Attributes
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com

Methods to maintain site attributes.

A session maintains the following attributes:
    "region", "year", "year_list", "opacity", "descrpt_txt"

29 Jul 2015. Revised get_session_attr(request) to use
session.request.get() with default values.

Version 3.2

Version 3.2 Deployed to moses on 26 Jul 2015.
"""

import os
import logging

from django.http import HttpResponse, HttpResponseRedirect

from smry.models import GeoDataAttrs
import geo_data_attrs

# Create a logging service.
smrylogger = logging.getLogger("smry")
smrylogger.setLevel(logging.WARNING)

def set_attrs(request, geodata_id):
    """
    set_attrs(request, geodata_id)

    Set attributes to session attributes and adjust for consistency
    with the geospatial dataset specified by geodata_id.

    set_attrs( ) returns a dictionary mapping attributes.
    """

    # Set attributes to session values.
    attr_dct = get_session_attr(request)
    # 1
    smrylogger.debug("1 set_attrs( )|attr_dct: %s", attr_dct)

    # Set a geodata_id attribute.
    attr_dct["geodata_id"] = geodata_id

    # Set geospatial data attributes.
    geo_attrs = geo_data_attrs.get_attrs(geodata_id)
    # 2
    smrylogger.debug("2 set_attrs( )|geo_attrs: %s", geo_attrs)

    # Set year list to geospatial attributes. Check that
    # current year is valid. Adjust if required.
    attr_dct["year_list"] = geo_attrs["year_list"]

    # Check that current year is valid. Adjust if required.
    attr_dct = valid_year(attr_dct)

    return attr_dct

def init_session(request):
    """
    init_session(request)
    
    Initialize a session, setting default values of all attributes.
    """
    request.session["region"] = "USA48"
    request.session["year"] = "2010"
    request.session["year_list"] = "2010"
    request.session["opacity"] = "80"
    request.session["dscrpt_txt"] = "False"
    request.session["lrg_fmt"] = "False"

def get_session_attr(request):
    """
    get_session_attr(request)
    
    Extract session attributes to a dictionary.
    """
    dct = {}
    dct["region"] = request.session.get("region", "USA48")
    dct["year"] = request.session.get("year", "2010")
    dct["year_list"] = request.session.get("year_list", "2010")
    dct["opacity"] = request.session.get("opacity", "80")
    dct["dscrpt_txt"] = request.session.get("dscrpt_txt", "False")
    dct["lrg_fmt"] = request.session.get("lrg_fmt", "False")
    return dct

def set_session_attr(request, dct):
    """
    set_session_attr(request, dct)

    Set attributes in session to dictionary items.    
    """
    for key in dct.keys():
        request.session[key] = dct[key]

def valid_year(attr_dct):
    """
    valid_year(attrs, year_list)
    
    Test that current year is valid. If not valid, adjust. The adjusted
    year_list is not saved to the session.
    """
    # 1
    smrylogger.debug("1 valid_year( )|attr_dct: %s", attr_dct)
    year_list = attr_dct["year_list"]
    if not attr_dct["year"] in year_list:
        attr_dct["year"] = year_list[-1]
        # 2
        smrylogger.debug('2 valid_year( )|%s attr_dct["year"]: %s',
                            attr_dct["year"])
    return attr_dct


























