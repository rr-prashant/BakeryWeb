from django.contrib import admin

from bakery_app.models import Banner, IntroSlider, about, accessories, cakeOnSale, cakes, contact_info, contact_us, phone

# Register your models here.


admin.site.register(IntroSlider)
admin.site.register(Banner)
admin.site.register(accessories)

class cakeAdmin(admin.ModelAdmin):
    list_display=('title', 'cake_price', 'is_featured')
    list_editable=('is_featured',)
admin.site.register(cakes, cakeAdmin)

admin.site.register(cakeOnSale)
admin.site.register(about)
admin.site.register(contact_info)
admin.site.register(contact_us)

class phoneAdmin(admin.ModelAdmin):
    list_display=('user', 'phone_number')
    
admin.site.register(phone, phoneAdmin)