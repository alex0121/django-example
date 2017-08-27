from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {'text':'hello world'}
    return render(request, 'basic_app/index.html', context_dict)

def basic_app(request):
    return render(request, 'basic_app/basic_app.html')

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
