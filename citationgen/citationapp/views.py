from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CiteBookField
# Create your views here.


def index(request):
    citation_history = CiteBookField.objects.order_by('-cite_date')[:5]
    template = loader.get_template('citationapp/index.html')
    context = {
        'citation_history': citation_history,
    }
    return HttpResponse(template.render(context, request))


'''
The results function below handles the view for the results of the
provided inputs. It displays the complete citation
'''


def results(request, citation_id):
    response = "Here is your citation for %s"
    return HttpResponse(response % citation_id)
