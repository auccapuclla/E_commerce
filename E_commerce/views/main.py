from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader


def home(request):
<<<<<<< HEAD
    # document_html = open('C:/Users/jhon_/Google Drive UNI/Scripts/Django/E_commerce/E_commerce/templates/main.html')
    # template = Template(document_html.read())
    # document_html.close()
    ctx = Context({'partner': 'Fabio'})
    document = template.render(ctx)
=======
    # document_html = open('../templates/main.html')
    # template = Template(document_html.read())
    # document_html.close()
    # ctx = Context({'partner': 'Fabio'})
    # document = template.render(ctx)
    document = 'ddd'
>>>>>>> 9c225d82fea3dd5d49111f3c8c5f12e9469902c1
    return HttpResponse(document)
