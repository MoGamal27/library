from django.urls import path
from .views import BookAPIView, BookDetailAPIView

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('<int:pk>/', BookDetailAPIView.as_view()),
]
