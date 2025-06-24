import json
from .db import user_db_handler as db
from . import serializers
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Post, RegularUser
from django.contrib.auth.hashers import make_password


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


@csrf_exempt
def post_view(request):
    if request.method == "GET":
        try:
            data = list(Post.objects.values())
            return JsonResponse(data= data, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            title = (data.get("title"))
            body = (data.get("body"))
            images = (data.get("images"))
            author_id = int(1)
            if not title or not isinstance(title, str):
                raise ValueError("Invalid post title")
            if not body or not isinstance(body, str):
                raise ValueError("Invalid post body")
            if not author_id or not isinstance(author_id, int):
                raise ValueError("Invalid post author id")
            new_post = Post.objects.create(
                title = title,
                body = body,
                images = images,
                author_id = author_id
            )
            return JsonResponse(data= Post.objects.filter(id=new_post.id).values()[0], safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_id_view(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            if not id:
                raise ValueError("Invalid post id")
            title = (data.get("title"))
            body = (data.get("body"))
            images = (data.get("images"))
            author_id = int(1)
            if not title or not isinstance(title, str):
                raise ValueError("Invalid post title")
            if not body or not isinstance(body, str):
                raise ValueError("Invalid post body")
            if not author_id or not isinstance(author_id, int):
                raise ValueError("Invalid post author id")
            post = Post.objects.get(id=id)
            post.title = title
            post.body = body
            post.images = images
            post.author = RegularUser.objects.get(id=author_id)
            post.save()
            return JsonResponse(data= Post.objects.filter(id=id).values()[0], safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "DELETE":
        try:
            if not id:
                raise ValueError("Invalid post id")
            target_post = Post.objects.get(id = id)
            target_post.delete()
            return JsonResponse(data= {"success": True}, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "GET":
        try:
            if not id:
                raise ValueError("Invalid post id")
            return JsonResponse(data= Post.objects.filter(id=id).values()[0], safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return HttpResponseNotAllowed(["PUT", "DELETE", "GET"])


@csrf_exempt
def regular_user_view(request):
    if request.method == "GET":
        try:
            pass
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "POST":
        try:
            pass
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def regular_user_id_view(request, id):
    if request.method == "PUT":
        try:
            pass
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "DELETE":
        try:
            pass
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "GET":
        try:
            pass
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return HttpResponseNotAllowed(["PUT", "DELETE", "GET"])