from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from .models import product,blog
from .forms import students_details
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages


def home(request):
    return render(request,'product/home.html')
@login_required
def main(request):
    return render(request,'product/main.html')

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST['age'] and request.POST['qualification'] and request.POST['country'] and request.POST['phone_no']:
            products=blog()
            products.name=request.POST['name']
            products.age=request.POST['age']
            products.qualification=request.POST['qualification']
            products.country=request.POST['country']
            products.phone_no=request.POST['phone_no']
            products.save()
            return render(request,'product/create.html',{'error':"Details submitted"})     
        else:
            return render(request,'product/create.html',{'error':"fill all fields"}) 
    else:
        return render(request,'product/create.html') 

@login_required
def enquiry(request):
    prdct=blog.objects
    return render(request,'product/enquiry.html',{'prdct':prdct})
@login_required
def applied(request):
    return render(request,'product/applied.html')

@login_required
def detail(request,pk):
    prdct=blog.objects.get(pk=pk)
    context={
        'prdct':prdct
    }
    return render(request,'product/detail.html',context)

@login_required
def registering(request):
    return render(request,'product/registering.html')

@login_required
def delete(request,pk):
    prdct=blog.objects.get(pk=pk)
    prdct.delete()
    prdct=blog.objects
    return redirect('enquiry')

@login_required
def modify(request,pk):
    prdct=blog.objects.get(pk=pk)
    if request.method=='POST':
        if request.POST['name'] and request.POST['age'] and request.POST['qualification'] and request.POST['country'] and request.POST['phone_no']:
            prdct.name=request.POST['name']
            prdct.age=request.POST['age']
            prdct.qualification=request.POST['qualification']
            prdct.country=request.POST['country']
            prdct.phone_no=request.POST['phone_no']
            prdct.save()
            return redirect('enquiry')
        else:
            return render(request,'product/detail.html',{'error':"fill all fields"}) 
    else:
        return render(request,'product/detail.html') 

def search(request):
    if request.method=="POST":
        srch=request.POST['srh'] 
        if srch:
            match=blog.objects.filter(Q(name__icontains=srch) | Q(country__icontains=srch))
            if match:
                return render(request,'product/enquiry.html',{'sr':match})
            else:
                messages.error(request,'No Result Found')
        else:
            return redirect('enquiry')
    return render(request,'product/enquiry.html')
@login_required
def prac(request):
    return render(request,'product/prac.html')


def apply(request):
    return render(request,'product/apply.html')

def study(request):
    return render(request,'product/study.html')

def working(request):
    return render(request,'product/working.html')

def tourist(request):
    return render(request,'product/tourist.html')