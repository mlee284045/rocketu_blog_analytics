from django.shortcuts import render

# Create your views here.
from analytics.models import Location, View, Page


def dashboard(request):
    data = {
        'pages': Page.objects.all(),
        'views': View.objects.all(),
        'locations': Location.objects.all(),
    }

    return render(request, 'dashboard.html', data)
