from django.contrib import admin
from .models import Post,Infomation_Post,List_Post,Sample_Post

admin.site.register(Post)
admin.site.register(Infomation_Post)
admin.site.register(Sample_Post)
admin.site.register(List_Post)