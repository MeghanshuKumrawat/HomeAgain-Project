from dataclasses import field, fields
from email import message
import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import CustomUser, institute_choice, ContactUs
from Hostels_app.models import Hostel, Hostel_images, HostelReview
import random, string

def rand_slug():
    slug = ''
    for _ in range(3):
        for i in range(5):
            char = random.choice(string.ascii_letters + string.digits) 
            slug += ''.join(char)
        if _ == 2:
            continue
        slug += '-'
    return slug

class Sign_Up_Form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your email'}))
    user_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control form-control-lg'}), choices=(('HO', 'Hostel Owner'), ('HS', 'Hostel Seeker')))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm your password'}))
    terms = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"form-check-input", "type":"checkbox", "id":"agree-to-terms"}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'password1', 'password2', 'terms']

    def save(self, commmit=True):
        user = super(Sign_Up_Form, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.slug = rand_slug()
        if commmit:
            user.save()
        return user

class Sign_In_Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Password'}))

class Profile_Update_Form(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'First name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Last name'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'you@yoursite.com'}))
    phone_no = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'9258454845'}), required=False)
    institute = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control form-control-lg', 'placeholder':'Express yourself'}), choices=institute_choice, required=False)
    profile = forms.ImageField(widget=forms.FileInput(attrs={"class":"btn btn-primary px-3 px-sm-4"}), required=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_no', 'institute', 'profile']

class Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Current password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'New password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Verify password'}))


class Create_Hostel_Form(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Title for your Hostel'}))
    category = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class":"form-select", "id":"ap-category"}), choices=(('M', 'Male'), ('F', 'Female'), ('C', 'CoEd')))
    type = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={"class":"form-check-input", "id":"ap-company"}), choices=(('RB', 'I am a registered business'), ('PB', 'I am a private seller')), initial="RB")
    state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'State name'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'City name'}))
    pin_code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Pin code'}))
    street_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Street address'}))
    one_seater_room = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control w-100 me-2 mb-2', 'placeholder':'Total rooms'}))
    one_seater_price = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control w-100 me-2 mb-2', 'placeholder':'Price / Room'}))
    two_seater_room = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control w-100 me-2 mb-2', 'placeholder':'Total rooms'}))
    two_seater_price = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control w-100 me-2 mb-2', 'placeholder':'Price / Room'}))
    three_seater_room = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control w-100 me-2 mb-2', 'placeholder':'Total rooms'}))
    three_seater_price = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control w-100 me-2 mb-2', 'placeholder':'Price / Room'}))
    attached_bathrooms = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"attached-bathrooms"}))
    parking = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"parking"}))
    wifi = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"wifi"}))
    gym = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"gym"}))
    laundry = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"laundry"}))
    pets_friendly = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"pets-friendly"}))
    tv = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"tv"}))
    air_conditioning = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"air-condition"}))
    balcony = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"balcony"}))
    water_heating = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"water-heating"}))
    linens = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"linens"}))
    iron = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"iron"}))
    kitchen = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"kitchen"}))
    watercooler = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"water-cooler"}))
    security_cameras = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"security-cameras"}))
    mess = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"mess"}))
    total_area = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Total area'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control form-control-lg', 'placeholder':'Describe your hostel', 'rows':5}))
    
    class Meta:
        model = Hostel
        fields = ["title","category","type","state","city","pin_code","street_address","one_seater_room","one_seater_price","two_seater_room","two_seater_price","three_seater_room","three_seater_price","attached_bathrooms","parking","wifi","gym","laundry","pets_friendly","tv","air_conditioning","balcony","water_heating","linens","iron","kitchen","watercooler","security_cameras","mess","description","total_area"]


class Hostel_Filter_Form(forms.ModelForm):
    category = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class":"form-select", "id":"ap-category"}), choices=(('boys', 'Boys'), ('girls', 'Girls'), ('C', 'CoEd')))
    attached_bathrooms = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"attached-bathrooms"}))
    parking = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"parking"}))
    wifi = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"wifi"}))
    gym = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"gym"}))
    laundry = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"laundry"}))
    pets_friendly = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"pets-friendly"}))
    tv = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"tv"}))
    air_conditioning = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"air-condition"}))
    balcony = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"balcony"}))
    water_heating = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"water-heating"}))
    linens = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"linens"}))
    iron = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"iron"}))
    kitchen = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"kitchen"}))
    watercooler = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"water-cooler"}))
    security_cameras = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"security-cameras"}))
    mess = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"mess"}))
    verified = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input", "id":"mess"}))
    class Meta:
        model = Hostel
        fields = ['category','attached_bathrooms','parking','wifi','gym','laundry','pets_friendly','tv','air_conditioning','balcony','water_heating','linens','iron','kitchen','watercooler','security_cameras','mess','verified']

class Hostel_Image_Form(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'multiple':True}), required=False)
    class Meta:
        model = Hostel_images
        fields = ['image']

class Hostel_Review_Form(forms.ModelForm):
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control form-control-lg', 'placeholder':'Your review message', 'rows':4}))
    locality_rate = forms.ChoiceField(widget=forms.RadioSelect(attrs={}), choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    food_rate = forms.ChoiceField(widget=forms.RadioSelect(attrs={}), choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    hostel_rate = forms.ChoiceField(widget=forms.RadioSelect(attrs={}), choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    class Meta:
        model = HostelReview
        fields = ['comment', 'locality_rate', 'food_rate', 'hostel_rate']

class Hostel_Search_Form(forms.Form):
    institute = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control text-muted'}), queryset=Hostel.objects.filter(category='C'))
    category = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control text-muted'}), choices=(('', 'Select hostel type.....'),('boys', 'For Boys'), ('girls', 'For Girls')))

class ContactUs_Form(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'you@yoursite.com'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control form-control-lg', 'placeholder':'Leave your message', 'rows':4}))
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':'you@yoursite.com'}))
    
class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Set New password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm New password'}))