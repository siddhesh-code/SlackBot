from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from slackbot_app.models import Article 

@method_decorator(csrf_exempt, name='dispatch')
class SlackEndpoint(View):
    def post(self, request, *args, **kwargs):
        
        return JsonResponse({"message": "Received"})

    def get(self, request, *args, **kwargs):
        # Optional: Handle GET requests if needed
        return JsonResponse({"message": "Hello, Slack!"})

class SlackAsk(View):
    def post(self, request, *args, **kwargs):
        Article.post_message_to_slack('#general', "What is Indian population?")
        return JsonResponse({"message": "Hello, Received!"})
    
    def get(self, request, *args, **kwargs):
        
        gpt_response = Article.get_gpt_response('Translate the following English text to Hindi: "Hello"')
        Article.post_message_to_slack('#general', gpt_response)
        return JsonResponse({"message": "Hello, Slack!"})

