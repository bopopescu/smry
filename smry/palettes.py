"""
Color Palettes
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com

igbp_lndcvr() - IGBP Land Cover
cdl_palette() - USDA NASS Cropland Data Layer
"""

def cdl_palette():
    """
    ee_map_palette( )
    
    Specify map color palette.
    
    ee_map_palette( ) returns the color palette as a string.
    """

    # USDA Cropland Data Layer color palette
    # Extracted from National Version 2014 (Iowa, 2013)
    cdl_palette = [
        'ffffff',
        'ffd300',
        'ff2626',
        '00a8e5',
        'ff9e0c',
        '267000',
        'ffff00',
        '000000',
        '000000',
        '000000',
        '70a500',
        '00af4c',
        'dda50c',
        'dda50c',
        '7fd3ff',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        'e2007c',
        '896354',
        'd8b56b',
        'a57000',
        'd69ebc',
        '707000',
        'ad007c',
        'a05989',
        '700049',
        'd69ebc',
        'd1ff00',
        '7f99ff',
        'd6d600',
        'd1ff00',
        '00af4c',
        'ffa5e2',
        'a5f28c',
        '00af4c',
        'd69ebc',
        '000000',
        'a800e5',
        'a50000',
        '702600',
        '00af4c',
        'b27fff',
        '702600',
        'ff6666',
        'ff6666',
        'ffcc66',
        'ff6666',
        '00af4c',
        '00ddaf',
        '54ff00',
        'f2a377',
        'ff6666',
        '00af4c',
        '7fd3ff',
        'e8bfff',
        'afffdd',
        '00af4c',
        'bfbf77',
        '000000',
        '93cc93',
        'c6d69e',
        'ccbfa3',
        'ff00ff',
        'ff8eaa',
        'ba004f',
        '704489',
        '007777',
        'b29b70',
        'ffff7f',
        '000000',
        'b5705b',
        '00a582',
        'ead6af',
        'b29b70',
        '000000',
        '000000',
        '000000',
        'f2f2f2',
        '9b9b9b',
        '4c70a3',
        '000000',
        '000000',
        '000000',
        '7fb2b2',
        'e8ffbf',
        '000000',
        '000000',
        '000000',
        '00ffff',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '4c70a3',
        'd3e2f9',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '9b9b9b',
        '9b9b9b',
        '9b9b9b',
        '9b9b9b',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        'ccbfa3',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '93cc93',
        '93cc93',
        '93cc93',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        'c6d69e',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        'e8ffbf',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '7fb2b2',
        '000000',
        '000000',
        '000000',
        '000000',
        '7fb2b2',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '000000',
        '00ff8c',
        'd69ebc',
        'ff6666',
        'ff6666',
        'ff6666',
        'ff6666',
        'ff8eaa',
        '334933',
        'e57026',
        'ff6666',
        'ff6666',
        '000000',
        'ff6666',
        'b29b70',
        'ff8eaa',
        'ff6666',
        'ff8eaa',
        'ff6666',
        'ff6666',
        'ff8eaa',
        '00af4c',
        'ffd300',
        'ffd300',
        'ff6666',
        '000000',
        'ff6666',
        '896354',
        'ff6666',
        'ff2626',
        'e2007c',
        'ff9e0c',
        'ff9e0c',
        'a57000',
        'ffd300',
        'a57000',
        '267000',
        '267000',
        'ffd300',
        '000099',
        'ff6666',
        'ff6666',
        'ff6666',
        'ff6666',
        'ff6666',
        'ff6666',
        'ff6666',
        'ff6666',
        'ffd300',
        '267000',
        'a57000',
        '267000',
        '000000'
    ]
    palette_str = ','.join(cdl_palette)

    return palette_str

def nlcd_palette():
    """
    nlcd_palette()

    National Landcover Database palette.

    nlcd_palette() returns the color palette as a string.
    """
    # NLCD Palette
    nlcd_palette = [
        "000000",
        "00fa00",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "476ba1",
        "d1defa",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "decaca",
        "d99482",
        "ee0000",
        "ab0000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "b3aea3",
        "fafafa",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "68ab63",
        "1c6330",
        "b5ca8f",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "a68c30",
        "ccba7d",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "e3e3c2",
        "caca78",
        "99c247",
        "78ae94",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "dcd93d",
        "ab7028",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "bad9eb",
        "b5d4e6",
        "b5d4e6",
        "b5d4e6",
        "b5d4e6",
        "70a3ba",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000",
        "000000"
    ]

    palette_str = ','.join(nlcd_palette)

    return palette_str

def igbp_lndcvr():
    """
    igbp_lndcvr( )
    
    Specify map color palette.
    
    igbp_lndcvr( ) returns the color palette as a string.
    """

    # Color palette based on Terra Visa visulaization.
    igbp_palette = [
        'b3d1ff', #0 Water
        '1b771d', #1 Evergreen Needleleaf Forest
        '368837', #2 Evergreen Broadleaf Forest
        '3eab70', #3 Deciduous Needleleaf Forest
        '3fa83b', #4 Deciduous Broadleaf Forest
        '4d9c3c', #5 Mixed Forest
        'ada47f', #6 Closed Shrublands
        'cdcca4', #7 Open Shrublands
        '9eb473', #8 Woody Savannas
        'c0bf5f', #9 Savannas
        'bcd495', #10 Grasslands
        '92b8ba', #11 Permanent Wetlands
        'd7d672', #12 Croplands
        'cb0814', #13 Urban and Built-up
        'bbe288', #14 Cropland and Natural Vegetation Mosaic
        'c3c3cd', #15 Snow and Ice
        'c6b486', #16 Barren or Sparsely Vegetated
        '6f6f6f'  #17
    ]
    palette_str = ','.join(igbp_palette)

    return palette_str