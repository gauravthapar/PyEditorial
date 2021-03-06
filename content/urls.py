from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.Search.as_view(), name='search'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('create/blog/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', views.BlogArchiveByCategoryPK.as_view(), name='blog_archive_by_category_pk'),
    path('blog/<str:slug>/', views.BlogSingle.as_view(), name='blog_single'),
    path('video_cast/', views.VideoCast.as_view(), name='video_cast'),
    path('video_cast/<int:pk>/', views.VideoCastArchiveByCategoryPK.as_view(), name='video_cast_archive_by_category_pk'),
    path('video_cast/<str:slug>/', views.VideoCastSingle.as_view(), name='video_cast_single'),
    path('podcast/', views.Podcast.as_view(), name='podcast'),
    path('podcast/<int:pk>/', views.PodArchiveByCategoryPK.as_view(), name='podcast_archive_by_category_pk'),
    path('podcast/<str:slug>/', views.PodSingle.as_view(), name='podcast_single'),
]
