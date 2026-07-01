from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User


class RegisterSerializer(UserSerializer):
    """
    Registration serializer for requests and user creation.
    """
    # Make sure the password is at leat 8 characters long,
    # and no longer than 128 characters and can't be read
    # by the user.
    password = serializers.CharField(
        max_length=128, write_only=True, required=True
    )

    class Meta:
        model = User
        # List of all the fileds that can be included in a request
        # or a response
        fields = [
            'id',
            'bio',
            'avatar',
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]

    def create(self, validated_data):
        # Use the `create_user` method for the UserManager to create
        # a new user.
        return User.objects.create_user(**validated_data)