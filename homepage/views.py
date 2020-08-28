from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import BoastsAndRoasts
from homepage.forms import CreatePost

def index(request):
    posts = BoastsAndRoasts.objects.all().order_by('-id')[:]
    return render(request, 'index.html', {"posts": posts})

def createpost_view(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastsAndRoasts.objects.create(isroast = data.get('isroast'), post_content = data.get('post_content'))
            return HttpResponseRedirect("/")
    form = CreatePost()
    return render(request, 'createpost.html', {"form": form})

def boasts_view(request):
    posts = BoastsAndRoasts.objects.filter(isroast='False').order_by('-id')[:]
    return render(request, 'boasts.html', {'posts': posts})

def roasts_view(request):
    posts = BoastsAndRoasts.objects.filter(isroast='True').order_by('-id')[:]
    return render(request, 'roasts.html', {'posts': posts})

def sorted_view(request):
    posts = BoastsAndRoasts.objects.all().order_by()[:]
    return render(request, 'sorted.html', {'posts': posts})

def upvote_view(request, upvote_id):
    print(upvote_id)
    post = BoastsAndRoasts.objects.get(id=upvote_id)
    post.upvote = post.upvote + 1
    return HttpResponseRedirect("/")

def downvote_view(request, downvote_id):
    print(downvote_id)
    post = BoastsAndRoasts.objects.get(id=downvote_id)
    post.downvote = post.downvote -1
    return HttpResponseRedirect("/")