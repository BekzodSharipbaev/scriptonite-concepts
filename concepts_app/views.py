from django.shortcuts import render

# Create your views here.
def concepts(request):
    return render(request, 'index.html')

