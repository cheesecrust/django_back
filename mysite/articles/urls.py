"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new, name='new'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('test', views.test, name='test'),
    path('edit/<int:question_id>', views.edit, name='edit'),
    path('delete/<int:question_id>', views.delete, name='delete'),
]
