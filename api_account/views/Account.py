from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from api_account.models import Account
from api_account.serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(methods=['POST'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(request.data)
        if serializer.is_valid:
            username = request.data.get('username')
            password = request.data.get('password')
            accounts = Account.objects.filter(username=username)
            if accounts.exists():
                account = accounts.first()
                if check_password(password, make_password(account.password)):
                    token = RefreshToken.for_user(account)
                    response = {
                        "email": account.email,
                        "access_token": str(token.access_token),
                        "refresh_token": str(token)
                    }
                    return Response(response, status=status.HTTP_200_OK)
        return Response({"error_message": "Invalid username/password!!"}, status=status.HTTP_400_BAD_REQUEST)
