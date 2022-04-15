from django.urls import path
from . import views

urlpatterns = [
    path('list/bucket/<bucket>/', views.datacatalog_list_bucket),
    path('list/bucket_es/<bucket>/', views.datacatalog_list_bucket_es),
]
