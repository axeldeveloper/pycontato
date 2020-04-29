from django.shortcuts import render
from sinesp_client import SinespClient


# Create your views here.

def criar(request):
    # If this is a post request we insert the person

    result = 1
    if request.method == 'POST':
        sc = SinespClient()
        #sc = SinespClient(proxy_address='127.0.0.1', proxy_port=8000)
        result = sc.search(request.POST['placa'])

    context = { 'resultado': result }
    return render(request, 'synesp/criar.html', context)


