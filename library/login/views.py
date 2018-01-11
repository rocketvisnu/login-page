from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate
from .models import Book
def login_page(request):
	if request.method== 'POST':
		user = request.POST.get("username")
		passw = request.POST.get("password")
		#print (user,passw)
		user = authenticate(username=user, password=passw)
		#print (user)
		if user is not None:
			return MyView(request)
		else:
			return HttpResponse("<br><br><br><br><br><center><h1>Not Valid</h1></center>")
	return render(request,"login.html")
	

def MyView(request):
	book = Book.objects.all()
	return render(request,"book_details.html",{'book':book})