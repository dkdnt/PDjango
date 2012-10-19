from django.shortcuts import render_to_response
from django.template import RequestContext
from mysite.apps.ventas.models import producto
from mysite.apps.home.forms import ContactForm

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
        mensaje = "Esto es un mensaje desde mi vista"
        ctx= {'msg':mensaje}
        return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def productos_view(request):
        prod= producto.objects.filter(status=True) # select  * from ventas_productos where status = True
        ctx = {'productos':prod} 
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def contact_view(request):
        formulario = ContactForm()
        ctx        = {'form':formulario}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))
	




        
