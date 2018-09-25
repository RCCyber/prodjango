from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'linkservice/linkservice.html', )


def in_request(request):
    return render(request, 'linkservice/out.html', {'values': ['http://localhost:8000/5Gh83Nb', ' take it']})
