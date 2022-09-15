from django.urls import path
from movie import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about),
    path('signup/', views.signup, name='signup'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('<int:movie_id>/create', views.createReview, name='createreview'),
    path('review/<int:review_id>', views.updateReview, name='updatereview'),
    path('review/<int:review_id>/delete',
         views.deleteReview, name='deletereview'),
]
