
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:url>/', views.post, name='post'),
    path('category/<slug:url>/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('addpost/', views.addpost, name='addpost'),
    path('post/<int:id>/like', views.AddLike.as_view(), name='like'),
    path('post/<int:id>/dislike', views.AddDislike.as_view(), name='dislike'),
    path('delete/<int:id>/', views.delete, name='deletedata'),
    path('update/<int:id>/', views.update_post, name='updatepost'),
    path('comment/<int:id>/', views.add_comment, name='comment'),
]
