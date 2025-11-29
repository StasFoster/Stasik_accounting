from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# def home(request):
#     return render(request, "Authtificate/index.html")

# def vApi(request):
#     return JsonResponse({"age": 999})

def wellcome(request):
    if request.GET.get("logout") == True:
        pass
    if request.user.is_authenticated:
        pass
    return render(request, "Authtificate/index.html")
