from django.urls import path
from .views import home_view, article_view, detail, login_view, logout_view, registration, post_views_up


# app_name = 'blog'


urlpatterns = [
    path('', home_view, name='home'),
    path('article/', article_view, name='article'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('detail/views/<int:pk>/', post_views_up, name='post_views_up'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
]
