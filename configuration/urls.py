from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from configuration import settings
from main_ai_yolo.views import PredictAPIView, predicting, last_predict

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', PredictAPIView.as_view()),
    path('predicting/', predicting, name='predicting'),
    path('last_predict/', last_predict, name='last_predict')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)