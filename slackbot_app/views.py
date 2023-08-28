from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class SlackEndpoint(View):
    def post(self, request, *args, **kwargs):
        # Here, you can process the Slack POST request
        # For now, let's just send a simple JSON response
        return JsonResponse({"message": "Received"})

    def get(self, request, *args, **kwargs):
        # Optional: Handle GET requests if needed
        return JsonResponse({"message": "Hello, Slack!"})
