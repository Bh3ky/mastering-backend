from rest_framework import serializers

from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.user.serializers import UserSerializer
from core.comment.models import Comment

# TODO: write the CommentSerializer class

class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='public_id')
    post = serializers.SlugRelatedField(read_only=True, slug_field='public_id')

    # method to validate the post field. NB: value shouldn't be editable on `PUT` requests
    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value
    
    # method for passing the edited value
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True

        instance = super().update(instance, validated_data)

        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        author = User.objects.get_object_by_public_id(rep["author"])
        rep['author'] = UserSerializer(author).data

        return rep
    

    class Meta:
        model = Comment
        # List of all the fields that can be included in a request or a response
        fields = [
            'id',
            'post',
            'author',
            'body',
            'edited',
            'created',
            'updated'
        ]
        read_only_fields = ['edited']
