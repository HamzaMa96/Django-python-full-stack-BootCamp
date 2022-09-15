from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_book/', views.BookCreate.as_view(), name='create_book'),
    path('create_author/', views.AuthorCreate.as_view(), name='create_author'),
    path('create_genre/', views.GenreCreate.as_view(), name='create_genre'),
    path('book_detail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('author_detail/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('genre_detail/<int:pk>/', views.GenreDetail.as_view(), name='genre_detail'),
    path('my_view', views.my_view, name='my_view'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.CheckedOutBooksView.as_view(), name='profile'),
]