from django.urls import path
from eproduct import views


urlpatterns = [
    path('homepage/', views.homepage),
    path('insertdata/',views.insertCompanyData),
    path('viewdata/',views.viewCompanyData)
]