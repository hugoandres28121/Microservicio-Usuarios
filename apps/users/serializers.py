from rest_framework import serializers
from apps.users.models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'username':instance['username'],
            'password':instance['password'],
            'documento':instance['documento'],
            'email':instance['email'],
            'nombres':instance['nombres'],
            'apellidos':instance['apellidos']


        }
