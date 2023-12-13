from rest_framework import serializers
from .models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "first_name", "password"]

    def create(self, validated_data: dict) -> UserData:
        user = UserData.objects.create(
            email=validated_data['email']
        )
        user.first_name = validated_data.get('first_name', user.first_name)
        user.set_password(validated_data['password'])
        user.save()
        return user
