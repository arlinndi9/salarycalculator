from django.contrib import admin
from django.urls import path,include
from calculate_salary.views import *

urlpatterns = [
    path('',index,name='index'),

]
