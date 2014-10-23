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

def error(request):
    my_variable = '!'
    my_list = ['testing', 'a', 'list', 'out']
    my_list = ["{}{}".format(list_item, my_variable) for list_item in my_list]
    raise NotImplementedError("Woops! This doesn't exist.")