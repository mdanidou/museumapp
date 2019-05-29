from django.db import models
# from geoposition.fields import GeopositionField




class CATEGORY(models.Model):
    CATEGORYNAME = models.CharField(max_length=200, db_index=True)
    CATEGORYID = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.CATEGORYNAME

class PRICE(models.Model):
    PRICENAME = models.CharField(max_length=200, db_index=True)
    PRICEID = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.PRICENAME

class MUSEUM(models.Model):
    NAME = models.CharField(max_length=200, db_index=True)
    DESCRIPTION = models.CharField(max_length=10000, db_index=True)
    COUNTRY = models.CharField(max_length=200, db_index=True)
    STATE = models.CharField(max_length=200, db_index=True)
    CITY = models.CharField(max_length=200, db_index=True)
    ADDRESS = models.CharField(max_length=200, db_index=True)
    TK = models.CharField(max_length=200, db_index=True)
    PHONE = models.CharField(max_length=200, db_index=True)
    WEBURL = models.CharField(max_length=1000, db_index=True)
    PHOTOURL = models.CharField(max_length=1000, db_index=True)
    CATEGORYID = models.ForeignKey(CATEGORY, on_delete=models.CASCADE, related_name = 'CATEGORY')
    PRICEID = models.ForeignKey(PRICE, on_delete=models.CASCADE, related_name = 'PRICE')
    MAP = models.CharField(max_length=200, db_index=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='museums', null=True)


    def __str__(self):
        return self.NAME

    class Meta:
        ordering = ('NAME', 'TK')

