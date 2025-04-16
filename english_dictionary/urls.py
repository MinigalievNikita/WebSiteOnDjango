"""
URL configuration for EnglishLearningDictionary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-project', views.about),
    path('guide-help', views.guide),
    path('words-list', views.words_list),
    path('add-word', views.add_word),
    path('send-definition', views.send_definition),
    path('sphere-choose', views.sphere_choose),
    path('definition-check', views.word_check),
    path('word-answer', views.word_answer)
]
