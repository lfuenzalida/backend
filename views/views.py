from django.shortcuts import render



# Create your views here.
def inicio (request):
    return render(request, 'views/index.html')
def iniciales(request):
    return render(request, 'views/iniciales.html')
def formas(request):
    return render(request, 'views/formas.html')
def legendarios(request):
    return render(request, 'views/legendarios.html')
def paradox(request):
    return render(request, 'views/paradox.html')
