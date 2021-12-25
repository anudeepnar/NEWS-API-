from django.urls import path
from .views import home
app_name = 'news_api'

urlpatterns = [
   path('', home, name='home')
]
