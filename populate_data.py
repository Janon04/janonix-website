#!/usr/bin/env python3
"""
Script to populate the database with sample data for Janonix Technologies website
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'janonix_website.settings')
django.setup()

from main.models import Service, Project, CompanyInfo, WhyChooseUs


def populate_services():
    """Create sample services"""
    services_data = [
        {
            'name': 'Website Development',
            'description': 'Modern, responsive websites built with cutting-edge technologies like Django, React, and Vue.js. We create fast, secure, and SEO-optimized websites that drive business growth.',
            'icon': 'fas fa-laptop-code'
        },
        {
            'name': 'Mobile App Development',
            'description': 'Native and cross-platform mobile applications for iOS and Android. We build user-friendly apps that provide seamless experiences across all devices.',
            'icon': 'fas fa-mobile-alt'
        },
        {
            'name': 'System API & Integration',
            'description': 'Seamless integration of third-party systems and APIs. We connect your applications with external services to enhance functionality and streamline operations.',
            'icon': 'fas fa-plug'
        },
        {
            'name': 'E-commerce Website',
            'description': 'Complete e-commerce solutions with payment integration, inventory management, and customer analytics. Build your online store with confidence.',
            'icon': 'fas fa-shopping-cart'
        },
        {
            'name': 'Website Maintenance & Security',
            'description': 'Ongoing maintenance, security updates, and performance optimization for your digital assets. Keep your website secure and running smoothly.',
            'icon': 'fas fa-shield-alt'
        },
        {
            'name': 'AI Integration',
            'description': 'Intelligent automation and AI-powered solutions to enhance your business processes. Implement chatbots, recommendation systems, and predictive analytics.',
            'icon': 'fas fa-brain'
        },
        {
            'name': 'IoT Projects',
            'description': 'Internet of Things solutions that connect devices and collect valuable data. Build smart systems for monitoring, automation, and control.',
            'icon': 'fas fa-wifi'
        },
        {
            'name': 'Professional Email',
            'description': 'Professional email setup and management services. Get custom domain emails with advanced security and collaboration features.',
            'icon': 'fas fa-envelope'
        },
        {
            'name': 'Personal & Professional Profiles',
            'description': 'Create compelling online profiles and portfolios that showcase your skills and achievements. Stand out in the digital world.',
            'icon': 'fas fa-user'
        }
    ]
    
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            name=service_data['name'],
            defaults=service_data
        )
        if created:
            print(f"Created service: {service.name}")
        else:
            print(f"Service already exists: {service.name}")


def populate_projects():
    """Create sample projects"""
    projects_data = [
        {
            'title': 'E-commerce Platform for Local Retailers',
            'description': 'A comprehensive e-commerce platform built for local retailers in Rwanda. Features include inventory management, payment integration with mobile money, and customer analytics dashboard.',
            'technology_stack': 'Django, React, PostgreSQL, Stripe API, Mobile Money Integration',
            'is_featured': True
        },
        {
            'title': 'Cooperative Management System',
            'description': 'A digital platform for managing cooperative societies, including member registration, loan management, savings tracking, and financial reporting.',
            'technology_stack': 'Python, Django, MySQL, Bootstrap, Chart.js',
            'is_featured': True
        },
        {
            'title': 'IoT Smart Agriculture Monitoring',
            'description': 'An IoT-based solution for monitoring soil moisture, temperature, and crop health. Includes mobile app for farmers and web dashboard for data analysis.',
            'technology_stack': 'Node.js, MongoDB, React Native, Arduino, Sensors',
            'is_featured': True
        },
        {
            'title': 'School Management System',
            'description': 'Complete school management solution with student records, grade management, attendance tracking, and parent communication portal.',
            'technology_stack': 'Django, Vue.js, PostgreSQL, Redis'
        },
        {
            'title': 'Healthcare Appointment System',
            'description': 'Online appointment booking system for healthcare providers with patient records, doctor scheduling, and SMS notifications.',
            'technology_stack': 'Flask, React, SQLite, Twilio API'
        }
    ]
    
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        if created:
            print(f"Created project: {project.title}")
        else:
            print(f"Project already exists: {project.title}")


def populate_company_info():
    """Create company information"""
    company_data = {
        'company_name': 'Janonix Technologies Ltd',
        'tagline': 'Empowering businesses with smart, scalable, and secure digital solutions',
        'description': 'We are a Rwandan technology company focused on innovation, integrity, and customer-centered software solutions. Our mission is to deliver high-quality, reliable, and affordable digital tools that empower businesses to thrive in the digital age.',
        'address': 'Kigali, Rwanda',
        'email': 'janonixtechnologiesltd@gmail.com',
        'phone': '+250786003139',
        'website': 'https://www.janonix.rw',
        'linkedin': 'https://linkedin.com/company/janonix-technologies',
        'twitter': 'https://twitter.com/janonixtech',
        'facebook': 'https://facebook.com/janonixtech'
    }
    
    company_info, created = CompanyInfo.objects.get_or_create(
        company_name=company_data['company_name'],
        defaults=company_data
    )
    
    # Update existing record with new data
    if not created:
        for key, value in company_data.items():
            setattr(company_info, key, value)
        company_info.save()
        print(f"Updated company info: {company_info.company_name}")
    else:
        print(f"Created company info: {company_info.company_name}")


def populate_why_choose_us():
    """Create why choose us reasons"""
    reasons_data = [
        {
            'title': 'Reliable & Secure',
            'description': 'We prioritize security and reliability in all our solutions. Your data and applications are protected with industry-standard security measures.',
            'icon': 'fas fa-shield-alt',
            'order': 1
        },
        {
            'title': 'Affordable Pricing',
            'description': 'Competitive pricing without compromising on quality. We offer flexible payment plans that fit your budget and business needs.',
            'icon': 'fas fa-dollar-sign',
            'order': 2
        },
        {
            'title': 'Customer-Centered Approach',
            'description': 'Your success is our priority. We work closely with you to understand your needs and deliver solutions that exceed expectations.',
            'icon': 'fas fa-users',
            'order': 3
        },
        {
            'title': 'Innovation Focus',
            'description': 'We stay ahead of technology trends and use cutting-edge tools to build future-ready solutions for your business.',
            'icon': 'fas fa-lightbulb',
            'order': 4
        },
        {
            'title': '24/7 Support',
            'description': 'Round-the-clock technical support to ensure your systems run smoothly. We are always here when you need us.',
            'icon': 'fas fa-headset',
            'order': 5
        },
        {
            'title': 'Local Expertise',
            'description': 'Deep understanding of the Rwandan market and business environment. We build solutions that work in your local context.',
            'icon': 'fas fa-map-marker-alt',
            'order': 6
        }
    ]
    
    for reason_data in reasons_data:
        reason, created = WhyChooseUs.objects.get_or_create(
            title=reason_data['title'],
            defaults=reason_data
        )
        if created:
            print(f"Created reason: {reason.title}")
        else:
            print(f"Reason already exists: {reason.title}")


def main():
    """Main function to populate all data"""
    print("Starting data population...")
    
    populate_company_info()
    populate_services()
    populate_projects()
    populate_why_choose_us()
    
    print("\nData population completed successfully!")
    print("\nYou can now:")
    print("1. Run the development server: python manage.py runserver")
    print("2. Access the admin panel at: http://localhost:8000/admin/")
    print("   Username: admin")
    print("   Password: admin123")
    print("3. View the website at: http://localhost:8000/")


if __name__ == '__main__':
    main()
