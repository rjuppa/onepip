
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, PriceSerializer
import helpers
from trading.models import Price


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PriceList(APIView):

    def get_queryset(self):
        return Price.objects.all()

    def get(self, request, mid=1):      # mid is market_id
        hours = int(request.GET.get('hours', 1))
        date_now = datetime.now()   # datetime.strptime('2017-01-23 01:30:14', '%Y-%m-%d %H:%M:%S')    # now
        date_from = date_now - timedelta(hours=hours)
        window_in_min = helpers.get_agg_window_in_min(hours)
        data = Price.objects.get_data_aggregated(date_from, aggreg_window_in_sec=window_in_min*60)
        serializer = PriceSerializer(data, many=True)
        return Response(serializer.data)
