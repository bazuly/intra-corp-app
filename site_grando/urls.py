from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacation/', include('hr_app.urls'), name='vacation_upload'),
    path('users/', include('users.urls'), name='users'),
    path('news/', include('news_app.urls'), name='news'),
    path('about/', include('about_app.urls'), name='about'),
    path('grando-main-page/', index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('feedback/', include('feedback_app.urls'), name='feedback'),
    path('education', include('education_app.urls'), name='education')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
