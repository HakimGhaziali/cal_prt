from django.urls import path
from .views import post_list , CourseFunc


app_name = 'blog'


urlpatterns = [
 path('calculator', post_list, name='post_list'),
 path('', CourseFunc.as_view() , name='coursefunc'),


]


