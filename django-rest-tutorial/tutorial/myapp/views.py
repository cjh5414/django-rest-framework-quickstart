from rest_framework import viewsets
from myapp.serializers import PersonSerialier
from myapp.models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerialier