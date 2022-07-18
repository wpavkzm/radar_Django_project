from django.urls import path, re_path
from . import views

app_name = 'sample'

urlpatterns = [
    #path('SmartplugSensor/', views.SmartplugSensor, name='SmartplugSensor'),
    # path('radar/', views.radar.as_view(), name='radar_sensor'),
    path('smartplug/', views.SmartplugSensor.as_view(), name='smartplug_data'),
    path('merge/', views.merge.as_view(), name='merge_data'),
    #path('<int:radar>/', views.radar.as_view, name='radar_sensor'),
    #path('getTestDatas/', views.getTestDatas, name='getTestDatas'),
]
