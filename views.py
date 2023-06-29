from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features= Feature.objects.all()
    return render(request,'index.html',{'features': features })

def counter(request):
    text= request.POST['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']   #whatever we are input-ing in the username textfield it is all getting stored in the variable username
        email = request.POST['email']
        password = request.POST['Password']
        password2 = request.POST['Password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
            elif User.object.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user = User.object.create_user(username= username, email= email, password= password)
                user.save;
                return redirect('login')
        else:
            messages.info(request,'Password not same')
            return redirect('register')
    else:
        return render(request,'register.html')




