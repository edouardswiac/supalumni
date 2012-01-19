import simplejson, urllib
GEOCODE_BASE_URL = 'http://maps.google.com/maps/api/geocode/json'

def geocode(address, sensor="false", **geo_args):
    geo_args = { 'address': address.encode('utf-8'), 'sensor': sensor}

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = simplejson.load(urllib.urlopen(url))
    
    try:
        res = result['results'][0]['geometry']['location']
        return res
    except IndexError:
        raise Exception("Unable to geocode this address")

# create company info to display on maps
def create_company_infos(company, as_json=True):
    infos = {}
    infos['name'] = company.name
    infos['full_address'] = company.address.__unicode__()
    infos['lat'] = company.address.lat
    infos['lng'] = company.address.long
    infos['url'] = company.get_absolute_url()
    if as_json:
        return simplejson.dumps(infos)
    else:
        return infos
    
def create_company_markers(companies):
    markers = []
    for c in companies:
        markers.append(create_company_infos(c, as_json=False))
    return simplejson.dumps(markers)
