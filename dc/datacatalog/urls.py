from django.urls import path
from . import views

urlpatterns = [
    path('list/buckets/', views.datacatalog_list_existing_buckets), 
    path('list/bucket/<bucket>/', views.datacatalog_list_bucket),
    path('list/bucket_es/<bucket>/', views.datacatalog_list_bucket_es),
]
