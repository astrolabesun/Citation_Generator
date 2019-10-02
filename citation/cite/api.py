from cite.models import JournalCitation
from rest_framework import viewsets, permissions
from .serializers import JournalSerializer


# Journal Viewset
class JournalCiteViewset(viewsets.ModelViewSet):
    queryset = JournalCitation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JournalSerializer
