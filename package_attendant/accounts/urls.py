from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)