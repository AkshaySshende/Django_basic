from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is home page')

def about(request):
    return render(request, 'about.html')
   # return HttpResponse('about')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('services')


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('contact')




