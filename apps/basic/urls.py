from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.basic.views import CategoryListAPIView, AdvertisementListAPIView, DistrictListAPIView, FavoriteAdsListCreateAPIView, \
    ChangePasswordUpdateAPIView, AdvertDocumentView

router = DefaultRouter()

router.register('adverts', AdvertDocumentView, 'adverts')
urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view()),
    path('basic/', AdvertisementListAPIView.as_view(), name='avert-list'),
    # path('district/', DistrictListAPIView.as_view()),
    path('fav-basic/', FavoriteAdsListCreateAPIView.as_view()),
    path('change-password/', ChangePasswordUpdateAPIView.as_view()),

]
