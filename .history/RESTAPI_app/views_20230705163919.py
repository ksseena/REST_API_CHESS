from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from RESTAPI_app.models import Snippet
from RESTAPI_app.serializers import SnippetSerializer

# Create your views here.
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets=Snippet.objects.all()
        serializer =SnippetSerializer(snippets,many=True)
    return 