from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from quote.models import Quote


class QuoteSerializers(ModelSerializer):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tag']
        read_only_fields = ['author',]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'first_last_name')

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password', 'first_last__name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'],
                                        validated_data['first_last_name'])

        return user