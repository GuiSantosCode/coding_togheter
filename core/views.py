# views == onde ficam as funções que vão renderizar as páginas


from django.shortcuts import render
    # render == ferramenta que renderiza o html

def pagina_um(request):
    contexto = {
        'disciplina': 'fundamentos de redes de computadores',
        'total_de_aulas': 0,
        'aulas_concluidas': 0
    }
    return render(request, 'index.html', contexto)


def pagina_dois(request):
    return render(request, 'assuidade.html')