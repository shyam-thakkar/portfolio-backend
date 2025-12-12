from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        msg = data.get("query", "")
        return JsonResponse({"response": f"You said: {msg}"})
    return JsonResponse({"error": "Only POST allowed"}, status=405)
