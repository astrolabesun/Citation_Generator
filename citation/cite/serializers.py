from rest_framework import serializers
from cite.models import JournalCitation


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalCitation
        fields = '__all__'
