from django.urls import path

from .views import AboutView

urlpatterns = [
    path('<int:pk>', AboutView.as_view(), name='about'),
]
