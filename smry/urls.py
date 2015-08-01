"""
smry Application URL Configuration
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com
"""

from django.conf.urls import patterns, url
from smry import views

urlpatterns = patterns('',
            url(r"^rgn_smry/", views.rgn_smry, name='rgn_smry'),
            url(r"^rgn_map/", views.rgn_map, name='rgn_map'),
            url(r"^rgn_pie_charts/", views.rgn_pie_charts, name="rgn_pie_charts"),
            url(r"^land_cover/", views.land_cover, name='land_cover'),
            url(r"^cdl/", views.cdl, name="cdl"),
            url(r"^nlcd/", views.nlcd, name="nlcd"),
            url(r"^about/", views.about, name="about"),
            url(r"^$", views.index, name='index') )



