from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CiteBookField
# Create your views here.

'''
home function: generates the home page view of the citation generator
'''


def home():
    template = loader.get_template('citationapp/home.html')
    return template


'''
history function displays past citations made by the user. Is displayed
after the form is submitted.
'''


def history(request):
    citation_history = CiteBookField.objects.order_by('-cite_date')[:5]
    template = loader.get_template('citationapp/history.html')
    context = {
        'citation_history': citation_history,
    }
    return HttpResponse(template.render(context, request))


'''
The results function below handles the view for the results of the
provided inputs. It displays the complete citation.
'''


def results(request, citation_id):
    response = "Here is your citation for %s"
    return HttpResponse(response % citation_id)


'''
The fill_form function displays the fields that the user must fill in order to
generate the citation. For now this form will take the inputs for book citations. 
'''


def fill_form(request, citation_id):
    return HttpResponse("Fill out as many blanks as you can to generate your citation.")
