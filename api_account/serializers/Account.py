from rest_framework.serializers import ModelSerializer

from api_account.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'first_name', 'last_name', "username", 'email', 'is_staff', 'is_superuser', 'phone', 'age', 'address',
            'role', 'is_active')


class LoginAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username', 'password'
        )
