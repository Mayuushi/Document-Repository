# books/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.book_list, name='book_list'),  # List all books
    path('new/', views.register_book, name='register_book'),  # Register new book
    path('edit/<int:pk>/', views.update_book, name='update_book'),  # Edit book
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),  # Delete book
    path('available/', views.available_books, name='available_books'),  # List available books
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),  # Borrow a book
    path('return/<int:book_id>/', views.return_book, name='return_book'),  # Return a book
    path('borrowed_books/', views.borrowed_books, name='borrowed_books'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
