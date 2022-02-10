from http.client import HTTPResponse
import json
from .sequential.main import calculate as sequential_calc
from .generator.main import calculate as generator_calc
from .multiprocessing.main import calculate as multiprocessing_calc
from rest_framework import status
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def calculate_sequential(request):

    data = request.data
    points = []
    for p in data['points']:
        points.append((p[0], p[1]))

    args = {
        'n': data['n'],
        'm': data['m'],
        'points': points
    }

    resp = sequential_calc(args)

    return JsonResponse(resp, safe=False, status=200)


@csrf_exempt
@api_view(['GET', 'POST'])
def calculate_generator(request):

    data = request.data
    points = []
    for p in data['points']:
        points.append((p[0], p[1]))

    args = {
        'n': data['n'],
        'm': data['m'],
        'points': points
    }

    resp = generator_calc(args)

    return JsonResponse(resp, safe=False, status=200)

@csrf_exempt
@api_view(['GET', 'POST'])
def calculate_multiprocessing(request):

    data = request.data
    points = []
    for p in data['points']:
        points.append((p[0], p[1]))

    args = {
        'n': data['n'],
        'm': data['m'],
        'points': points
    }

    resp = multiprocessing_calc(args)

    return JsonResponse(resp, safe=False, status=200)