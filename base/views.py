# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from base.models import *
import json

''' 
###########################################
The following are function related to Carts 
###########################################
'''

def cart_add(request):
    template = Template.objects.get(pk=request.POST.get('id'))
    data = request.POST
    newItem = {
            
            'id' : data['id'],
            'title' : template['name'],
            'price' : template['price'],
            'statName' : data['statName'],
            'statVoice' : data['statVoice'],
            'fre' : data['fre'],
            'freVoice' : data['freVoice'],
            'posName' : data['posName'],
            'posVoice' : data['posVoice'],

        }
    check = 1
    count = len(request.session['cart'])
    for item in request.session['cart']:
        if newItem == item:
            check = 0
            break
    if check == 1:
        count+=1
        newItem['pid'] = count 
        reqest.session['cart'].append(newItem)
        
    report = {'check':check, 'count':count }
    json_report = json.dumps(report)
    
    return HttpResponse(json_report)

def cart_recount(request):
    ''' Updates the Counter of Cart'''
    count = json.dumps(len(request.session['cart']))
    return HttpResponse(count)

def cart_empty(request):
    ''' Empties Cart After Checkout '''
    del request.session['cart']


'''
##################################################
 The following are search and retreival functions
 ##################################################
 '''

def lister(request):
    '''
       Returns a json encoded value of Stations matching the given format
       
       Keyword Arguments: 
       
        id -- primary key of format
        
       Returns:
       
        HttpRespone as <option>
        
    '''
    type = request.GET.get('type')
    if type=='station':
        items = Station.objects.filter(formats__pk=request.GET.get('id'))
    elif type=='slogan':
        items = Slogan.objects.filter(formats__pk=request.GET.get('id'))
    
    out = []
    for item in items:
        out.append("<option value='%s'>%s</option>" % (item.id,item.name, ))
    
    return HttpResponse(out)

def search_template(format_id,frequency_id,station_id,slogan_id):
    
    format = Format.objects.get(pk=format_id)   
    frequency = Frequency.objects.get(pk=frequency_id)
    station = Station.objects.get(pk=station_id)
    slogan = Slogan.objects.get(pk=slogan_id)
    templates = Template.objects.filter(formats__pk=format.id).filter(station_words__exact=station.words).filter(slogan_words__exact=slogan.words)
    
    return templates, format.real_name, frequency.name, station.name, slogan.name

def find_template(request):
    templates,format,frequency,station,slogan = search_template(request.GET.get('format'),request.GET.get('frequency'),request.GET.get('station'),request.GET.get('slogan'))
    return render(request,'base/search.html',{'templates':templates,'format':format,'frequency':frequency,'station':station, 'slogan':slogan })
