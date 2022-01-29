from pyexpat import model
from django.db.models import fields, manager
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from django.contrib.auth import get_user_model
from .models.pet import Pet
from .models.booking import Booking
from .models.review import Review
from .models.sitter import Sitter


class PetSerializer(serializers.ModelSerializer):
    pet_owner = serializers.StringRelatedField()
    class Meta:
        model = Pet
        fields  = ('id', 'name', 'pet_owner', 'image')

    def create(self, validated_data):
        return Pet(**validated_data)

class SitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitter
        fields = '__all__'

class SitterReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitter
        fields = ('id','first_name')

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','image')


class UserReadSerializer(serializers.ModelSerializer):
    pets_owned = PetSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:       
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } ,'id':{'read_only:False'} }
    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)
    zipcode = serializers.CharField(max_length = 5, required=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data


class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)



class BookingSerializer(serializers.ModelSerializer):
    # pet_owner = UserReadSerializer()
    # sitter = SitterReadSerializer()
    class Meta:
        model = Booking
        fields= ('id','start_date', 'end_date','sitter', 'pet_owner')


class ReviewSerializer(serializers.ModelSerializer):
    sitter = serializers.StringRelatedField()
    pet_owner = serializers.StringRelatedField()
    pet_owner = UserReadSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



