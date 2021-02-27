from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('',views.IndexView.as_view(),name='index'),
	path('post/new/', views.PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
	path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
	path('post/<str:category>', views.JobPostView.as_view(), name='job-posts'),
	path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
	path('post/<int:pk>/comment/', views.CreateComment.as_view(), name='comment-create'),
	path('post/<int:post_pk>/comment/<int:pk>/edit', views.CommentUpdateView.as_view(), name='comment-update'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment-delete'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
