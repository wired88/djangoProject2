from django.shortcuts import render


# Create your views here.
# alle html Files werden aus dem templates Directory importiert

def index(request):
    return render(request, 'recipies/base.html')
