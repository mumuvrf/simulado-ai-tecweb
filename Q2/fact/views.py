from django.shortcuts import render, redirect
from .models import Fact

def index(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        curtidas = 0

        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        fact = Fact(descricao=descricao, curtidas=curtidas)
        fact.save()
        return redirect('index')
    else:
        all_facts = Fact.objects.all()
        n_facts = len(all_facts)
        return render(request, 'facts/index.html', {'facts': all_facts, 'n_facts': n_facts})
    
def like(request, primary_key=-1):
    fact = Fact.objects.get(pk=primary_key)
    fact.curtidas = fact.curtidas+1
    fact.save()
    
    return redirect('index')
