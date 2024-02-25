from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
class CreateUser(APIView):
    @staticmethod
    def post(request):
        usr_obj: models.UserModel = models.UserModel.objects.get_or_create(
            chat_id=request.data['chat_id'],
            defaults={
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name'],
                'username': request.data['username'],
            })[0]
        usr_obj.save()
        return Response(status=200)