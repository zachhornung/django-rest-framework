from django.urls import path
from .views import BandList, BandDetail

urlpatterns = [
    path("", BandList.as_view(), name="band_list"),
    path("<int:pk>/", BandDetail.as_view(), name="band_detail"),
]