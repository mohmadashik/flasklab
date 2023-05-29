from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.

def cred_home(request):
    return HttpResponse('Hello Dude...This is Credentials App')
def user_credential(request):
    return JsonResponse({"username":"ashikg"})
