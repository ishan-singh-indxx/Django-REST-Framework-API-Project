from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hello World, this is your Django API Response!"})
