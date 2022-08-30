from http.client import NOT_FOUND, HTTPResponse
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.shortner import create_url
from .models import urlShortener
from .serializers import urlShortenerSerializer


@api_view(['POST'])
def getclicks(request):
    shorturl = request.data['shorturl'].split(r"/")[-1]
    obj = urlShortener.objects.get(shorturl=shorturl)
    obj.clicks +=1
    obj.save()
    return Response({"clicks":obj.clicks})

@api_view(['GET'])
def summary(request):
    obj = urlShortener.objects.all()
    return Response(urlShortenerSerializer(obj, many=True).data)
@api_view(['POST'])
def makeshorturl(request):
    data = request.data
    shorturl = create_url(data['longurl'])
    urlShortener.objects.create(
        longurl=data['longurl'],
        shorturl=shorturl
    )
    longurl = data['longurl']
    shorturl = f"{request.get_host()}/{shorturl}"
    return Response({'longurl': longurl, 'shorturl': shorturl, 'clicks':0})


def redirectUrl(request, shorturl):
    try:
        obj = urlShortener.objects.get(shorturl=shorturl)
        obj.clicks +=1
        obj.save()
        return HttpResponseRedirect(obj.longurl)
    except urlShortener.DoesNotExist:
        return Response("error")
