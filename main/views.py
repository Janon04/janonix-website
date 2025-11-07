from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Service, Project, CompanyInfo, WhyChooseUs, ContactMessage, PartnerRequest
from .models import TeamMember


def home(request):
    """Home page view"""
    context = {
        'services': Service.objects.filter(is_active=True)[:6],
        'featured_projects': Project.objects.filter(is_featured=True)[:3],
        'why_choose_us': WhyChooseUs.objects.filter(is_active=True)[:4],
        'company_info': CompanyInfo.objects.first(),
    }
    return render(request, 'main/home.html', context)


def about(request):
    """About page view"""
    if request.method == 'POST':
        # Handle Partner with Us submissions
        name = request.POST.get('partner_name')
        email = request.POST.get('partner_email')
        company = request.POST.get('partner_company')
        message_text = request.POST.get('partner_message')

        if name and email and message_text:
            PartnerRequest.objects.create(
                name=name,
                email=email,
                company=company,
                message=message_text
            )
            messages.success(request, 'Thank you — your partnership inquiry has been received. We will contact you soon.')
            return redirect('about')
        else:
            messages.error(request, 'Please fill in your name, email, and a short message to partner with us.')

    context = {
        'company_info': CompanyInfo.objects.first(),
    }
    return render(request, 'main/about.html', context)


def services(request):
    """Services page view"""
    context = {
        'services': Service.objects.filter(is_active=True),
    }
    return render(request, 'main/services.html', context)


def portfolio(request):
    """Portfolio page view"""
    context = {
        'projects': Project.objects.all(),
        'featured_projects': Project.objects.filter(is_featured=True),
    }
    return render(request, 'main/portfolio.html', context)


def why_choose_us(request):
    """Why Choose Us page view"""
    context = {
        'reasons': WhyChooseUs.objects.filter(is_active=True),
    }
    return render(request, 'main/why_choose_us.html', context)


def team(request):
    """Meet Our Team page view"""
    members = TeamMember.objects.filter(is_active=True)
    context = {
        'members': members,
        'company_info': CompanyInfo.objects.first(),
    }
    return render(request, 'main/team.html', context)


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    context = {
        'company_info': CompanyInfo.objects.first(),
    }
    return render(request, 'main/contact.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def contact_api(request):
    """API endpoint for contact form submission"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! We will get back to you soon.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON data.'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred while processing your request.'
        }, status=500)
