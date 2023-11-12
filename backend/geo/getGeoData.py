from dadata import Dadata
from backend import tokens
token = tokens.dadata_token

def getData(request):
    dadata = Dadata(token)
    result = {}
    if request.GET.get('lat') and request.GET.get('long') and request.GET.get('radius'):
        result = dadata.geolocate(
                name="address", 
                lat=request.GET.get('lat'), 
                lon=request.GET.get('long'), 
                radius_meters=request.GET.get('radius')
            )
    return result