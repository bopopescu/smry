"""
Region Image Module
    W. R. Emanuel, University of Maryland, College Park
    E-mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com

Version 2.0

The Region Image Module provides an interface to the MySQL database
that determines image file names corresponding to specified attributes
through class RegionImages.

class RegionImages(img_size = "300px", large_img_size = "800px")
class RegionImageAttr()
"""

import os
import logging

from smry.models import Region, Map, Chart

# Create a logging service.
smrylogger = logging.getLogger("smry")
smrylogger.setLevel(logging.DEBUG)

class RegionImages:
    """
    class RegionImages
    
    Methods for retrieving regional summary image file names and
    related attributes from the database.
    
    The options img_size and large_image_size specify sizes of
    standard and large images respectively.
    """

    def __init__(self, img_size = "300px", large_img_size = "800px"):
        """       
        Initialize an instance of class RegionImages.
        """
        # Create an instance of class RegionImageAttributes to
        # contain image file names and attributes.
        self.attr = RegionImageAttr()
        
        self.img_size = img_size
        self.large_img_size = large_img_size
        
        self.attr.img_size = self.img_size
        self.attr.large_img_size = self.large_img_size

        return

    def rgn_smry_images(self, region, year):
        """
        rgn_smry_images(region, year)
        
        Get image attributes for region summary pages.
        """
        # 1
        logmsg = "1 rgn_smry_images( )|region: %s, year: %s"
        smrylogger.debug(logmsg, region, year)

        # Get Map objects and extract image file names.
        self.attr.map_filename = self.map_filter(region, year,
                                            "LC", self.img_size)
        self.attr.large_map_filename = self.map_filter(region, year, 
                                            "LC", self.large_img_size)
        self.attr.vcf_map_filename = self.map_filter(region, year,
                                            "VCF", self.img_size)
        self.attr.large_vcf_map_filename = self.map_filter(region, year,
                                            "VCF", self.large_img_size)

        # Get pie chart file name.
        self.attr.pie_chart_filename = self.chart_filter(region, year, "LC",
                                            self.img_size, "piechart")

        # Get distribution plot file name.
        self.attr.plot_filename = self.chart_filter(region, year, "LC",
                                            self.img_size, "plot")

        # Get VCF distribution on land cover file name.
        self.attr.vcf_distr_plot_filename = self.chart_filter(region, year, "VCF", 
                                                    self.img_size, "distr-plot")

        # Create a dictionary to map fle names and attributes.
        self.attr.dct = {"image_filename": self.attr.map_filename,
                    "large_image_filename": self.attr.large_map_filename,
                    "vcf_image_filename": self.attr.vcf_map_filename,
                    "large_vcf_image_filename": self.attr.large_vcf_map_filename,
                    "pie_chart_filename": self.attr.pie_chart_filename,
                    "plot_filename": self.attr.plot_filename,
                    "vcf_distr_plot_filename": self.attr.vcf_distr_plot_filename}

    def rgn_map_images(self, region, year):
        """
        rgn_map_images(region, year)
        
        Get image attributes for region map pages.
        """
        self.attr.map_filename = self.map_filter(region, year,
                                            "LC", self.large_img_size)
        # Create a dictionary to map fle names and attributes.
        self.attr.dct = {"image_filename": self.attr.map_filename}       

    def map_filter(self, region, year, feature, image_size):
        """
        map_filter(region, year, feature, image_size)
        
        Get the name of the file containing the image corresponding to the
        specified region, year, feature, and image size arguments.
        map_filter() implements filters on Map model objects.
        
        map_filter() returns the name of the file associated with the
        specified attributes. If a file name is not identified, then
        map_filter() returns None.
        """

        # 1
        logmsg = "1 map_filter( )|region: %s, year: %s"
        smrylogger.debug(logmsg, region, year)
        smrylogger.debug("1 map_filter( )|feature: %s", feature)
        smrylogger.debug("1 map_filter( )|image_size: %s, chart_type: %s")

        # All Map objects with specified image size.
        image_size = image_size.replace("px", '')
        objects = Map.objects.filter(img_size__contains=image_size)
        # 2
        logmsg = "2 map_filter( )|image_size: %s, objects: %s"
        smrylogger.debug(logmsg, image_size, len(objects))

        # Region filter.   
        objects = objects.filter(rgn_name__contains=region)
        # 3
        logmsg = "3 map_filter( )|region: %s, objects: %s"
        smrylogger.debug(logmsg, region, len(objects))

        # Year filter.
        objects = objects.filter(year__contains=str(year))
        # 4
        logmsg = "4 map_filter( )|year: %s, objects: %s"
        smrylogger.debug(logmsg, year, len(objects))

        # Feature filter.
        objects = objects.filter(feature__contains=feature)
        # 5
        logmsg = "5 map_filter( )|feature: %s, objects: %s"
        smrylogger.debug(logmsg, feature, len(objects))

        if objects:
            obj = objects[0]
            filename = ("smry/maps/" + obj.year
                                            + '/' + obj.image_filename)
        else:
            filename = None
            # 6
            smrylogger.warning("6 map_filter( )|Chart objects not found")

        return filename

    def chart_filter(self, region, year, feature, image_size, chart_type):
        """
        chart_filter(region, year, feature, image_size, chart_type)

        Get Chart object and extract file name. chart_filter() returns
        the name of the file containing the corresponding chart. If
        a file name is not identified, chart_filter() returns None.
        """

        # 1
        logmsg = "1 chart_filter( )|region: %s, year: %s"
        smrylogger.debug(logmsg, region, year)
        smrylogger.debug("1 chart_filter( )|feature: %s", feature)
        logmsg = "1 chart_filter( )|image_size: %s, chart_type: %s"
        smrylogger.debug(logmsg, image_size, chart_type)

        # Filter for feature and type.
        chart_objects = Chart.objects.filter(feature__contains=feature)
        # 2
        logmsg = "2 chart_filter( )|feature: %s, chart_objects: %s"
        smrylogger.debug(logmsg, feature, len(chart_objects))

        chart_objects = Chart.objects.filter(chart_type__contains=chart_type)
        # 3
        logmsg = "3 chart_filter( )|chart_type__contains: %s,"
        logmsg += " chart_objects: %s"
        smrylogger.debug(logmsg, chart_type, len(chart_objects))

        # Filter for image size.
        chart_objects = chart_objects.filter(img_size__contains=image_size)
        # 4
        logmsg = "4 chart_filter( )|img_size: %s, chart_objects: %s"
        smrylogger.debug(logmsg, image_size, len(chart_objects))

        # Filter for region name.
        chart_objects = chart_objects.filter(rgn_name__contains=region)
        # 5
        logmsg = "5 chart_filter( )|region: %s, chart_objects: %s"
        smrylogger.debug(logmsg, region, len(chart_objects))

        if chart_type == "piechart":
            # Filter for year.
            chart_objects = chart_objects.filter(years__contains=str(year))
        # 6
        logmsg = "6 chart_filter( )|year: %s, chart_objects: %s"
        smrylogger.debug(logmsg, year, len(chart_objects))

        if len(chart_objects):
            obj = chart_objects[0]
        else:
            # 7
            smrylogger.warning("7 chart_filter( )|Chart objects not found")

        # Determine path to image files from feature and type.
        if chart_type == "piechart":
            path = "smry/pie_charts/"
        elif chart_type == "plot":
            path = "smry/distr_plts/"
        elif feature == "VCF" and chart_type == "distr-plot":
            path = "smry/vcf_lndcvr_plts/"
        else:
            path = "smry/images"

        # Create full file name.    
        filename = os.path.join(path, obj.image_filename)
        # 8
        smrylogger.debug("8 chart_filter( )|File Name: %s", filename)

        return filename

class RegionImageAttr:
    """
    class RegionImagesAttr
    
    Container for image file names and attributes.
    """



















 
