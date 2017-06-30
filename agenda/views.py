# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.utils import timezone
from django.template import loader, Context, RequestContext
from django.db import IntegrityError, transaction
from .models import Contato


def list(request):
    contato_list = Contato.objects.order_by('data_atualizacao')[:5]
    context = {'contato_list': contato_list}
    return render(request, 'agenda/index.html', context)

def create(request):
    
    # If this is a post request we insert the Contato

    if request.method == 'POST':
        try:
            p = Contato(nome=request.POST['nome'],
                        telefone=request.POST['telefone'],
                        url=request.POST['url'],
                        data_criacao=timezone.now(),
                        data_atualizacao=timezone.now())
            p.save()
            return  HttpResponseRedirect('/agenda/list')
        except IntegrityError: 
            raise Http404('INTEGRIDADE VIOLADA - Problema ao gravar o registro')
    else:

        return render(request, 'contato/criar.html')

def update(request, id):
    # If this is a post request we update the Contato

    try:
        contato = Contato.objects.get(pk=id)
        if request.method == 'POST':
            contato.nome = request.POST['nome']
            contato.telefone = request.POST['telefone']
            contato.url = request.POST['url']
            contato.data_atualizacao =timezone.now()
            contato.save()
            return  HttpResponseRedirect('/agenda/list')
        else: 
            t = loader.get_template('contato/criar.html')
            c = RequestContext(request, {
                'contato': contato
            })
            return HttpResponse(t.render(c))

    except Contato.DoesNotExist:
        raise Http404("Question does not exist")
    
    
    

    



def view(request, id):
    try:
        contato = Contato.objects.get(pk=id)
    except Contato.DoesNotExist:
        raise Http404("Question does not exist")
       
    return render(request, 'agenda/view.html', {
        'contato': contato,
        'error_message': "You didn't select a choice.",})



def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)




# Leave the rest of the views (detail, results, vote) unchanged

