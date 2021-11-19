from django.http import HttpResponse
from django.template import Template, Context


def home(request):
    document_html = open('C:/Users/jhon_/Google Drive UNI/Scripts/Django/E_commerce/E_commerce/templates/main.html')
    template = Template(document_html.read())
    document_html.close()
    ctx = Context({'partner': 'Fabio'})
    document = template.render(ctx)
    return HttpResponse(document)
