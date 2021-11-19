from django.http import HttpResponse
from django.template import Template, Context


def home(request):
    # document_html = open('../templates/main.html')
    # template = Template(document_html.read())
    # document_html.close()
    # ctx = Context({'partner': 'Fabio'})
    # document = template.render(ctx)
    document = 'ddd'
    return HttpResponse(document)
