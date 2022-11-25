from rest_framework.generics import UpdateAPIView

from ad.models import Ad
from ad.serializers import AdSerializer

from solution.part2.sky_ad.ad.permissions import IsOwner


# TODO добавьте ниже код в соответствии с заданием
class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsOwner]
