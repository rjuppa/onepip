from __future__ import unicode_literals
from datetime import datetime, timedelta
from django.utils.encoding import python_2_unicode_compatible
import uuid
import json
from django.db import models
from django.conf import settings
import pandas as pd
import numpy as np


class Market(models.Model):
    name = models.CharField("Market", max_length=50, blank=False, null=False)

    def __unicode__(self):
        return u"{0}".format(self.name)


class PriceManager(models.Manager):

    def get_data_aggregated(self, date_from, aggreg_window_in_sec=60):
        # returns aggregated data from DB
        sql = "SELECT MAX(id) as id, market_id, FLOOR(UNIX_TIMESTAMP(created_at) / {}) as p, " \
              "FLOOR(AVG(ask)) as ask, FLOOR(AVG(bid)) as bid, " \
              "MAX(volume) as volume, MAX(created_at) as created_at".format(aggreg_window_in_sec)
        sql += " FROM trading_price"
        sql += " WHERE created_at > '{}'".format(date_from.strftime('%Y-%m-%d %H:%M:%S'))
        sql += " GROUP BY p"
        data = self.raw(sql)
        return data


class Price(models.Model):
    market = models.ForeignKey(Market, null=False, blank=False)
    ask = models.DecimalField(max_digits=16, decimal_places=8)
    bid = models.DecimalField(max_digits=16, decimal_places=8)
    volume = models.DecimalField(max_digits=16, decimal_places=8)
    status = models.PositiveIntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(null=True, blank=True)

    objects = PriceManager()

    class Meta:
        unique_together = ('market', 'created_at')
        ordering = ('created_at',)

    def __unicode__(self):
        return u"{0} - {1} Ask: {2}".format(self.created_at.strftime(), self.market.name, self.ask)

    def __repr__(self):
        return str(self.id)
