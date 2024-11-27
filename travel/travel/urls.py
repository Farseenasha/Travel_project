"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
# FOR MEDIA FILES!!
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('',views.home,name="home"),
    path('allogin',views.allogin,name="allogin"),
    path('all_logout',views.all_logout,name="all_logout"),
    path('pswrd',views.pswrd_rqst,name="pswrd"),
    path('otpvar',views.otp,name="otpvar"),
    path('resetpswrd',views.resetpswrd,name="resetpswrd"),

    ## USER ##
    path('user_register',views.user_register,name="user_register"),
    path('user_home',views.user_home,name="user_home"),
    path('user_profile',views.user_profile,name="user_profile"),
    path('useredit_profile',views.useredit_profile,name="useredit_profile"),
    path('user_allpackage',views.user_allpackage,name="user_allpackage"),
    path('user_searchpackage',views.user_searchpackage,name="user_searchpackage"),
    path('user_packageview/<int:id>',views.user_viewpackage,name="user_packageview"),
    path('user_booking/<int:id>',views.user_booking,name="user_booking"),
    path('booking_history',views.booking_history,name="booking_history"),
    path('booking_view/<int:id>',views.booking_view,name="booking_view"),
    path('write_review/<int:id>',views.review,name="write_review"),
    path('view_review',views.view_review,name="view_review"),
    path('delete_review/<int:id>',views.delete_review,name="delete_review"),

    ## AGENCY##
    path('agency_register',views.agency_register,name="agency_register"),
    path('agency_profile',views.agency_profile,name="agency_profile"),
    path('agency_home',views.agency_home),
    path('add_package',views.add_package,name="add_package"),
    path('search_package',views.search_package,name="search_package"),
    path('all_packages',views.all_packages,name="all_packages"),
    path('package_view/<int:id>',views.package_view,name="package_view"),
    path('edit_package/<int:id>',views.edit_package,name="edit_package"),
    path('delete_package/<int:id>',views.delete_package,name="delete_package"),
    path('all_bookings',views.all_bookings,name="all_bookings"),
    path('booking_status/<int:id>',views.booking_status,name="booking_status"),
    path('booking_detail/<int:id>',views.booking_detail,name="booking_detail"),
    path('user_reviews',views.user_reviews,name="user_reviews"),

    ##ADMIN##
    path('dashboard',views.dashboard,name="dashboard"),
    path('user_list/', views.user_list, name='user_list'),
    path('user_edit/<int:id>',views.user_edit, name='user_edit'),
    path('agency_list/', views.agency_list, name='agency_list'),
    path('update_agency/<int:id>', views.update_agency_status, name='update_agency_status'),
    path('agency_document/<int:id>', views.agency_document, name='agency_document'),
    path('packages/', views.package_list, name='package_list'),
    path('package_detail/<int:id>/', views.package_detail, name='package_detail'),
    path('admndelete_package/<int:id>/', views.admndelete_package, name='admndelete_package'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
