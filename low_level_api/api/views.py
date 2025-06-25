from .db import user_db_handler as db
from . import serializers
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_view(request):
    if request.method == "GET":
        try:
            users = db.get_users()
            return JsonResponse(serializers.user_list_serializer(users), safe=False)
        except Exception as e:
            print("GET error:", e)
            return JsonResponse({"error": "Failed to fetch users from DB"}, status=500)

    elif request.method == "POST":
        data, error = serializers.user_deserializer(request)
        if error:
            return error
        print(data)
        try:
            new_user = db.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"]
            )
            return JsonResponse(serializers.user_serializer(new_user), status=201)
        except Exception as e:
            print("POST error:", e)
            return JsonResponse({"error": "Failed to create user"}, status=500)

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def user_id_view(request, id):
    if request.method == "PUT":
        data, error = serializers.user_deserializer(request)
        if error:
            return error
        try:
            new_user = db.edit_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
                id=id
            )
            return JsonResponse(serializers.user_serializer(new_user), status=201)
        except Exception as e:
            print("PUT error:", e)
            return JsonResponse({"error": "Failed to edit user"}, status=500)
    elif request.method == "DELETE":
        try:
            success = db.delete_user(id)
            if success:
                return JsonResponse({"success": True})
        except Exception as e:
            print("DELETE error:", e)
            return JsonResponse({"error": "Failed to delete user from DB"}, status=500)
    elif request.method == "GET":
        try:
            user = db.get_user(id)
            return JsonResponse(serializers.user_serializer(user), safe=False)
        except Exception as e:
            print("GET error:", e)
            return JsonResponse({"error": "Failed to fetch user from DB"}, status=500)
    return HttpResponseNotAllowed(["PUT", "DELETE", "GET"])


