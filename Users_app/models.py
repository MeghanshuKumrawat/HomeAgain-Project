from django.db import models
from django.contrib.auth.models import AbstractUser


institute_choice = (("", "Select your Study location......."),
                    ("Acropolis Institute Of Technology And Research - AITR, Square, Malwa County, Manglaya Sadak, Indore, Madhya Pradesh", "Acropolis Institute Of Technology And Research - AITR, Square, Malwa County, Manglaya Sadak, Indore, Madhya Pradesh"),
                    ("Arihant College, Khandwa Road, opp. Radha Swami Satsang, Near DAVV Takshila Parisar, Opposite Radha Swami Satsang, Rani Bagh Main, Indore, Madhya Pradesh", "Arihant College, Khandwa Road, opp. Radha Swami Satsang, Near DAVV Takshila Parisar, Opposite Radha Swami Satsang, Rani Bagh Main, Indore, Madhya Pradesh"),
                    ("Arihant College, Khandwa Road, Radha Swami Satsang, Near DAVV Takshila Parisar, Opposite Radha Swami Satsang, Rani Bagh Main, Indore, Madhya Pradesh", "Arihant College, Khandwa Road, Radha Swami Satsang, Near DAVV Takshila Parisar, Opposite Radha Swami Satsang, Rani Bagh Main, Indore, Madhya Pradesh"),
                    ("Devi Ahilya Vishwavidyalaya Takshila Campus, Khandwa Road, Indrapuri Colony, Indra Puri Colony, Indore, Madhya Pradesh", "Devi Ahilya Vishwavidyalaya Takshila Campus, Khandwa Road, Indrapuri Colony, Indra Puri Colony, Indore, Madhya Pradesh"),
                    ("Government Holkar Science College Indore, AB Road, near Bhawarkua, Square, Indore, Madhya Pradesh", "Government Holkar Science College Indore, AB Road, near Bhawarkua, Square, Indore, Madhya Pradesh"),
                    ("Indore Institute of Law, opp. IIM, Indore, Madhya Pradesh", "Indore Institute of Law, opp. IIM, Indore, Madhya Pradesh"),
                    ("IPS Academy Institute of Business Management and Research,Knowledge Village, Rajendra Nagar , A.B Road, Indore, Madhya Pradesh 452012", "IPS Academy Institute of Business Management and Research,Knowledge Village, Rajendra Nagar , A.B Road, Indore, Madhya Pradesh 452012"),
                    ("KHAN STUDY GROUP(KSG),111-117,Veda Building, Bhanwarkua Square, near Apple Hospital, Indore, Madhya Pradesh 452001", " KHAN STUDY GROUP(KSG),111-117,Veda Building, Bhanwarkua Square, near Apple Hospital, Indore, Madhya Pradesh 452001"),
                    ("Ocean academy Indore, 56, Bhawarkua Main Rd, near Siddharth Nagar, Vishnu Puri Colony, Indore, Madhya Pradesh 452001", "Ocean academy Indore, 56, Bhawarkua Main Rd, near Siddharth Nagar, Vishnu Puri Colony, Indore, Madhya Pradesh 452001"),
                    ("Oriental University, Sanwer Rd, opposite Revati Range, Jakhya, Indore, Madhya Pradesh", "Oriental University, Sanwer Rd, opposite Revati Range, Jakhya, Indore, Madhya Pradesh"),
                    ("Prestige Institute of Engineering Management & Research, Sector-D, Scheme No 74, Vijay Nagar, Indore, Madhya Pradesh", "Prestige Institute of Engineering Management & Research, Sector-D, Scheme No 74, Vijay Nagar, Indore, Madhya Pradesh"),
                    ("Radiant Institute of Management and Science,SECTOR A BAKHTAWAR RAM NAGAR, near Tilak Nagar, Indore, Madhya Pradesh 452001", "Radiant Institute of Management and Science,SECTOR A BAKHTAWAR RAM NAGAR, near Tilak Nagar, Indore, Madhya Pradesh 452001"),
                    ("Renaissance College of Commerce & Management, behind Press Complex, Sunil Nagar, Krishna Bagh Colony, Indore, Madhya Pradesh", "Renaissance College of Commerce & Management, behind Press Complex, Sunil Nagar, Krishna Bagh Colony, Indore, Madhya Pradesh"),
                    ("SAGE University, Bypass Road, Kailod Kartal, Indore, Madhya Pradesh", "SAGE University, Bypass Road, Kailod Kartal, Indore, Madhya Pradesh"),
                    ("SDPS College, Shri Krishna Avenue, Limbodi, Indore, Madhya Pradesh", "SDPS College, Shri Krishna Avenue, Limbodi, Indore, Madhya Pradesh"),
                    ("Sgsits Main Gate, SGSITS Road, Shivaji Nagar, Indore, Madhya Pradesh", "Sgsits Main Gate, SGSITS Road, Shivaji Nagar, Indore, Madhya Pradesh"),
                    ("Shri Atal Bihari Vajpayee Government Arts And Commerce College, AB Road, Navlakha, Davv Takshila Parisar, Indore, Madhya Pradesh", "Shri Atal Bihari Vajpayee Government Arts And Commerce College, AB Road, Navlakha, Davv Takshila Parisar, Indore, Madhya Pradesh"),
                    ("Shri Vaishnav Institute of Management, Indore, Sector B, Gumasta Nagar, Scheme 71, Indore, Madhya Pradesh", "Shri Vaishnav Institute of Management, Indore, Sector B, Gumasta Nagar, Scheme 71, Indore, Madhya Pradesh"),
                    ("St. Paul Institute of Professional Studies Indore, Lalaram Nagar, Indore, Madhya Pradesh", "St. Paul Institute of Professional Studies Indore, Lalaram Nagar, Indore, Madhya Pradesh"),)

class CustomUser(AbstractUser):
    institute = models.CharField(choices=institute_choice, max_length=300, null=True)
    phone_no = models.IntegerField(default=0)
    profile = models.ImageField(upload_to='Profile_images', default='default.png')
    user_type = models.CharField(choices=(('HO', 'Hostel Owner'), ('HS', 'Hostel Seeker')), max_length=2)
    terms = models.BooleanField(default=False)
    slug = models.CharField(max_length=50)


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

