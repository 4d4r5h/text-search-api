from rest_framework import serializers
from .models import CustomUser, Paragraph, Word

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'dob', 'password', 'created_at', 'modified_at')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            name=validated_data['name'],
            dob=validated_data['dob']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'text')

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'word', 'paragraph')
