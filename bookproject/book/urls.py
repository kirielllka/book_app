from django.urls import path
from .views import BookClass,BookAboutSearch


urlpatterns = [
    path('books/', BookClass.as_view(), name='book_main'),
    path('books/<str:desc>/', BookAboutSearch.as_view(), name='book_desc_search'),
]