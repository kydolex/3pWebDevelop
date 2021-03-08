from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post,Infomation_Post,List_Post,Sample_Post
from .forms import request_text_Form
from .forms import UserForm,NameForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        Infomation_data = Infomation_Post.objects.order_by("-id")
        Sample_data = Sample_Post.objects.order_by("-id")
        return render(request, 'three_web/index.html', {
            'post_data': post_data,
            'Sample_data': Sample_data,
            'Infomation_data': Infomation_data,
        })


class List_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'three_web/list.html', {
            'List_data': List_data,
        })

class Plan_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'three_web/plan.html', {
            'List_data': List_data,
        })

class request_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'three_web/request.html', {
            'List_data': List_data,
        })


class contact_View(View):
    def get(self, request, *args, **kwargs):
        List_data = List_Post.objects.order_by("-id")
        return render(request, 'three_web/contact.html', {
            'List_data': List_data,
        })

class request_next_View(View):
    def get(self, request, *args, **kwargs):
        params = {'name': '', 'email': '', 'form': None}
        if request.method == 'POST':
            form = request_text_Form(request.POST)
            params['name'] = request.POST['name']
            params['email'] = request.POST['email']
            params['form'] = form
        else:
            params['form'] = request_text_Form()

        return render(request, 'three_web/request_next.html',params)




class ex_View(View):
    def get(self, request, *args, **kwargs):
        params = {'name': '', 'email': '', 'form': None}
        if request.method == 'POST':
            form = UserForm(request.POST)
            params['name'] = request.POST['name']
            params['email'] = request.POST['email']
            params['form'] = form
        else:
            params['form'] = UserForm()
        return render(request, 'three_web/sample.html', params)
        
  


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'three_web/sample.html', {'form': form})

