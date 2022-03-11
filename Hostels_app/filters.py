from .models import Hostel
from Users_app.forms import Hostel_Filter_Form
import django_filters

class HostelFilter(django_filters.FilterSet):
    class Meta:
        model = Hostel
        fields = ['category','attached_bathrooms','parking','wifi','gym','laundry','pets_friendly','tv','air_conditioning','balcony','water_heating','linens','iron','kitchen','watercooler','security_cameras','mess','verified']
        # form = Hostel_Filter_Form