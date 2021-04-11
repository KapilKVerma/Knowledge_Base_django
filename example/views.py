from django.shortcuts import render

# Create your views here.


def exampleHome(request):
    return render(request, 'example/example_home.html')
