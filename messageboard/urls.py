from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, PostDetails, NewPost, DeletePost, NewComment, CommentsList, CommentDetails, CommentDelete, \
    CommentAccept, PostEdit

urlpatterns = [
    path('', Home.as_view(), name='allposts'),
    path('newpost', NewPost.as_view()),
    path('<int:pk>', PostDetails.as_view()),
    path('<int:pk>/delete', DeletePost.as_view()),
    path('<int:pk>/edit', PostEdit.as_view()),
    path('accounts/', include('allauth.urls')),
    path('<int:pk>/comment', NewComment.as_view()),
    path('posts_comments', CommentsList.as_view()),
    path('posts_comments/<int:pk>', CommentDetails.as_view()),
    path('posts_comments/<int:pk>/delete', CommentDelete.as_view()),
    path('posts_comments/<int:pk>/accept', CommentAccept.as_view()),

]
