from django.urls import path
from three_web import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.List_View.as_view(), name='list'),
    path('plan/', views.Plan_View.as_view(), name='plan'),
    path('request/', views.request_View.as_view(), name='request'),
    path('contact/', views.contact_View.as_view(), name='contact'),
    path('request_next', views.request_next_View.as_view(), name='request_next'),
    path('sample', views.ex_View.as_view(), name='sample'),
]
