from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'views\index.html')

def main (request):
    return render(request, 'base\main.html')
