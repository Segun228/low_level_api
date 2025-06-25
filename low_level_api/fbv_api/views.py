import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import Post, RegularUser
from django.contrib.auth.hashers import make_password

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
    fields = ["id", "username", "email"]
    if request.method == "GET":
        try:
            data = list(RegularUser.objects.values(*fields))
            return JsonResponse(data= data, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            username = (data.get("username"))
            email = (data.get("email"))
            password = (data.get("password"))
            if not username or not isinstance(username, str):
                raise ValueError("Invalid username")
            if not email or not isinstance(email, str):
                raise ValueError("Invalid email")
            if not password or not isinstance(password, str):
                raise ValueError("Invalid password format")
            new_user = RegularUser.objects.create(
                username = username,
                email = email,
                password = make_password(password),
            )
            return JsonResponse(data= RegularUser.objects.filter(id=new_user.id).values(*fields)[0], safe=False, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def regular_user_id_view(request, id):
    fields = ["id", "username", "email"]
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            if not id:
                raise ValueError("Invalid user id")
            username = (data.get("username"))
            email = (data.get("email"))
            password = (data.get("password"))
            if not username or not isinstance(username, str):
                raise ValueError("Invalid username")
            if not email or not isinstance(email, str):
                raise ValueError("Invalid email")
            if not password or not isinstance(password, str):
                raise ValueError("Invalid password format")
            target_user = RegularUser.objects.get(id=id)
            target_user.username = username
            target_user.email = email
            target_user.password = make_password(password)
            target_user.save()
            return JsonResponse(data= RegularUser.objects.filter(id=id).values(*fields)[0], safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "DELETE":
        try:
            if not id:
                raise ValueError("Invalid user id")
            target_user = RegularUser.objects.get(id = id)
            target_user.delete()
            return JsonResponse(data= {"success": True}, safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    elif request.method == "GET":
        try:
            if not id:
                raise ValueError("Invalid user id")
            target_user = RegularUser.objects.get(id = id)
            return JsonResponse(data= RegularUser.objects.filter(id=id).values(*fields)[0], safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status = 500)
    return HttpResponseNotAllowed(["PUT", "DELETE", "GET"])
