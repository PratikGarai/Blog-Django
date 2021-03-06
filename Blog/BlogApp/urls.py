from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'BlogApp'

urlpatterns = [
        path('about/', views.AboutView.as_view() , name = "About"),
        path('', views.ArticleListView.as_view(), name="Article-List"),
        path('<int:pk>/', views.ArticleDetailView.as_view(), name="Article-Detail"),
        path('article/write/', views.ArticleCreateView.as_view(), name="Article-Create"),
        path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name="Article-Update"),
        path('article/<int:pk>/remove/', views.ArticleDeleteView.as_view(), name="Article-Delete"),
        path('drafts/', views.DraftListView.as_view(), name="Draft-List"),
        path('article/<int:pk>/comment/', views.add_comment_to_post, name="Comment-Add"),
        path('comment/<int:pk>/approve/', views.comment_approve, name="Comment-Approve"),
        path('comment/<int:pk>/remove/', views.comment_remove, name="Comment-Remove"),
        path('article/<int:pk>/publish/', views.article_publish, name="Article-Publish"),
        path('accounts/login/', LoginView.as_view(), name = 'login'),
        path('accounts/logout/', views.logout_view_func , name = 'logout'),
        ]
