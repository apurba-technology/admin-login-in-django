from django.shortcuts import render,redirect
from django.http import HttpResponse
from Next_app.functions.functions import handle_uploaded_file
from Next_app.forms import *


# Create your views here.
def index(request):
    if request.method == 'GET':
        Banners = Banner.objects.all() 
        Notices = Notice.objects.all()
        prog = Programme.objects.all()  
        return render(request, 'index.html', {'Note' : Notices, 'banner_images' : Banners, 'pro' : prog})
    
         
        

def admin(request):
    return render(request, 'admin.html')

def banner_upload(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('display_images')
    else:
        form = BannerForm()
    return render(request,'banner_upload.html',{'form': form})

def display_images(request): 
  
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'display_banner_images.html',{'banner_images' : Banners})

def delete(request, id):
    Banners = Banner.objects.get(id=id)
    Banners.delete()
    return redirect("display_images")

def delet(request, id):
    Notices = Notice.objects.get(id=id)
    Notices.delete()
    return redirect("display_notice")

def notice_upload(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
    else:
        form = NoticeForm()
    return render(request,'notice_up.html',{'form': form})


def disNo(request): 
  
    if request.method == 'GET':
        Notices = Notice.objects.all()  
        return render(request, 'disn.html',{'Note' : Notices})

def programme_upload(request):
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse('<center><h1> Upload successful<br><a href="admin">Back menu</a> </h1></center>')
    else:
        form = ProgrammeForm()
    return render(request,'pro.html',{'form': form})
    
def admin_regestion(request):
	error=True
	if request.method=='POST':
		b=admin_regestion_meForm(request.POST)
		bb=admin_regestion_me()
		bb.name=request.POST['name']
		bb.e_mail=request.POST['e_mail']
		bb.password=request.POST['password']
		bb.password1=request.POST['password1']
		if bb.password == bb.password1:
			error = False
			bb.password=request.POST['password']
			bb.save()
			return redirect("log")
		else:
			b=admin_regestion_meForm()
			return render(request,"admin_reg.html",{'form':b})				
	else:
		b=admin_regestion_meForm()
		return render(request,"admin_reg.html",{'form':b})


def log_in(request):
	if request.method=='POST':
		e_mail=request.POST['e_mail']
		password=request.POST['password']
		row=admin_regestion_me.objects.raw("select id,e_mail,password from Admin_Regestion where e_mail='"+str(e_mail)+"' and password='"+str(password)+"'")
		#return HttpResponse(row)
		if(row):
			return redirect("admin")
		else:
			return render(request, "admin_login.html")
            #return HttpResponse("Not Ok")


	else:
		return render(request,"admin_login.html")
		#return HttpResponse("Password is Worng")
