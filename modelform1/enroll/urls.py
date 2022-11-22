from django.urls import path
from . import views
urlpatterns = [
    path('registration/',views.ShowData),
    path('success/',views.submited)
    ]