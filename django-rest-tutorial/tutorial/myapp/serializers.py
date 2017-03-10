from myapp.models import Person
from rest_framework import serializers


class PersonSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')