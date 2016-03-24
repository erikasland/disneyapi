from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import JsonResponse
from apps.main.models import Data

class Api(View):
    def get(self, request, currdate, prevdate, val):
        print currdate
        print prevdate
        data = Data.objects.filter(curr_time__range=(prevdate, currdate))
        total = 0
        for i in data:
            total = total + i.value
        return JsonResponse({'total': total})
