from django.conf import settings
from localflavor.us.us_states import STATES_NORMALIZED
from blog.models import Post, Tag, Author, Ad


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }

def sidebar(request):
    return {
        'tags': Tag.objects.all()
    }

def authors(request):
    return {
        'authors': Author.objects.all()
    }

def dates(request):
    return {
        'posts': Post.objects.all()
    }

def advertisements(request):
    state = request.location['region'] # California
    location = STATES_NORMALIZED[state.lower()]
    print settings.MEDIA_URL
    print settings.PROJECT_ROOT
    print settings.MEDIA_ROOT

    return {
        'ad': Ad.objects.filter(state=location).order_by('?').first()
    }