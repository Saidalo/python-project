import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Wiki
from django.http import HttpResponse
from django.db.models import Q


def index(request):
    all_wikis = Wiki.objects.all()
    return render(request, 'index.html', {
        'allWikis': all_wikis,
        'colors': ['',
                   'list-group-item-primary',
                   'list-group-item-secondary',
                   'list-group-item-success',
                   'list-group-item-danger',
                   'list-group-item-warning',
                   'list-group-item-info',
                   'list-group-item-light',
                   'list-group-item-dark'
                   ],

    })


def create_form(request):
    return render(request, 'create.html')


def update_form(request, wiki_id):
    context = {
        'edit': True,
        'wiki': Wiki.objects.get(id=wiki_id)
    }

    return render(request, 'create.html', context)


@csrf_exempt
def create(request):
    if request.method == 'PUT':
        from django.http import QueryDict
        put = QueryDict(request.body)
        wiki_id = put.get('wikiId')
        name = put.get('name')
        topic = put.get('topic')
        wiki = Wiki.objects.get(id=wiki_id)
        wiki.topic = topic
        wiki.name = name
        wiki.save()
        return HttpResponse(json.dumps({'status': 'success'}), content_type="application/json")
    name = request.POST.get("name", "")
    topic = request.POST.get("topic", "")
    Wiki.objects.create(name=name, topic=topic)
    return HttpResponse(json.dumps({'status': 'success'}), content_type="application/json")


def search(request):
    search_value = request.GET.get('q')
    wiki = Wiki.objects.filter(Q(name__contains=search_value) | Q(topic__contains=search_value))
    search_results = []
    for w in wiki:
        if search_value in w.name:
            search_results.append({'value': w.id, 'text': w.name})
        else:
            search_results.append({'value': w.id, 'text': w.topic})
    return HttpResponse(json.dumps(search_results), content_type="application/json")
