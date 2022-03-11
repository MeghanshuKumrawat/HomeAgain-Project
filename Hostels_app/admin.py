from django.contrib import admin
from .models import Hostel, Hostel_images, HostelReview, Wishlist
from import_export.admin import ImportExportModelAdmin

class Hostel_IE(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class HostelImg_IE(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(Hostel, Hostel_IE)
admin.site.register(Hostel_images, HostelImg_IE)
admin.site.register(HostelReview)
admin.site.register(Wishlist)
