from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm() # se instancia el form
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email =  EmailMessage(
                'La  Caffetieriera: Nuevo mensaje',
                'De {} <{}> \n\nEscribió:\n\n{}'.format(name,email,content),
                'no-contestar@inbox.mailtrap.io',
                ['johandrijps@gmail.com'],
                reply_to=[email]
            )
            try:
                # Todo ha ido bien
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #redireccionamos si algo no sale bien
                return redirect(reverse('contact')+"?fail")
    return render(request, 'contact/contact.html', {'form': contact_form}) 