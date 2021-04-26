from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def scanner(request):
    return render(request, "core/scanner.html")

def scannerResult(request):
    return render(request, "core/scanner-result.html")

def procesosElectorales(request):
    return render(request, "core/procesos-electorales.html")

def boleta(request):
    return render(request, "core/boleta.html")

def generadorVoto(request):
    return render(request, "core/generadorVoto.html")