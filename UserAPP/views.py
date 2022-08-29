from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserAPP.models import Users
from UserAPP.serializers import UserSerializer

# Create your views here.
@csrf_exempt
def userApi(request, id = 0):
    if request.method == 'GET':
        users = Users.objects.all() 
        users_serializer = UserSerializer(users, many = True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data= users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Agregado", safe=False)
    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        user = Users.objects.get(UserId=users_data['UserId'])
        users_serializer = UserSerializer(user, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Actualizado", safe=False)
        return JsonResponse("fallo actu")
    elif request.method == 'DELETE':
        user = Users.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Eliminacion ok", safe=False)
        
        