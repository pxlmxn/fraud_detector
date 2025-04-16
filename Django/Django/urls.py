"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from FraudDetector import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', views.TransactionsView.as_view(), name='transactions'),
    path('transaction/<int:id>', views.TransactionsView.as_view(), name='transaction'),
    path('complaints/', views.ComplaintsView.as_view(), name='complaints'),
    path('complaint/<str:userId>', views.SingleComplaintView.as_view(), name='complaint'),
    path('api/scheme/', SpectacularAPIView.as_view(), name='scheme'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='scheme'), name='docs'), 
]
