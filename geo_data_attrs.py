"""
Geospatial Data Set Attributes
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com
"""

import logging

from smry.models import GeoDataAttrs

# Create a logging service.
smrylogger = logging.getLogger("smry")
smrylogger.setLevel(logging.WARNING)

def set_current_attrs(data_id):
    """
    set_current_attrs(data_id)
    
    Set current geospatial data attributes to those associated
    with data_id.
    """
    # 1
    smrylogger.debug("1 set_current_attrs( )|data_id: %s", data_id)

    # Get attribute objects from database.
    objs = GeoDataAttrs.objects.all()

    # Get attributes associated with data_id.
    dct = get_attrs(data_id)
 
    # Get current attribute object.
    crnt_objs = objs.filter(data_id__contains="current")
    crnt_obj = crnt_objs[0]

    # Set current attributes to those associated with data_id.
    crnt_obj.descr = dct["descr"]
    crnt_obj.years = dct["years"]
    # 2
    log_msg = "2 set_current_attrs( )|crnt_obj.years: %s"
    smrylogger.debug(log_msg, crnt_obj.years)
    # 3
    log_msg = "3 set_current_attrs( )|crnt_obj.descr: %s"
    smrylogger.debug(log_msg, crnt_obj.descr)   

    # Save current attribute object to the database.    
    crnt_obj.save()
               
    return

def get_attrs(data_id):
    """
    get_geodata_attrs()
    
    Get geospatial data attributes from database. get_attrs( ) returns
    a dictionary mapping attributes to keys.
    """
    # 1
    smrylogger.debug("1 get_attrs( )|data_id: %s", data_id)

    objs = GeoDataAttrs.objects.all()
    objs = objs.filter(data_id__contains=data_id)
    obj = objs[0]
    
    dct = {}
    dct["data_id"] = obj.data_id
    dct["descr"] = obj.descr
    dct["years"] = obj.years
    dct["year_list"] = extr_years(dct["years"])
    # 2
    smrylogger.debug("2 get_attrs( )|dct: %s", dct)
        
    return dct

def extr_years(yr_str):
    """
    extr_years(yr_str)
    
    Extract a list of years from the string yr_str. The string
    may take one of two forms:
    
    "2001-2010": specifying an inclusive range of years, or
    "2001,2004,2008,2012": specifying years to include.
    
    extr_years( ) returns a list of years as type string.
    """
    if '-' in yr_str:
        yr_str = yr_str.strip('"')
        vals = yr_str.split('-')
        vals = list(range(int(vals[0]), int(vals[1]) + 1))

    else:
        vals = yr_str.split(',')

    yrs = [str(x) for x in vals]
    return yrs





























