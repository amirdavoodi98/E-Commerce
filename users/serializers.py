import re
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from users.models import User


def validate_password(value):
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', value):
        raise ValidationError("Password must contain at least one letter and one digit, and be at least 8 characters long.")


class UserSignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'},
                                     required=True,
                                     write_only=True,
                                     validators=[validate_password])
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
    
    def create(self, validated_data):
        instance: User = super().create(validated_data)
        # use set password method to set password hash
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance