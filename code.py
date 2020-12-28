# '''
# Track Phone Number Location & Provider Using Python
# Author: Gajendra Singh Thakur
# '''

#import the necessary module!
import phonenumbers
#import number from test.py file
from test import number
#import geolocation from module
from phonenumbers import geocoder
#get number details
ch_nmber=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))
from phonenumbers import carrier
service_nmber=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))
