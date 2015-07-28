"""
Region Forms
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com

Forms associated with regions.

class YearForm(forms.Form)
class RegionForm(forms.Form)
class Region_Year_Form(forms.Form)
"""

import logging

from django import forms

import site_attr

# Create a logging service.
# smrylogger = logging.getLogger("smry")
# smrylogger.setLevel(logging.WARNING)

class YearForm_MODIS_LandCover(forms.Form):
	"""
	class YearForm_MODIS_LandCover(forms.Form, years)

	Form providing a ChoiceField for year selection. Valid years
	correspond to availability of MODIS land cover images.

	A BooleanField provides selction to display descriptive text.
	"""

	# Create help text.
	form_help = "Select a year."
	form_help += " Select Text for additional explanations."

	# Year selection by ChoiceField on years.
	choice_list = [(str(x), str(x)) for x in list(range(2001, 2013))]
	year = forms.ChoiceField(choice_list)

	# Opacity selction by ChoiceField.
	opacity_choice_list = [(str(x), str(x)) for x in list(range(10, 110, 10))]
	opacity = forms.ChoiceField(opacity_choice_list)

	# Boolean field to specify the state of descriptive text.
	dscrpt_txt = forms.BooleanField(required = False,
	                        widget = forms.CheckboxInput())

class YearForm_CDL(forms.Form):
	"""
	YearForm_CDL(forms.Form)

	Form providing a ChoiceField for year selection. Valid years
	correspond to availability of USDA NASS Cropland Data Layer
	images.

	A BooleanField provides selction to display descriptive text.

	"""

	# Create help text.
	form_help = "Select a year."
	form_help += " Select Text for additional explanations."

	# Year selection by Choice Field on years.
	choice_list = [(str(x), str(x)) for x in list(range(2010, 2015))]
	year = forms.ChoiceField(choice_list)

	# Opacity selction by ChoiceField.
	opacity_choice_list = [(str(x), str(x)) for x in list(range(10, 110, 10))]
	opacity = forms.ChoiceField(opacity_choice_list)

	# Boolean field to specify the state of descriptive text.
	dscrpt_txt = forms.BooleanField(required = False,
	                        widget = forms.CheckboxInput())

class YearForm_NLCD(forms.Form):
	"""
	YearForm_NLCD(forms.Form)

	Form providing a ChoiceField for year selection. Valid years
	correspond to availability of NLCD images.

	A BooleanField provides selction to display descriptive text.

	"""

	# Create help text.
	form_help = "Select a year."
	form_help += " Select Text for additional explanations."

	# Year selection by Choice Field on years.
	choice_list = [(str(x), str(x)) for x in [1992, 2001, 2006, 2011]]
	year = forms.ChoiceField(choice_list)

	# Opacity selction by ChoiceField.
	opacity_choice_list = [(str(x), str(x)) for x in list(range(10, 110, 10))]
	opacity = forms.ChoiceField(opacity_choice_list)

	# Boolean field to specify the state of descriptive text.
	dscrpt_txt = forms.BooleanField(required = False,
	                        widget = forms.CheckboxInput())

class RegionForm(forms.Form):
    """
    class Region_Form(forms.Form)
    
    Select a region name.
    """

    # Create help text.
    form_help = "Select a region."
    form_help += " Select Text for additional explanations."

    # Region selection by ChoiceField on names.
    region = forms.ChoiceField(
                            [("Alaska", "Alaska"),
                            ("Northeast", "Northeast"),
                            ("Southeast", "Southeast"),
                            ("Midwest", "Midwest"),
                            ("Great Plains", "Great Plains"),
                            ("Northwest", "Northwest"),
                            ("Southwest", "Southwest"),
                            ("Hawaii", "Hawaii"),
                            ("Puerto Rico", "Puerto Rico"),
                            ("Conterminous 48 U.S. States",
                                "Conterminous 48 U.S. States")])

    # Boolean field to specify the state of descriptive text.
    dscrpt_txt = forms.BooleanField(required = False,
                            widget = forms.CheckboxInput())

class RegionYearForm_MODIS_LandCover(forms.Form):
	"""
	class RegionYearForm_MODIS_LandCover(forms.Form)

	Get a region name and year.
	"""

	# Create help text.
	form_help = "Select a region and year."
	form_help += " Select Text for additional explanations."

	# Region selection by ChoiceField on names.
	region = forms.ChoiceField(
	                        [("Alaska", "Alaska"),
	                        ("Northeast", "Northeast"),
	                        ("Southeast", "Southeast"),
	                        ("Midwest", "Midwest"),
	                        ("Great Plains", "Great Plains"),
	                        ("Northwest", "Northwest"),
	                        ("Southwest", "Southwest"),
	                        ("Hawaii", "Hawaii"),
	                        ("Puerto Rico", "Puerto Rico"),
	                        ("Conterminous 48 U.S. States",
	                            "Conterminous 48 U.S. States")])

	# Year selection by Choice Field on years.
	choice_list = [(str(x), str(x)) for x in list(range(2001, 2013))]
	year = forms.ChoiceField(choice_list)

	# Boolean field to specify the state of descriptive text.
	dscrpt_txt = forms.BooleanField(required = False,
	                        widget = forms.CheckboxInput())


























