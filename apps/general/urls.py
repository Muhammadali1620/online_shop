from apps.general.views import home
from django.urls import path


urlpatterns = [
    path('', home, name='home-page' ),
] 