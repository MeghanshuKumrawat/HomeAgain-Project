from unicodedata import name
from django.urls import path
from .views import (add_hostel, delete_hostel, edit_hostel, delete_hostel, activate_deactivate_hostel, hostel_promotion, 
                vendor_account_properties, hostels_catalog, hostel_single_view, add_hostel_wishlist,
                remove_hostel_wishlist)

urlpatterns = [
    path('add-property', add_hostel, name='add-property-page'),
    path('edit-property/<int:pk>', edit_hostel, name='edit-property-page'),
    path('delete-property/<int:pk>', delete_hostel, name='delete-property-page'),
    path('activate-property/<int:pk>', activate_deactivate_hostel, name='activate-property-page'),
    path('hostel-promotion', hostel_promotion, name='hostel-promotion-page'),
    path('vendor-account-properties', vendor_account_properties, name='vendor-account-properties-page'),
    path('hostels-catalog', hostels_catalog, name='hostels-catalog-page'),
    path('hostel-single-view/<int:pk>', hostel_single_view, name='hostel-single-view'),
    path('hostel-addto-wishlist/<int:pk>', add_hostel_wishlist, name='add-hostel-wishlist'),
    path('hostel-removefrom-wishlist/<int:pk>', remove_hostel_wishlist, name='remove-hostel-wishlist'),
]
