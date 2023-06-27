from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1=Feature()
    feature1.id=1
    feature1.name='fast'
    feature1.details='our service is very quick'
    feature1.is_true=True
    
    feature2=Feature()
    feature2.id=2
    feature2.name='reliable'
    feature2.details='our service is very reliable'
    feature2.is_true=True

    feature3=Feature()
    feature3.id=3
    feature3.name='easy to use'
    feature3.details='our service is very easy to use'
    feature3.is_true=True

    feature4=Feature()
    feature4.id=4
    feature4.name='affordable'
    feature4.details='our service is very affordable'
    feature4.is_true=False



    features=[feature1,feature2,feature3,feature4]
    return render(request,'index.html',{'features': features })

def counter(request):
    text= request.POST['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})
    



