from dadata import Dadata
token = "f7a1591f5e7299109ce8792e99a970066de53bbe"

def getData(request):
    dadata = Dadata(token)
    if request.GET.get('lat') and request.GET.get('lon') and request.GET.get('radius'):
        result = dadata.geolocate(
                name="address", 
                lat=request.GET.get('lat'), 
                lon=request.GET.get('lon'), 
                radius_meters=request.GET.get('radius')
            )
    return result