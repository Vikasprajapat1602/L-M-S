# library/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('students/', views.students, name='students'),
    path('issue/', views.issue_book, name='issue-book'),  
    path('return/', views.return_book, name='return-book'),  
    path('issue-list/', views.issue_list, name='issue-list'),
    path('clear-fine/<int:pk>/', views.clear_fine, name='clear_fine'),
    path('get-issued-books/', views.get_issued_books, name='get_issued_books'),
    path('get-books/', views.get_books_for_student, name='get_books'),
]
