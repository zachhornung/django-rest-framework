from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import BandSerializer
from .models import Band


class BandList(ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetail(RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
