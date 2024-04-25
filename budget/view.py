from django.http import HttpRequest
from django.http.response import JsonResponse

def health(request: HttpRequest) -> HttpRequest:
    return JsonResponse({"satus": "OK"})