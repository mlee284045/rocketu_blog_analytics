import re
from django.conf import settings
from ipware.ip import get_real_ip
import requests
from analytics.models import Page, View, Location


class LocationMiddleware(object):
    def process_request(self, request):
        # Get the IP Address of this request
        ip = get_real_ip(request)

        # If we didn't get an IP Address and we're developing locally,
        # make an API call to get our IP Address.
        if ip is None and settings.DEBUG:
            ip = requests.get('http://icanhazip.com/').text

        if ip is not None:
            response = requests.get('http://ipinfo.io/{}/json'.format(ip))
            if response.status_code == 200:
                request.location = response.json()
                # Split out the lat and long from the location
                request.location['latitude'], request.location['longitude'] = request.location['loc'].split(',')

        # ip = '162.12.36.2'
        request.ip = ip


class AnalyticsMiddleware(object):
    def process_request(self, request):
        url_path = request.META['PATH_INFO']
        # If url_path starts with admin/, ignore it ie don't create the Page, View, Location
        if re.match(r'^/admin/', url_path) is None and re.match(r'^/analytics/', url_path) is None:
            request_page, created = Page.objects.get_or_create(url=url_path)
            request_location, created = Location.objects.get_or_create(
                city=request.location['city'],
                region=request.location['region'],
                country=request.location['country'],
            )
            View.objects.create(
                page=request_page,
                location=request_location,
                latitude=request.location['latitude'],
                longitude=request.location['longitude'],
            )
        else:
            pass
