from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Users_app.forms import Create_Hostel_Form, Hostel_Image_Form, Hostel_Review_Form, Sign_In_Form, Sign_Up_Form, Hostel_Filter_Form
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Hostel, Hostel_images, HostelReview, Wishlist
from .analysis import calculate_sentiment
from .filters import HostelFilter


from sklearn.metrics.pairwise import euclidean_distances
import pandas
import numpy
import sqlite3
import os

def main(request):
    cnx = sqlite3.connect('C:\\Users\\hp\\Desktop\\Home_Again_Project\\db.sqlite3')
    data = pandas.read_sql_query("select * from Hostels_app_hostel", cnx)
    
    newdata = data
    newdata["boys"]=newdata['category'].astype(str).apply(lambda x:True if x=='boys' else (True if x=='C' else False))
    newdata["girls"]=newdata['category'].astype(str).apply(lambda x:True if x=='girls' else (True if x=='C' else False))
    result=data[data[request.GET.get('category')]]
    result.reset_index(drop=True, inplace=True)
    college = get_object_or_404(Hostel, id=request.GET.get('institute'))
    ans=result.index[result['title']==college.title]
    newresult=result.filter(['lat','log'])
    dis=euclidean_distances(newresult)
    final_data=dis[ans[0]]
    disdf=pandas.DataFrame(dis)
    value=disdf.iloc[ans[0]].values
    sortedvalue=numpy.argsort(value)
    hostels = []
    for i in range(1,40):
        try:
            if((result['title'][sortedvalue[i]]!="KHAN STUDY GROUP(KSG),111-117,Veda Building, Bhanwarkua Square, near Apple Hospital, Indore, Madhya Pradesh 452001")and(result['title'][sortedvalue[i]]!="Acropolis Institute Of Technology And Research - AITR, Square, Malwa County, Manglaya Sadak, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Arihant College, Khandwa Road, opp. Radha Swami Satsang, Near DAVV Takshila Parisar, Opposite Radha Swami Satsang, Rani Bagh Main, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Government Holkar Science College Indore, AB Road, near Bhawarkua, Square, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Indore Institute of Law, opp. IIM, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Institute of Engineering & Technology, Davv Takshila Parisar, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="IPS Academy Institute of Business Management and Research,Knowledge Village, Rajendra Nagar , A.B Road, Indore, Madhya Pradesh 452012")and(result['title'][sortedvalue[i]]!="Kautilya Academy, Payal Plaza, Bhawarkua Main Rd, opp. Bhawarkuan Police Station, Bhavarkuan Square, Aditya Nagar, Bhanwar Kuwa, Indore, Madhya Pradesh 452001")and(result['title'][sortedvalue[i]]!="Mahatma Gandhi Institute for Civil Services,G-13, Ground Floor Veda Business Park, Bhanvarkuan Square, near Apple Hospital, Indore, Madhya Pradesh 452001")and(result['title'][sortedvalue[i]]!="Ocean academy Indore, 56, Bhawarkua Main Rd, near Siddharth Nagar, Vishnu Puri Colony, Indore, Madhya Pradesh 452001")and(result['title'][sortedvalue[i]]!="Oriental University, Sanwer Rd, opposite Revati Range, Jakhya, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Prestige Institute of Engineering Management & Research, Sector-D, Scheme No 74, Vijay Nagar, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Radiant Institute of Management and Science,SECTOR A BAKHTAWAR RAM NAGAR, near Tilak Nagar, Indore, Madhya Pradesh 452001")and(result['title'][sortedvalue[i]]!="Renaissance College of Commerce & Management, behind Press Complex, Sunil Nagar, Krishna Bagh Colony, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="SAGE University, Bypass Road, Kailod Kartal, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Sgsits Main Gate, SGSITS Road, Shivaji Nagar, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Shri Atal Bihari Vajpayee Government Arts And Commerce College, AB Road, Navlakha, Davv Takshila Parisar, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Shri Vaishnav Institute of Management, Indore, Sector B, Gumasta Nagar, Scheme 71, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="St. Paul Institute of Professional Studies Indore, Lalaram Nagar, Indore, Madhya Pradesh")and(result['title'][sortedvalue[i]]!="Devi Ahilya Vishwavidyalaya Takshila Campus, Khandwa Road, Indrapuri Colony, Indra Puri Colony, Indore, Madhya Pradesh")):
                hostels.append(result['id'][sortedvalue[i]])
                # print(result['title'][sortedvalue[i]])
        except:
            pass
    else:
        return hostels

    

def add_hostel(request):
    create_hostel_form = Create_Hostel_Form()
    hostel_image_form = Hostel_Image_Form()
    if request.method == 'POST':
        create_hostel_form = Create_Hostel_Form(request.POST)
        imageform = Hostel_Image_Form(request.POST, request.FILES)
        if create_hostel_form.is_valid() and imageform.is_valid():
            hostel_form = create_hostel_form.save(commit=False)
            hostel_form.owner = request.user
            hostel_form.save()
            images = request.FILES.getlist('image')
            for img in images:
                photo = Hostel_images.objects.create(hostel = hostel_form,image = img)
                photo.save()
            return redirect('hostel-promotion-page')

    context = {"create_hostel_form":create_hostel_form, 'hostel_image_form':hostel_image_form}
    return render(request, 'add-property.html', context)

def edit_hostel(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    create_hostel_form = Create_Hostel_Form(instance=hostel)
    hostel_image_form = Hostel_Image_Form()
    if request.method == 'POST':
        create_hostel_form = Create_Hostel_Form(request.POST, instance=hostel)
        # hostel_image_form = Hostel_Image_Form()
        if create_hostel_form.is_valid():
            create_hostel_form.save()
            return redirect('vendor-account-properties-page')
    context = {"create_hostel_form":create_hostel_form, 'hostel_image_form':hostel_image_form}
    return render(request, 'edit-property.html', context)

def delete_hostel(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    hostel.delete()
    return redirect('vendor-account-properties-page')

def activate_deactivate_hostel(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    if hostel.vacant:
        hostel.vacant = False
    else:
        hostel.vacant = True
    hostel.save()
    return redirect('vendor-account-properties-page')

def hostel_promotion(request):
    return render(request, 'hostel-promotion.html')

def vendor_account_properties(request):
    properties = Hostel.objects.filter(owner=request.user)
    images = []
    for hostel in properties:
        image = Hostel_images.objects.filter(hostel=hostel)
        images.append(image[0])
    context = {'properties':zip(properties,images)}
    return render(request, 'vendor-account-properties.html', context)

def hostels_catalog(request):
    p = main(request)
    properties_list = Hostel.objects.filter(id__in=p).order_by('-sentiment')
    if request.GET.get('air_conditioning')=='on':
        properties_list.filter(air_conditioning=True)

    filter_form = Hostel_Filter_Form()

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
    context = {'properties':properties_list, 'filter_form':filter_form, 'sign_up_form':sign_up_form, 'sign_in_form':sign_in_form}
    return render(request, 'hostels-catalog.html', context)

def hostel_single_view(request, pk):
    property = get_object_or_404(Hostel, pk=pk)
    images = Hostel_images.objects.filter(hostel=property)
    reviews = HostelReview.objects.filter(hostel=property).order_by('-timestamp')
    hostel_review_form = Hostel_Review_Form()
    sign_up_form = Sign_Up_Form(request.POST or None)
    sign_in_form = Sign_In_Form(request.POST or None)
    if request.method == 'POST':
        form = Hostel_Review_Form(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.user = request.user
            temp_form.hostel = property
            temp_form.save()
            calculate_sentiment(property, reviews)
            return redirect('hostel-single-view', pk=pk)
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
    context = {'property':property, 'images':images, 'hostel_review_form':hostel_review_form, 'reviews':reviews, 'sign_up_form':sign_up_form, 'sign_in_form':sign_in_form}
    return render(request, 'hostel-single-view.html', context)

def add_hostel_wishlist(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    temp, _ = Wishlist.objects.get_or_create(user=request.user)
    temp.hostels.add(hostel)
    return redirect('hostel-single-view', pk=pk)

def remove_hostel_wishlist(request, pk):
    hostel = get_object_or_404(Hostel, pk=pk)
    temp, _ = Wishlist.objects.get_or_create(user=request.user)
    temp.hostels.remove(hostel)
    return redirect('user-account-wishlist-page')
