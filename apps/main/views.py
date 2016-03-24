from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import JsonResponse
import random
from models import Data

class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')

class SubmitValue(View):
    def get(self, request, currdate):
        val = random.randrange(1,100)
        Data.objects.create(value=val, curr_time=int(currdate))
        return JsonResponse({'status': 111})