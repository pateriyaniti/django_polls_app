from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, everyone. You're at the about index.")

# Create your views here.
