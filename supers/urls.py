from django.urls import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.SupersList.as_view()),
    path('<int:pk>/', views.SupersDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)