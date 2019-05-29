from rest_framework import serializers
from snippets.models import MUSEUM
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = MUSEUM
        fields = ('id', 'NAME', 'DESCRIPTION', 'COUNTRY', 'STATE', 'CITY', 'ADDRESS','TK', 'PHONE', 'WEBURL', 'PHOTOURL', 'CATEGORYID', 'PRICEID', 'MAP', 'owner')


class UserSerializer(serializers.ModelSerializer):
    museums = serializers.PrimaryKeyRelatedField(many=True, queryset=MUSEUM.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'museums')