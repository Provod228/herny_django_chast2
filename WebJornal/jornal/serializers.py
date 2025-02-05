from rest_framework import serializers
from .models import *


class EducationalMaterialSerializer(serializers.ModelSerializer):
    subject = serializers.CharField()

    class Meta:
        model = EducationalMaterial
        fields = ('id', 'title', 'summary', 'material_file', 'subject')

# описание проекта подробное опмание
# описание функция