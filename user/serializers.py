from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model
from user.models import Account, MealSetting

class MealSettingSerializer(serializers.ModelSerializer):
    account =serializers.CharField(required=False)

    class Meta: 
        model = MealSetting
        fields = ['id', 'account', 'daily_calories',]

class UserSerializer(serializers.ModelSerializer):
    daily_calories = MealSettingSerializer(required=False)

    class Meta:
        model = Account
        include = ['daily_calories',]
        exclude = ('groups', 'user_permissions',)
        validators = [
            UniqueTogetherValidator(
                queryset=get_user_model().objects.all(),
                fields=['email', 'password']
            )
        ]

    def create(self, validated_data):
        daily_calories = validated_data.pop('daily_calories')
        user = Account.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        if (validated_data.get('is_patient') == True):
            MealSetting.objects.create(account=user, **daily_calories)
        return user