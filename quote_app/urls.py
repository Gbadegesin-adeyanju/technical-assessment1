from django.urls import path
from .views import quoteview

urlpatterns = [
    path('', quoteview.as_view(), name='quote'),
]