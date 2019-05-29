from django.contrib import admin
from .models import MUSEUM, CATEGORY, PRICE

# admin.site.register(Snippet)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['CATEGORYNAME', 'CATEGORYID']
    # prepopulated_fields = {'slug':('CATEGORYNAME',)}
admin.site.register(CATEGORY, CategoryAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display = ['PRICENAME', 'PRICEID']
    # prepopulated_fields = {'slug':('PRICENAME',)}
admin.site.register(PRICE, PriceAdmin)


class MuseumAdmin(admin.ModelAdmin):
    list_display = ['NAME', 'DESCRIPTION', 'COUNTRY', 'STATE', 'CITY', 'ADDRESS', 'TK', 'PHONE','WEBURL', 'PHOTOURL', 'CATEGORYID', 'PRICEID', 'MAP']
    # list_filter = ['category', 'date', 'dog']
    # list_editable = ['description', 'price']
    # prepopulated_fields = {'slug':('NAME',)}
admin.site.register(MUSEUM,MuseumAdmin)