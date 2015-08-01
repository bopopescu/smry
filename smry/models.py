"""
U.S. Land Cover Indicators - Data Models
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com

Version 1.8

Version 1.8 incorporates a descriptive text option field into the
SiteVars model.

Version 1.7 incorporates adjustments for Django on CentOS 7.

Version 1.6 incorporates class TextItem to contain arbitrary
text not associated with specific data or images.
"""
from django.db import models

class SiteVars(models.Model):
    """
    class SiteVars(models.Model)
    
    crnt_year: Current year for data and image displays;
    crnt_year_list: Current year list for forms;
    crnt_rgn: Current region name for data and image displays; and
    dscrpt_txt: True/False to specify descriptive text.
    """
    crnt_year = models.CharField(max_length = 4, default = "2010")
    crnt_year_list = models.CharField(max_length = 256, default = "2010")
    crnt_rgn = models.CharField(max_length = 50, default = "USA48")
    dscrpt_txt = models.BooleanField(default = False)

class GeoDataAttrs(models.Model):
    """
    class GeoDataAttrs(models.Model)
    
    Geospatial data set attributes.

    data_id: short identifier, unique to the data set.
    name: data set name.    
    years: valid years for which data are available (type = CharField)
            Expessed as a comma separated string (e.g., "2001, 2002, 2004"),
            or as a range "2001-2004". A range is identified by the presence
            of the '-' character.
    descr: description.
    """
    data_id = models.CharField(max_length = 20)
    years = models.CharField(max_length = 256)
    descr = models.CharField(max_length = 512)
    

class TextItem(models.Model):
    """
    class TextItem(models.Model)
    
    An arbitrary text item with fields:
        number: a unique number to identify the item;
        view: a view that the text is associated with;
        name: a short name for convenience in refering to the item;
        title: a title that may be displayed with the text;
        text: the text representing content.
    
    The text may contain html mark-up.
    """
    number = models.IntegerField()
    view = models.CharField(max_length = 80)
    name = models.CharField(max_length = 40)
    title = models.CharField(max_length = 250)
    text = models.TextField()

class Region(models.Model):
    """
    class Region(models.Model)
    
    Region attributes. Each inidcator region is represented by
    a record. A region field is the primary key.
    """
    region = models.CharField(max_length = 10)

    # Short and long region names. The short name corresponds
    # to the region name embedded in associated data file names.
    name = models.CharField(max_length = 40)
    short_name = models.CharField(max_length = 40)

class Map(models.Model):
    """
    class Map(models.Model)
    
    Geospatial map attributes. Each map is associated with a specific
    region and year.
    """
    feature = models.CharField(max_length = 10)
    region = models.ForeignKey(Region)
    rgn_name = models.CharField(max_length = 40)
    year = models.CharField(max_length=4)
    rsl = models.CharField(max_length=10)
    img_size = models.CharField(max_length=10)
    image_filename = models.CharField(max_length = 120)

class Chart(models.Model):
    """
    class Chart(models.Model)
    
    """
    chart_type = models.CharField(max_length=10)
    feature = models.CharField(max_length = 10)
    region = models.ForeignKey(Region)
    rgn_name = models.CharField(max_length = 40)
    years = models.CharField(max_length=100)
    img_size = models.CharField(max_length=10)
    image_filename = models.CharField(max_length = 120)

class Legend(models.Model):
    """
    class Legend(models.Model)
    
    Land cover class legend Model.
    """
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    short_name = models.CharField(max_length=60)
    
    



















