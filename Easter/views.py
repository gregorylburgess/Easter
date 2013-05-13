from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from Easter.settings import STATIC_URL
from Easter.models import Card, Player, PointSet
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render_to_response(
              'index.html',
              {
               'STATIC_URL': STATIC_URL,
               })
    
def index2(request):
   
    
    return render_to_response(
              'index2.html',
              {
               'STATIC_URL': STATIC_URL,
               
               })
@csrf_exempt
def update(request, field, id):
    print str("moved "+str(id) + " to " + str(field))
    return HttpResponse(status=200)
    