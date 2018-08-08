from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from symcrypt import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserCreate.as_view()),
    path('verification/', views.Verification.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    path('forgetpassword/', views.ForgetPassword.as_view()),
    path('setnewpass/', views.SetNewPassword.as_view()),
    path('contacts/', views.ContactView.as_view()),
    path('update/', views.Update.as_view()),
    path('image/', views.GetImage.as_view()),
    url(r'^file/', include('symcrypt.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
