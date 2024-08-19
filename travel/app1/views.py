from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import All_login , Customer,Agency,Packages,Booking,Reviews
from django.contrib.auth.models import User,auth

# Create your views here.


def home(request):
    return render(request,'home.html')

def allogin(request):
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']
        admin_user = auth.authenticate(request,username=Username,password=Password)
        if admin_user is not None and admin_user.is_staff:
            auth.login(request,admin_user)
            return redirect(agency_view)
            # return HttpResponse("admin loged in") 
        data = auth.authenticate(username=Username,password=Password)
        if data is not None:
            auth.login(request,data)
            if data.user_type == "customer" :
                # return HttpResponse("customer loged in")
                return redirect(user_home)
            if data.user_type == "agency" and data.status == "pending":
                return HttpResponse("Can't login without approval of admin.Either wait for 1 day or register again")
            if data.user_type == "agency" and data.status == "accept":
                return redirect(agency_home)
        else:
            return HttpResponse("incorrect credentials")
    else:
        return render(request,'allogin.html') 

def all_logout(request):
    auth.logout(request)
    return redirect(allogin)

      ### AGENCY ###
def agency_register(request):
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Number = request.POST["phone"]
        Image = request.FILES['image']
        Document = request.FILES['document']
        Username = request.POST['username']
        if All_login.objects.filter(username=Username).exists():
            return render(request,'agency/agency_register.html',{'warning':"username already exists"})
        Password = request.POST['password']
        data = All_login.objects.create_user(username=Username,password=Password,user_type="agency")
        data.save()
        datas = All_login.objects.get(id=data.id)
        agency = Agency.objects.create(login_id=datas,name=Name,image=Image,
                                         document=Document,
                                         phone=Number,email=Email)
        agency.save()
        return redirect(allogin)
    else:
        return render(request,'agency/agency_register.html') 

def agency_home(request):
    data = Agency.objects.get(login_id=request.user.id)
    return render(request,'agency/agency_home.html',{'data':data})

def agency_profile(request):
    data = Agency.objects.get(login_id=request.user.id)  
    return render(request,'agency/agency_profile.html',{'data':data})

def add_package(request):
    if request.method == "POST":
       Package_name = request.POST["package_name"]
       Place = request.POST["place"]
       Start_place = request.POST["start_place"]
       End_place = request.POST["end_place"]
       About =  request.POST["about"]
       Description = request.POST["description"]
       Days = request.POST["days"]
       Price_adult = int(request.POST["price_adult"])
       Price_children = int(request.POST["price_children"])
       Image1 = request.FILES["image1"]
       Image2 = request.FILES["image2"]
       Image3 = request.FILES["image3"]
       Image4 = request.FILES["image4"]
       agency = Agency.objects.get(login_id=request.user.id)   
       data = Packages.objects.create(agency_id=agency,package_name=Package_name,place=Place,start_place=Start_place,
                                      end_place=End_place,about=About,description=Description,days=Days,price_adult=Price_adult,
                                      price_children=Price_children,image1=Image1,image2=Image2,image3=Image3,image4=Image4)
       data.save()
       return redirect(all_packages)
    else:
        return render(request,'agency/add_package.html')
    
def all_packages(request):
    data = Agency.objects.get(login_id=request.user.id)
    package = Packages.objects.filter(agency_id=data)
    return render(request,'agency/all_packages.html',{'data':package,'agency':data})

def package_view(request,id):
    data = Agency.objects.get(login_id=request.user.id)
    package = Packages.objects.get(id=id)
    return render(request,'agency/package_view.html',{'data':package})

def edit_package(request,id):
    data = Agency.objects.get(login_id=request.user.id)
    package = Packages.objects.get(id=id)
    if request.method == "POST":
        package.package_name = request.POST['package_name']
        package.start_place =  request.POST['start_place']
        package.end_place =  request.POST['end_place']
        package.about =  request.POST['about']
        package.days =  request.POST['days']
        package.price_adult =  int(request.POST['price_adult'])
        package.price_children =  int(request.POST['price_children'])
        if 'image1' in request.FILES:
            package.image1 =  request.FILES['image1']
        if 'image2' in request.FILES:
            package.image2 =  request.FILES['image2']
        if 'image3' in request.FILES:
            package.image3 =  request.FILES['image3']
        if 'image4' in request.FILES:
            package.image4 =  request.FILES['image4']     
        package.save()
        return redirect(all_packages)
    else:
        return render(request,'agency/edit_package.html',{'package':package})
    
def delete_package(request,id):
    data = Agency.objects.get(login_id=request.user.id)
    package = Packages.objects.get(id=id)
    package.delete()
    return redirect(all_packages)

def all_bookings(request):
    data = Agency.objects.get(login_id=request.user.id)
    booking = Booking.objects.filter(package_id__agency_id=data)
    return render(request,'agency/all_bookings.html',{'booking':booking})

def booking_status(request,id):
    data = Agency.objects.get(login_id=request.user.id)
    booking = Booking.objects.get(id=id)
    try:
        if request.method == "POST":
            booking_status = request.POST['status']
            if booking_status == "accept":
                booking.status = booking_status
                booking.save()
                return HttpResponse("booking accepted")
            if booking_status == "reject":
                booking.status = booking_status
                booking.save()
                return HttpResponse("booking rejected")
    except Exception as e:
        return HttpResponse({e})
        
    else:
        return redirect(all_bookings)

def booking_detail(request,id):
    data = Agency.objects.get(login_id=request.user.id)
    booking = Booking.objects.get(id=id)
    return render(request,'agency/booking_detail.html',{'data':booking})

def user_reviews(request):
    data = Agency.objects.get(login_id=request.user.id)
    review = Reviews.objects.filter(package_id__agency_id=data)
    return render(request,'agency/user_reviews.html',{'review':review})
            
     

      ### USER ###
def user_register(request):
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Address = request.POST["address"]
        Number = request.POST["phone"]
        Date = request.POST["dob"]
        Image = request.FILES["image"]
        Username = request.POST['username']
        if All_login.objects.filter(username=Username).exists():
            return render(request,'user/user_register.html',{'warning':"username already exists"})
        Password = request.POST['password']
        data = All_login.objects.create_user(username=Username,password=Password,user_type="customer")
        data.save()
        datas = All_login.objects.get(id=data.id)
        User = Customer.objects.create(login_id=datas,name=Name,image=Image,
                                           dob=Date,
                                           phone=Number,email=Email,address=Address)
        User.save()
        return redirect(allogin)
        
    else:
        return render(request,'user/user_register.html')
           

def user_home(request):
    data = Customer.objects.get(login_id=request.user.id)
    return render(request,'user/user_home.html',{'data':data})            

def user_profile(request):
    data = Customer.objects.get(login_id=request.user.id)  
    return render(request,'user/user_profile.html',{'data':data})

def useredit_profile(request):
    data = Customer.objects.get(login_id=request.user.id)
    if request.method == "POST":
        data.name = request.POST['name']
        data.email =  request.POST['email']
        data.address =  request.POST['address']
        data.phone =  request.POST['phone']
        if 'image' in request.FILES:
            data.image =  request.FILES['image']
        data.save()
        return redirect(user_profile)
    else:
        return render(request,'user/useredit_profile.html',{'data':data}) 

def user_allpackage(request):
    data = Packages.objects.all()
    return render(request,'user/user_allpackage.html',{'data':data})

def user_viewpackage(request,id):
    data = Packages.objects.get(id=id)
    return render(request,'user/user_packageview.html',{'data':data})

def user_booking(request,id):
    user = Customer.objects.get(login_id=request.user.id)
    package = Packages.objects.get(id=id)
    if request.method == "POST":
        adult = int(request.POST['adult'])
        children = int(request.POST['children'])
        date = request.POST['date']
        total_people = adult + children
        total_amount = (adult * package.price_adult) + (children * package.price_children)
        User_booking = Booking.objects.create(user_id=user,package_id=package,booking_amount=total_amount,
                                              booking_day=date,total_no=total_people)
        User_booking.save()
        return redirect(user_home)
    else:
        return render(request,'user/user_booking.html',{'data':user, 'package':package})

def booking_history(request):
    booking = Booking.objects.all()
    return render(request,'user/booking_history.html',{'booking':booking})

def booking_view(request,id):
    data = Booking.objects.get(id=id)
    return render(request,'user/booking_view.html',{'data':data})

def review(request,id):
    user = Customer.objects.get(login_id=request.user.id)
    package = Packages.objects.get(id=id)
    if request.method == "POST":
        rate = request.POST['rating']
        details = request.POST['description']
        review = Reviews.objects.create(user_id=user,package_id=package,rating=rate,description=details)
        review.save()
        return redirect(user_home)
    else:
        return render(request,'user/write_review.html',{'package':package})
    
def view_review(request):
    review = Reviews.objects.all()
    return render(request,'user/view_review.html',{'review':review})

def delete_review(request,id):
    data = Customer.objects.get(login_id=request.user.id)
    review = Reviews.objects.get(id=id)
    review.delete()
    return redirect(user_home)   


## ADMIN ##

def agency_view(request):
    agency = Agency.objects.filter(login_id__status="pending")
    print(agency)
    return render(request,'admin/agency_status.html',{'agency':agency})


def agency_status(request,id):
    agency = Agency.objects.get(id=id) 
    logdata = All_login.objects.get(id=agency.login_id.id)
    try:
        if request.method == "POST":
            agency_status = request.POST['status']
            if agency_status == "accept":
                logdata.status = agency_status
                logdata.save()
                return redirect(agency_view)
            if agency_status == "reject":
                logdata.status = agency_status
                logdata.save()
                return redirect(agency_view)
    except Exception as e:
        return HttpResponse({e})
        
    else:
        return redirect(agency_view)
    
# def all_agencies(request):
