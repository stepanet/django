
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from news.models import Articles

urlpatterns = [
    path('', ListView.as_view(
                    queryset=Articles.objects.all().order_by("-date")[:25],
                    template_name="news/posts.html",
                   )
            ),
    path('<slug:pk>/', DetailView.as_view(
                    model=Articles, template_name = "news/post.html",
    )),
]
