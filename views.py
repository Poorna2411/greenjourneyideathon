from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost
from .forms import ContactForm



def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def vr(request):
  template = loader.get_template('vr.html')
  return HttpResponse(template.render())

def underdevelopment(request):
  template = loader.get_template('development.html')
  return HttpResponse(template.render())

def eco_t(request):
  template = loader.get_template('eco_t.html')
  return HttpResponse(template.render())

def topten(request):
  template = loader.get_template('topten.html')
  return HttpResponse(template.render())

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')



