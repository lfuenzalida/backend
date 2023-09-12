from django.shortcuts import render



# Create your views here.
def inicio (request):
    return render(request, 'views/inicio.html')
def pagina1 (request):
    return render(request, 'views/pagina1.html')
def pagina2(request):
    return render(request, 'views/pagina2.html')
def pagina3(request):
    return render(request, 'views/pagina3.html')
def pagina4(request):
    return render(request, 'views/pagina4.html')
def pagina5(request):
    return render(request, 'views/pagina5.html')
