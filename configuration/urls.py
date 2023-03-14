from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from configuration import settings
from main_ai_yolo.views import PredictAPIView, TestPredictAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', PredictAPIView.as_view()),
    # path('test_view/', QuantityView.as_view()),
    path('test_predict/', TestPredictAPIView.as_view()),
    # path('hello/', predicting)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)