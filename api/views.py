from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
import requests

# Create your views here.


class Following(APIView):
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}
    def get(self, request):
        params = request.query_params
        username = params["username"]
        response = requests.get(f"https://api.github.com/users/{username}/following")
        print(response)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"Enter a valid username"}, status=status.HTTP_400_BAD_REQUEST)


class Followers(APIView):
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}
    def get(self, request):
        params = request.query_params
        username = params["username"]
        response = requests.get(f"https://api.github.com/users/{username}/followers")
        print(response)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({"Enter a valid username"}, status=status.HTTP_400_BAD_REQUEST)