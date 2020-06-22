from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'BlogApp'

urlpatterns = [
        path('', views.ArticleListView.as_view(), name="Article-List"),
        path('<int:pk>/', views.ArticleDetailView.as_view(), name="Article-Detail"),
        path('write/', views.ArticleCreateView.as_view(), name="Article-Create"),
        path('update/<int:pk>', views.ArticleUpdateView.as_view(), name="Article-Update"),
        path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name="Article-Delete"),
        ]
