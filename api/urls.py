from django.urls import path, include
from .views import cluster_list, wa_blast, broadcast_list
urlpatterns = [
    path('clusters', cluster_list),
    path('broadcast', broadcast_list),
    path('wablast', wa_blast)
]
