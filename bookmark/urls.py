from django.urls import path
from bookmark.views import (
    BookmarkListView, BookmarkCreateView, BookmarkDetailView,
    BookmarkUpdateView
)

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
]
