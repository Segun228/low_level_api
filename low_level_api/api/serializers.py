import json
from django.http import JsonResponse


def user_deserializer(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return None, JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not isinstance(username, str):
        return None, JsonResponse({"error": "Invalid username"}, status=400)
    if not email or not isinstance(email, str):
        return None, JsonResponse({"error": "Invalid email"}, status=400)
    if not password or not isinstance(password, str):
        return None, JsonResponse({"error": "Invalid password"}, status=400)

    return {
        "username": username,
        "email": email,
        "password": password
    }, None


def user_serializer(info):
    id, username, email, password = info[0], info[1], info[2], info[3]
    data = {
        "id": id,
        "username": username,
        "password": password,
        "email": email,
    }
    return data


def user_serializer_helper(info):
    id, username, email, password = info[0], info[1], info[2], info[3]
    data = {
        "id": id,
        "username": username,
        "password": password,
        "email": email,
    }
    return data


def user_list_serializer(info):
    result = []
    for chunk in info:
        result.append(user_serializer_helper(chunk))
    return result
