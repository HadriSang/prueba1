from django.shortcuts import render, HttpResponse

# return HttpResponse('<h1>hola gola</h1>')

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html') 

def store(request):
    return render(request, 'core/store.html')

def blog(request):
    return render(request, 'core/blog.html')


    
