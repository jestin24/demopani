from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),

    # path('add/',views.addition,name='add'),
    # path('about/',views.about,name='about'),
    # path('detail/',views.detail,name=' detail'),
    # path('contact/',views.contact,name='contact'),
    # path('thanks/',views.thanks,name='thanks'),
]