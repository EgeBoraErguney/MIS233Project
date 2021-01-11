from django.db import models


class BigMacIndexes(models.Model):
    date = models.DateField()
    iso_a3 = models.CharField(max_length=5)
    currency_code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    local_price = models.FloatField(max_length=100)
    dollar_ex = models.FloatField(max_length=100)
    USD_raw = models.FloatField(max_length=100)
    EUR_raw = models.FloatField(max_length=100)
    GBP_raw = models.FloatField(max_length=100)
    JPY_raw = models.FloatField(max_length=100)
    CNY_raw = models.FloatField(max_length=100)
    GDP_dollar = models.FloatField(max_length=100)
    adj_price = models.FloatField(max_length=100, default=None, blank=True, null=True)
    USD_adjusted = models.FloatField(max_length=100, default=None, blank=True, null=True)
    EUR_adjusted = models.FloatField(max_length=100, default=None, blank=True, null=True)
    GBP_adjusted = models.FloatField(max_length=100, default=None, blank=True, null=True)
    JPY_adjusted = models.FloatField(max_length=100, default=None, blank=True, null=True)
    CNY_adjusted = models.FloatField(max_length=100, default=None, blank=True, null=True)
