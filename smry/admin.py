from django.contrib import admin
from smry.models import SiteVars, TextItem, Region, Map, Chart, Legend, GeoDataAttrs

# Register your models here.
admin.site.register(SiteVars)
admin.site.register(TextItem)
admin.site.register(Region)
admin.site.register(Map)
admin.site.register(Chart)
admin.site.register(Legend)
admin.site.register(GeoDataAttrs)
