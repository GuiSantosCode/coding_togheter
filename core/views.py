from django.http import HttpResponse
# django.htt == modulo de comunicação via protocolo HTTP


def ola_mundo(request):
    return HttpResponse("Olá mundo")
# HttpResponse == envia uma resposta ao navegador