from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Schema, cc
from django.template import Template, Context, loader
from django.utils import log


def index(request):
    list = Schema.objects.order_by('id')[:5]
    output = '.'.join([str(i.deleted) for i in list])
    return HttpResponse(output)


def detail(request, name):
    list = Schema.objects.get(name=name)
    template = loader.get_template('cmdb/detail.html')
    context = {'question': list}
    return HttpResponse(template.render(context))


def rr(request):
    latest_question_list = Schema.objects.order_by('id')[:5]
    template = loader.get_template('cmdb/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context))


def vote(request, question_id):
    question = get_object_or_404(Schema, pk=question_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice', 0)
        try:
            selected_choice = question.cc_set.get(pk=choice_id)
            log(selected_choice)
        except cc.DoesNotExist:
            return render(request, 'cmdb/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

