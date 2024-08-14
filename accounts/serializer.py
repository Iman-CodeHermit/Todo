from rest_framework import serializers


def clean_email(value):
    if 'admin' or 'root' in value:
        raise serializers.ValidationError('admin or root cant be in email')


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)

    def validate_username(self, value):
        if value == 'admin' or 'root':
            raise serializers.ValidationError('username cant be admin or root')
        return value
