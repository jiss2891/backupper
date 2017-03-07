from django.shortcuts import render

# Create your views here.
def databases(request):

    return render(request, 'crud_databases.html', {})
