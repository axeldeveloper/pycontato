# Create your views here.
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from django.template import loader, Context, RequestContext



from .models import Contato


def index(request):
    contato_list = Contato.objects.order_by('data_atualizacao')[:5]
    context = {'contato_list': contato_list}
    return render(request, 'contato/index.html', context)

def detail(request, contato_id):
    try:
        contato = Contato.objects.get(pk=contato_id)
    except Contato.DoesNotExist:
        raise Http404("Question does not exist")
        # Redisplay the question voting form.
        #return render(request, 'polls/detail.html', {
        #    'contato': contato,
        #    'error_message': "You didn't select a choice.",
        #})


    return render(request, 'contato/detail.html', {
        'contato': contato,
        'error_message': "You didn't select a choice.",})

def results(request, contato_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % contato_id)

def vote(request, contato_id):
    return HttpResponse("You're voting on question %s." % contato_id)

def criar(request):
    # If this is a post request we insert the person
    if request.method == 'POST':
        p = Contato(
            nome=request.POST['name'],
            telefone=request.POST['phone'],
            url=request.POST['url'],
            data_criacao =timezone.now() ,
            data_atualizacao =timezone.now() ,
        )
        p.save()

    #t = loader.get_template('inser.html')
    #c = RequestContext(request)
    #return HttpResponse(t.render(c))
    return render(request, 'contato/criar.html')

def edit(request, contato_id):
    p = Contato.objects.get(pk=contato_id)
    if request.method == 'POST':
        p.nome = request.POST['name']
        p.telefone = request.POST['telefone']
        p.url = request.POST['url']
        p.data_criacao =timezone.now()
        p.data_atualizacao =timezone.now()
        p.save()
    t = loader.get_template('contato/criar.html')
    c = RequestContext(request, {
        'contato': p
    })
    return HttpResponse(t.render(c))


# Leave the rest of the views (detail, results, vote) unchanged

