from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expense/', views.expense, name='expense'),
    path('submit/', views.submit, name='submit'),
    path('download/', views.export_csv_record, name='download'),
    path('approve/<int:item_id>/', views.approve, name='approve'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)