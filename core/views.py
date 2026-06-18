from django.shortcuts import render
    # render == ferramenta que renderiza o html

def ola_mundo(request):
    return render(request, 'index.html')