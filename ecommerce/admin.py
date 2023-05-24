from django.contrib import admin

from django.contrib import admin
from .models import Products,Category, Customer, Order

# 1
class AdminProduct(admin.ModelAdmin):
    # list_display = ['id','name', 'price', 'category','description']
    list_display = ['id','name', 'price', 'category','description','image']
admin.site.register(Products,AdminProduct)

# 2
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,CategoryAdmin)

# 3
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone','email','password']
admin.site.register(Customer,CustomerAdmin)

# 4
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product','customer','quantity','price','address','phone','date','status']
admin.site.register(Order,OrderAdmin)




