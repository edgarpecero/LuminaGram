""" luminagram urls views"""
#django
from django.urls import path
from django.http import HttpResponse
#utilities
from datetime import datetime
import json

def hello_world(request):
    #now = datetime.now()
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse( 'Oh, hi! Current server time is {now}'.format(now=now))

def sort_integers(request):
    """Return JSON response with some integers"""
    #import pdb; pdb.set_trace()
    #numbers = (request.GET['numbers'])
    numbers = [int(i) for i in (request.GET['numbers'].split(','))]
    sorted_ints = sorted(numbers)
    data ={
        'status': 'ok',
        'numbers':sorted_ints,
        'message': 'Integers sorted successfully'
           }
    #import pdb; pdb.set_trace()

    #return HttpResponse('Hi!')
    #return HttpResponse(str(numbers),)
    #return HttpResponse(str(numbers),content_type='application/json')
    return HttpResponse(
                        json.dumps(data, indent= 4),
                        content_type='application/json'
                        )

def say_hi(response, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry, {}, you are not allowed here'.format(name)
    else: 
        message = 'Hello!, {}, Welcome to luminaGram'.format(name)
    return HttpResponse(message)


