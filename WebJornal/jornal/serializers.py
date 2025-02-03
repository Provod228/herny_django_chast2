from rest_framework import serializers
from .models import *


class EducationalMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalMaterial
        fields = ('id', 'title', 'summary', 'material_file', 'subject')

