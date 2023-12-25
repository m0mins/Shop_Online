from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import BaseInlineFormSet
from App_Products.models import Category,Sub_Category,Product,Size,Color,Product_Color,Product_Size,Product_Image
# Register your models here.
class ProductImageInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        
        # Check if at least one image is present
        if any(self.errors):
            return

        has_at_least_one_image = False

        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('image'):
                    has_at_least_one_image = True
                    break

        if not has_at_least_one_image:
            raise forms.ValidationError('At least one image is required.')
  
class Product_SizeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Ensure that at least one size is selected
        if not any(form.cleaned_data.get('size') for form in self.forms):
            raise ValidationError('You must select at least one image.')

class Product_ColorInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        # Ensure that at least one size is selected
        if not any(form.cleaned_data.get('color') for form in self.forms):
  
            raise ValidationError('You must select at least one color.')

class Product_SizeInline(admin.TabularInline):
    model = Product_Size
    formset = Product_SizeInlineFormSet

class Product_ColorInline(admin.TabularInline):
    model = Product_Color
    formset = Product_ColorInlineFormSet
class ProductImageInline(admin.TabularInline):
    model = Product_Image
    extra = 1
    formset = ProductImageInlineFormSet

class ProductAdmin(admin.ModelAdmin):
    inlines = [Product_SizeInline,Product_ColorInline,ProductImageInline]

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product_Size)
admin.site.register(Product_Color)
admin.site.register(Product_Image)


