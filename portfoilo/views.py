from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment  # Import your Comment model
from django.contrib.auth.decorators import login_required


def home_page(request): 
    # return HttpResponse("home page")
    articles = "fuck python"
    return render(request, 'portfoilo/home.html')

def about_me(request):
    return render(request, 'portfoilo/about.html')

# def contact_me(request):
#     return render(request, 'contact.html')

def contact_me(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            print("valid form")
            # Optionally, you can redirect to a success page or do other actions.
            # return redirect('home')
            return redirect('portfoilo:home',)
        else:
             return HttpResponse("error happened in submission of form")
    else:
        form = CommentForm()
    return render(request, 'portfoilo/contact.html', {'form': form})


@login_required(login_url="/accounts/login/")
def view_messages(request):
    messages = Comment.objects.all()  # Retrieve all messages from the database
    return render(request, 'portfoilo/feedback.html', {'messages': messages})
    

def components(request):
    return render(request, 'portfoilo/components.html')