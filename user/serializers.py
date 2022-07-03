from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

from user.models import Account


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Account.objects.create(**validated_data)
        user.set_password(password)
        user.save()        
        return user

    class Meta:
        model = Account
        exclude = ('groups', 'user_permissions',)
        validators = [
            UniqueTogetherValidator(
                queryset=get_user_model().objects.all(),
                fields=['email', 'password']
            )
        ]
