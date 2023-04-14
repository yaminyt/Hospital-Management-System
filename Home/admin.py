from django.contrib import admin
from .models import Department, doctor , Booking 

admin.site.register(Department)

admin.site.register(doctor)
class BookingAdmin(admin.ModelAdmin ):
    list_display=("id","p_name","p_phone","p_email","doc_name","booking_date","booked_on")


admin.site.register(Booking,BookingAdmin)


# Register your models here.
