from . import views
from django.urls import path

urlpatterns = [
    # path('',views.space,name='space'),
    # path('about/',views.about,name='about')
    # path('',views.fall,name='fall')

    path('',views.travelo,name='travelo'),
]