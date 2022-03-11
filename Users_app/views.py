from django.shortcuts import get_object_or_404, render
from .forms import Sign_In_Form, Sign_Up_Form, Profile_Update_Form, Password_Change_Form, Hostel_Search_Form, ContactUs_Form
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import redirect
from .models import ContactUs
from Hostels_app.models import HostelReview, Hostel, Wishlist, Hostel_images

def index(request):

    properties = Hostel.objects.all()[:8]
    wishlist = None
    wishlist_img = [] 
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist = wishlist.hostels.all()
        
        for wish_hostel in wishlist:
            image = Hostel_images.objects.filter(hostel=wish_hostel)
            wishlist_img.append(image[0])

    sign_up_form = Sign_Up_Form(request.POST or None)
    sign_in_form = Sign_In_Form(request.POST or None)
    hostel_search_form = Hostel_Search_Form(request.POST or None)
    if request.method == 'POST':
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data.get('username')
            password = sign_in_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('user-account-info-page')
        if sign_up_form.is_valid():
            sign_up_form.save()
            user = authenticate(username=sign_up_form.cleaned_data.get('username'), password=sign_up_form.cleaned_data.get('password1'))
            Wishlist.objects.create(user=user)
            login(request, user)
            return redirect('user-account-info-page')
    context = {'sign_up_form':sign_up_form, 'sign_in_form':sign_in_form, "hostel_search_form":hostel_search_form, 'wishlist':wishlist, 'wishlist_img':wishlist_img, 'properties':properties}
    return render(request, 'index.html', context)

def user_account_info(request):
    profile_update_form = Profile_Update_Form(instance=request.user)
    if request.method == 'POST':
        form = Profile_Update_Form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-account-info-page')
    context = {'profile_update_form':profile_update_form}
    return render(request, 'user-account-info.html', context)

def user_account_security(request):
    password_change_form = Password_Change_Form(user=request.user, data=request.POST)
    if password_change_form.is_valid():
        password_change_form.save()
        update_session_auth_hash(request, password_change_form.user)
        return redirect('user-account-security-page')
    context = {'password_change_form':password_change_form}
    return render(request, 'user-account-security.html', context)

def user_account_wishlist(request):
    wishlist_img = [] 
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist = wishlist.hostels.all()
        
    for wish_hostel in wishlist:
        image = Hostel_images.objects.filter(hostel=wish_hostel)
        wishlist_img.append(image[0])

    context = {"wishlist":zip(wishlist, wishlist_img)}
    return render(request, 'user-account-wishlist.html', context)

def user_account_reviews(request):
    properties = Hostel.objects.filter(owner=request.user)
    reviews_by_you = HostelReview.objects.filter(user=request.user)
    reviews_about_you = []

    for property in properties:
        temp = HostelReview.objects.filter(hostel=property)
        for i in temp:
            reviews_about_you.append(i)
    context = {'reviews_about_you':reviews_about_you, 'reviews_by_you':reviews_by_you}
    return render(request, 'user-account-reviews.html', context)
    
def about_us(request):
    sign_up_form = Sign_Up_Form(request.POST or None)
    sign_in_form = Sign_In_Form(request.POST or None)
    if request.method == 'POST':
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data.get('username')
            password = sign_in_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('user-account-info-page')
        if sign_up_form.is_valid():
            sign_up_form.save()
            user = authenticate(username=sign_up_form.cleaned_data.get('username'), password=sign_up_form.cleaned_data.get('password1'))
            Wishlist.objects.create(user=user)
            login(request, user)
            return redirect('user-account-info-page')
    context = {'sign_up_form':sign_up_form, 'sign_in_form':sign_in_form}
    return render(request, 'about-us.html', context)

def contact_us(request):
    sign_up_form = Sign_Up_Form(request.POST or None)
    sign_in_form = Sign_In_Form(request.POST or None)
    contact_us_form = ContactUs_Form(request.POST or None)
    if request.method == 'POST':
        if contact_us_form.is_valid():
            contact_us_form.save()
            return redirect('contact-us-done-page')
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data.get('username')
            password = sign_in_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('user-account-info-page')
        if sign_up_form.is_valid():
            sign_up_form.save()
            user = authenticate(username=sign_up_form.cleaned_data.get('username'), password=sign_up_form.cleaned_data.get('password1'))
            Wishlist.objects.create(user=user)
            login(request, user)
            return redirect('user-account-info-page')
    context = {'contact_us_form':contact_us_form, 'sign_up_form':sign_up_form, 'sign_in_form':sign_in_form}
    return render(request, 'contact-us.html', context)

def contact_us_done(request):
    return render(request, 'contact-us-done.html')

def help_center(request):
    sign_up_form = Sign_Up_Form(request.POST or None)
    sign_in_form = Sign_In_Form(request.POST or None)
    if request.method == 'POST':
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data.get('username')
            password = sign_in_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('user-account-info-page')
        if sign_up_form.is_valid():
            sign_up_form.save()
            user = authenticate(username=sign_up_form.cleaned_data.get('username'), password=sign_up_form.cleaned_data.get('password1'))
            Wishlist.objects.create(user=user)
            login(request, user)
            return redirect('user-account-info-page')
    context = {'sign_up_form':sign_up_form, 'sign_in_form':sign_in_form}
    return render(request, 'help-center.html', context)


def sign_out(request):
    logout(request)
    return redirect('index-page')