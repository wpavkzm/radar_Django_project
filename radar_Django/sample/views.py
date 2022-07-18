from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RadarSensor
from .models import SmartplugSensor
from rest_framework import status
#from .models import get_embedded_connection
from config import settings
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TestDataSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
import datetime
import pymysql
from django.db import connection
import MySQLdb.cursors

pymysql.install_as_MySQLdb()


# get_sys_connection = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sys',
#         'USER': 'root',
#         'PASSWORD': 'wpavkzm',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
#         }
#     }
# }

# get_sys_connection = pymysql.connect(host="localhost",
#                                      user="root",
#                                      password="wpavkzm",
#                                      db="sys")


# class SmartplugSensor(APIView):
#     def get(self, request):
#         return Response('SmartplugSensor get api')

#     def post(self, request):
#         try:
#             data = self.request.data
#             display_name = data["display_name"]
#             conn_status = data["conn_status"]
#             power = data["power"]
#             report_interval = data["report_interval"]
#             push_time = data["push_time"]
#             register_count = data["register_count"]

#             query = "INSERT INTO smartplug_sensor (display_name, conn_status, power, report_interval, push_time, register_count)" \
#                     f"values ('{display_name}', {conn_status}, {power}, {report_interval}, '{push_time}', {register_count})"
#             read_sys = get_sys_connection()
#             try:
#                 with read_sys.cursor() as cursor:
#                     cursor.execute(query)
#                     read_sys.commit()
#             finally:
#                 read_sys.close()
#             return Response({
#                 'message': 'Created',
#                 'status': status.HTTP_201_CREATED}
#             )
#         except Exception as e:
#             print(e)
#             data = {
#                 'message': 'Bad request',
#                 'code': status.HTTP_400_BAD_REQUEST
#             }
#             return Response(data)

# class Radar(APIView):
#     def get(self, request):
#         return Response('radar get api')

#     def post(self, request):
#         try:
#             data = self.request.data
#             mac_address = data["mac_address"]
#             motion_detection = data["motion_detection"]
#             detect_time = data["detect_time"]
#             detect_distance = data["detect_distance"]
#             push_time = data["push_time"]
#             radar_rssi = data["radar_rssi"]

#             query = "INSERT INTO radar_sensor (mac_address, motion_detection, detect_time, detect_distance, push_time, radar_rssi)" \
#                     f"values ('{mac_address}', {motion_detection}, {detect_time}, {detect_distance}, '{push_time}', {radar_rssi})"
#             read_embedded = get_embedded_connection()
#             try:
#                 with read_embedded.cursor() as cursor:
#                     cursor.execute(query)
#                     read_embedded.commit()
#             finally:
#                 read_embedded.close()
#             return Response({
#                 'message': 'Created',
#                 'status': status.HTTP_201_CREATED}
#             )
#         except Exception as e:
#             print(e)
#             data = {
#                 'message': 'Bad request',
#                 'code': status.HTTP_400_BAD_REQUEST
#             }
#             return Response(data)


class merge(APIView):
    def get(self, request):
        datas = RadarSensor.objects.all()
        serializer = TestDataSerializer(datas, many=True)
        return Response(serializer.data)

    def post(self, request):
        datas = RadarSensor.objects.all()
        serializer = TestDataSerializer(datas, many=True)
        print(datas)
        print(type(datas))
        return Response(serializer.data)


class SmartplugSensor(APIView):
    def get(self, request):
        return Response('SmartplugSensor get api')

    def post(self, request):
        try:
            conn = pymysql.connect(host='localhost', user='root',
                                   password='wpavkzm', db='sys', charset='utf8')
            data = self.request.data
            display_name = data["display_name"]
            conn_status = data["conn_status"]
            power = data["power"]
            report_interval = data["report_interval"]
            push_time = data["push_time"]
            register_count = data["register_count"]

            query = "INSERT INTO smartplug_sensor (display_name, conn_status, power, report_interval, push_time, register_count)" \
                    f"values ('{display_name}', {conn_status}, {power}, {report_interval}, '{push_time}', {register_count})"
            read_sys = conn
            try:
                with read_sys.cursor() as cursor:
                    cursor.execute(query)
                    read_sys.commit()
            finally:
                read_sys.close()
            return Response({
                'message': 'Created',
                'status': status.HTTP_201_CREATED}
            )
        except Exception as e:
            print(e)
            data = {
                'message': 'Bad request',
                'code': status.HTTP_400_BAD_REQUEST
            }
            return Response(data)
