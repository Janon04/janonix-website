from django.contrib import admin
from .models import Service, Project, ContactMessage, CompanyInfo, WhyChooseUs, TeamMember, PartnerRequest
from django.utils.html import format_html


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


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_active', 'order', 'photo_preview']
    list_filter = ['is_active']
    search_fields = ['name', 'role']
    list_editable = ['is_active', 'order']
    readonly_fields = ['photo_preview']
    fields = ('name', 'role', 'bio', 'photo', 'photo_preview', 'order', 'is_active')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;" />', obj.photo.url)
        return '(no image)'

    photo_preview.short_description = 'Photo'


@admin.register(PartnerRequest)
class PartnerRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'email', 'is_handled', 'created_at']
    list_filter = ['is_handled', 'created_at']
    search_fields = ['name', 'company', 'email', 'message']
    readonly_fields = ['created_at']
