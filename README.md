# Janonix Technologies Website

A professional business website built with Django, showcasing digital solutions and services.

## Features

- **Responsive Design**: Mobile-first approach with modern UI/UX
- **Dynamic Content**: Admin-manageable services, portfolio, and company information
- **Contact System**: Professional contact forms with email notifications
- **SEO Optimized**: Meta tags, structured data, and search engine friendly URLs
- **Modern Animations**: Smooth scroll animations using AOS library
- **Professional Styling**: Consistent brand colors and typography

## Technology Stack

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Styling**: Custom CSS with Bootstrap-inspired grid system
- **Icons**: Font Awesome
- **Animations**: AOS (Animate On Scroll)
- **Fonts**: Google Fonts (Inter)

## Pages

- **Home**: Hero section, services overview, portfolio preview, company highlights
- **About Us**: Company information, mission & vision, core values, team expertise
- **Services**: Detailed service offerings with process workflow
- **Portfolio**: Project showcase with statistics and success stories
- **Why Choose Us**: Company differentiators and client testimonials
- **Contact**: Contact form, FAQ section, and company information

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/janonix-website.git
cd janonix-website
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` to view the website

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root for production settings:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Admin Panel

Access the admin panel at `/admin/` to manage:
- Company information
- Services
- Portfolio projects
- User messages

## Deployment

### For Production

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure static files serving
5. Set up SSL/HTTPS

### Static Files

For production deployment, collect static files:
```bash
python manage.py collectstatic
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is proprietary software owned by Janonix Technologies Ltd.

## Contact

- **Website**: www.janonixtechnologiesltd.rw
- **Email**: info@janonixtechnologiesltd.rw
- **Location**: Kigali, Rwanda

## Brand Colors

- **Primary**: #523112 (Chocolate Brown)
- **Secondary**: #ffd700 (Golden Yellow)
- **Text**: #000000 (Black)
- **Background**: #ffffff (White)