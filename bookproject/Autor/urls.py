from django.urls import path
from .views import AutorClass,AutorSearch


urlpatterns = [
    path('writers/', AutorClass.as_view(), name='main_autor'),
    path('writers/<str:name>/', AutorSearch.as_view(), name='autor_search'),
]