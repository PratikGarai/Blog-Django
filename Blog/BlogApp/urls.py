from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'BlogApp'

urlpatterns = [
        path('about/', views.AboutView.as_view() , name = "About"),
        path('', views.ArticleListView.as_view(), name="Article-List"),
        path('<int:pk>/', views.ArticleDetailView.as_view(), name="Article-Detail"),
        path('article/write/', views.ArticleCreateView.as_view(), name="Article-Create"),
        path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name="Article-Update"),
        path('article/<int:pk>/remove/', views.ArticleDeleteView.as_view(), name="Article-Delete"),
        path('drafts/', views.DraftListView.as_view(), name="Draft-List"),
        ]
