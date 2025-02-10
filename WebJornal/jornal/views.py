from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from django.urls import reverse
from .forms import *
from rest_framework import status
# from .models import EducationalMaterial
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .serializers import *


def download_material(request, material_id):
    educational_material = get_object_or_404(EducationalMaterial, id=material_id)
    file_path = educational_material.material_file.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=educational_material.material_file.name)
    return response


class UserRegistrationView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration.html'

    def get(self, request):
        form = SignUpForm()
        return Response({'form': form})

    def post(self, request) -> Response:
        form = SignUpForm(request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('jornal:main-page'))
        else:
            return Response({'form': form})


class MainPageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_page.html'

    def get(self, request):
        educational_materials = EducationalMaterial.objects.all()
        return Response({
            "educational_materials": EducationalMaterialSerializer(educational_materials, many=True).data,
        })


class EducationalMaterialDeleteView(APIView):
    def post(self, request, material_id):
        try:
            obj = get_object_or_404(EducationalMaterial, id=material_id)
            obj.delete()
            return redirect(reverse('jornal:main-page'))
        except EducationalMaterial.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EducationalMaterialAddView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'educational_material_add.html'

    def get(self, request):
        form = EducationalMaterialForm()
        return Response({'form': form})

    def post(self, request) -> Response:
        form = EducationalMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('jornal:main-page'))
        else:
            return Response({'form': form})
