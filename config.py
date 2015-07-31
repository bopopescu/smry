#!/usr/bin/env python
"""
config.py

Configuration for Earth Engine API
    W. R. Emanuel, University of Maryland, College Park
    E-Mail: wemanuel@umd.edu
    Gmail: wemanuel@gmail.com
"""

import ee

# The URL of the Earth Engine API.
EE_URL = 'https://earthengine.googleapis.com'

# The service account email address authorized by Google contact.
EE_ACCOUNT = '344650483656@developer.gserviceaccount.com'

# The private key associated with service account in Privacy Enhanced
# Email format (.pem suffix).
EE_PRIVATE_KEY_FILE = '/var/www/html/Indicators/smry/wre_earth_api_pvt_key.pem'
# EE_PRIVATE_KEY_FILE = '/home/thenan6/public_html/Indicators/smry/wre_earth_api_pvt_key.pem'

# DEBUG_MODE will be True if running in a local development environment.
# DEBUG_MODE = ('SERVER_SOFTWARE' in os.environ and
#              os.environ['SERVER_SOFTWARE'].startswith('Dev'))

# Create credentials for Earth Engine access.
EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)

