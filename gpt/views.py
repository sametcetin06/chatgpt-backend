import os
import openai
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(['POST'])
@csrf_exempt
def gpttest(request):
    message = request.data.get('message')
    openai.organization = "org-eC71vQjJT5hMfOLKcvClMq0Y"
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
        ]
    )
    return Response(completion.choices[0].message)