# views == onde ficam as funções que vão renderizar as páginas


from django.shortcuts import render
    # render == ferramenta que renderiza o html

def ola_mundo(request):
    contexto = {
        'disciplina': 'fundamentos de redes de computadores',
        'total_de_aulas': 0,
        'aulas_concluidas': 0
    }
    return render(request, 'index.html', contexto)