from django.contrib import admin
from .models import Service, Project, ContactMessage, CompanyInfo, WhyChooseUs


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technology_stack', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description', 'technology_stack']
    list_editable = ['is_featured']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['created_at']


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'website']
    fieldsets = (
        ('Basic Information', {
            'fields': ('company_name', 'tagline', 'description')
        }),
        ('Contact Information', {
            'fields': ('address', 'email', 'phone', 'website')
        }),
        ('Social Media', {
            'fields': ('linkedin', 'twitter', 'facebook')
        }),
    )


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order']
