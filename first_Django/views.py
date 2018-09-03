from django.http import HttpResponse
from django.shortcuts import render
import requests
def home(request):
    return render(request, 'index.html')
def count(request):
    # score = SnowNLP(request.GET['text']).sentiments
    # print(score)
    api_key = "6ebf3bacd3e247cf8c1f358d243bc260"
    api_url = "http://www.tuling123.com/openapi/api"
    msg = request.GET['text']
    print(msg)
    msg = {
        "key": api_key,
        "info": msg
    }
    response = requests.post(url=api_url, json=msg)
    data = response.json()
    print(data)
    text1 = data['text']
    # print(text1)
    return render(request, 'count.html',{ 'content':text1})

def about(request):
    return render(request, 'about.html')