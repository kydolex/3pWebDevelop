from django.views.generic import View
from django.shortcuts import render
from .models import Post,Infomation_Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        Infomation_data = Infomation_Post.objects.order_by("-id")
        return render(request, 'three_web/index.html', {
            'post_data': post_data,
            'Infomation_data': Infomation_data,
        })