from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:spec_event_id>/', views.ev_desc, name='Event base'),
    # path('calendar/', views.cal, name='Event calendar')    # https://codepen.io/jpag82/pen/Nazayx
]
