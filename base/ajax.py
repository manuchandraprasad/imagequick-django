from dajaxice.core import Dajax
from dajaxice.decorators import dajaxice_register
from base.models import Station, Slogan

@dajaxice_register
def updatestation(request, option):
    dajax = Dajax()
    stations = Station.objects.filter(formats__pk=option)
    out = []
    for station in stations:
        out.append("<option value='%s'>%s</option>" % (station.id,station.name))

    dajax.assign('#station', 'innerHTML', ''.join(out))
    return dajax.json()