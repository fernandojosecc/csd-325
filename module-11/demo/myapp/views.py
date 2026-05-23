from django.http import HttpResponse

def home(request):
    return HttpResponse("Contreras says Hello!")