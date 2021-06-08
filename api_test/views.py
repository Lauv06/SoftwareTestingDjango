from django.shortcuts import render

# Create your views here.
# 处理前端发起的网络请求并调用对应的接口返回所需的结果，其实就是控制类

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .services import *


@require_http_methods(["GET"])
def Triangle(request):
    response = {}
    try:
        information = HandleTriangle(request.GET)
        response['reInfo'] = information
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def TriangleTest(request):
    response = {}
    try:
        response['list'] = TestTriangle(request.GET)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def Computer(request):
    response = {}
    try:
        information = HandleComputer(request.GET)
        response['reInfo'] = information
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def ComputerTest(request):
    response = {}
    try:
        response['list'] = TestComputer(request.GET)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def Telephone(request):
    response = {}
    try:
        information = HandleTelephone(request.GET)
        response['reInfo'] = information
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def TelephoneTest(request):
    response = {}
    try:
        response['list'] = TestTelephone(request.GET)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def Calendar(request):
    response = {}
    try:
        information = HandleCalendar(request.GET)
        response['reInfo'] = information
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def CalendarTest(request):
    response = {}
    try:
        response['list'] = TestCalendar(request.GET)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def ATM(request):
    response = {}
    try:
        information = HandleATM(request.GET)
        response['reInfo'] = information
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def ATMTest(request):
    response = {}
    try:
        response['list'] = TestATM(request.GET)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
