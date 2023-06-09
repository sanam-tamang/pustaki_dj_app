from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            user = User.objects.create_user(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                image=validated_data['image'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            user.is_active = True
            user.save()
            return user


class UserDetailSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id', 'email','first_name', 'last_name', 'last_login','image','is_active','is_admin','created_at','updated_at' ]
       
