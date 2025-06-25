import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Student
from django.views import View


@method_decorator(csrf_exempt, name='dispatch')
class StudentListView(View):
    def get(self, request):
        students = Student.objects.all().values()
        return JsonResponse(list(students), safe=False, status = 200)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            student = Student.objects.create(
                first_name=data["first_name"],
                second_name=data["second_name"],
                patronymic=data.get("patronymic"),
                class_number=data["class_number"],
                letter=data["letter"],
                email=data.get("email")
            )
            return JsonResponse({
                "id": student.id,
                "first_name": student.first_name,
                "second_name": student.second_name,
                "patronymic": student.patronymic,
                "class_number": student.class_number,
                "letter": student.letter,
                "email": student.email
            }, status=201)
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest(f"Invalid data: {e}")
        except Exception as e:
            return HttpResponseServerError(f"Error: {e}")
        
    def put(self, request):
        return HttpResponseNotAllowed(["GET", "POST"])
    
    def delete(self, request):
        return HttpResponseNotAllowed(["GET", "POST"])


@method_decorator(csrf_exempt, name='dispatch')
class StudentDetailView(View):
    def get(self, request, id):
        try:
            student = Student.objects.values().get(id=id)
            return JsonResponse(student)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        except Exception as e:
            return HttpResponseServerError(f"Error: {e}")

    def put(self, request, id):
        try:
            data = json.loads(request.body)
            student = Student.objects.get(id=id)
            student.first_name = data.get("first_name", student.first_name)
            student.second_name = data.get("second_name", student.second_name)
            student.patronymic = data.get("patronymic", student.patronymic)
            student.class_number = data.get("class_number", student.class_number)
            student.letter = data.get("letter", student.letter)
            student.email = data.get("email", student.email)
            student.save()
            return JsonResponse({
                "id": student.id,
                "first_name": student.first_name,
                "second_name": student.second_name,
                "patronymic": student.patronymic,
                "class_number": student.class_number,
                "letter": student.letter,
                "email": student.email
            }, status=201)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
        except Exception as e:
            return HttpResponseServerError(f"Error: {e}")

    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({"deleted": True})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)
        except Exception as e:
            return HttpResponseServerError(f"Error: {e}")
    
    def post(self, request):
        return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])