from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'age', 'avatar',)
        
class UserSerializer(UserDetailsSerializer):

    profile = ProfileSerializer(source="userprofile")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)

    def update(self, instance, validated_data):
        userprofile_serializer = self.fields['profile']
        userprofile_instance = instance.userprofile
        userprofile_data = validated_data.pop('userprofile', {})

        # to access the 'company_name' field in here
        name = userprofile_data.get('name')
        age = userprofile_data.get('age')
        avatar = userprofile_data.get('avatar')

        # update the userprofile fields
        userprofile_serializer.update(userprofile_instance, userprofile_data)

        instance = super().update(instance, validated_data)
        return instance