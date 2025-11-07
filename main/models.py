from django.db import models


class Service(models.Model):
    """Model for services offered by Janonix Technologies"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology_stack = models.CharField(max_length=500)
    project_url = models.URLField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']


class CompanyInfo(models.Model):
    """Model for company information"""
    company_name = models.CharField(max_length=200, default="Janonix Technologies Ltd")
    tagline = models.CharField(max_length=500)
    description = models.TextField()
    address = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField()
    
    # Social media links
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"


class WhyChooseUs(models.Model):
    """Model for why choose us reasons"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Why Choose Us"
        verbose_name_plural = "Why Choose Us"


class PartnerRequest(models.Model):
    """Stores partnership inquiries submitted from the About page."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    is_handled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company or 'Individual'}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Partner Request'
        verbose_name_plural = 'Partner Requests'


class TeamMember(models.Model):
    """Model for team members shown on the Meet Our Team page."""
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    # Use ImageField so admins can upload profile pictures.
    # Requires Pillow in the environment (already listed in requirements.txt).
    photo = models.ImageField(
        upload_to='team/',
        blank=True,
        null=True,
        help_text='Upload a profile image (will be stored in MEDIA_ROOT/team/)'
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
