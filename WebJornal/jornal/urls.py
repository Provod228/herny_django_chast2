from django.urls import path, include
from .views import *
from WebJornal import settings

app_name = 'jornal'

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('main_page/', MainPageView.as_view(), name='main-page'),
    path('main_page/add_educational_material', EducationalMaterialAddView.as_view(), name='educational_material_add'),
    path('main_page/download/<int:material_id>/', download_material, name='download_material'),
    path('delete/<int:material_id>/', EducationalMaterialDeleteView.as_view(), name='delete_educational_material'),
    path('accounts/', include('django.contrib.auth.urls')),
]

