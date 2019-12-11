from django.shortcuts import render
from django.views.generic.list import ListView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark


