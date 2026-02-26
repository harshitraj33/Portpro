## Personal Portfolio Website

A modern portfolio website built with Django, Django REST Framework, PostgreSQL, and Tailwind CSS. This is a personal portfolio project showcasing projects, skills, and professional experience.

## About The Owner

- **Name**: HARSHIT RAJ
- **Role**: Full Stack Developer & Cybersecurity Enthusiast
- **Education**: B.Tech in Computer Science and Engineering at Lovely Professional University
- **Location**: Phagwara, Punjab, India

## Features

- **User Authentication**: Sign up, login, logout with Django auth
- **Project Portfolio**: Showcase your projects with images, descriptions, and links
- **Project Categories**: Organize projects by category
- **Contact Form**: Send messages with email notifications
- **REST API**: Full CRUD API with token authentication
- **Admin Panel**: Easy content management
- **Responsive Design**: Mobile-friendly with Tailwind CSS
- **About Page**: Personal info, skills, internships, projects, certificates, and education

## Tech Stack

- **Backend**: Django 5.0+
- **Database**: PostgreSQL 15 (or SQLite for development)
- **API**: Django REST Framework
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Deployment**: Docker, Gunicorn, Whitenoise

## Skills

### Languages
- Python
- Java
- C++

### Frameworks
- Django
- React

### Tools & Platforms
- MySQL
- Git
- AWS
- Kali Linux

### Soft Skills
- Creative
- Problem Solver
- Active Listener
- Adaptability

## Internships

- **Conquest Tech Solutions** - Intern Computer Analyst (June-July 2023)
- **Coincent.ai** - Cyber Security & Ethical Hacking Training (January-March 2023)

## Projects

- **ArtiQuery (HBS Chats)** - AI Chatbot that works online/offline, handles voice I/O and image generation
- **Cyber Security Labs** - Practical exercises on penetration testing and threat analysis

## Certificates

- Master Generative AI & Generative AI tools by Infosys Springboard (Aug 2025)
- Privacy and Security in Online Social Media by NPTEL (April 2025)
- Amazon Web Service (AWS) Certified by Infosys Springboard (April 2024)
- Fundamentals of Network Communication by University of Colorado, Coursera (Sept 2024)
- GCP Cloud Digital Leader Certification by KodeKloud (April 2023)
- Cyber Security and Ethical Hacking by Coincent.ai (March 2023)

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL (optional, for development SQLite is used by default)
- Docker & Docker Compose (for containerized deployment)

### Local Development Setup

1. Clone the repository:
```
bash
git clone <repository-url>
cd Portpro
```

2. Create virtual environment:
```
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
bash
pip install -r requirements.txt
```

4. Set up environment variables:
```
bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```
bash
python manage.py migrate
```

6. Create superuser:
```
bash
python manage.py createsuperuser
```

7. Run development server:
```
bash
python manage.py runserver
```

8. Visit http://localhost:8000

### Docker Setup

1. Build and run with Docker Compose:
```
bash
docker-compose up --build
```

2. Visit http://localhost:8000

## Project Structure

```
Portpro/
├── .github/              # GitHub workflows
├── .dockerignore         # Docker ignore file
├── .env                  # Environment variables
├── accounts_app/         # User authentication app
├── api_app/              # REST API app
├── contact_app/          # Contact form app
├── projects_app/         # Portfolio projects app
├── Portpro/              # Django project settings
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── media/                # User-uploaded files
├── create_about.py       # Script to generate about page
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose config
├── requirements.txt      # Python dependencies
├── manage.py             # Django management script
└── README.md             # This file
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/projects/` | GET | List all projects |
| `/api/projects/` | POST | Create project (admin) |
| `/api/projects/{id}/` | GET | Get project details |
| `/api/projects/{id}/` | PUT | Update project (admin) |
| `/api/projects/{id}/` | DELETE | Delete project (admin) |
| `/api/projects/featured/` | GET | Get featured projects |
| `/api/contact/` | GET | List messages (admin) |
| `/api/contact/` | POST | Submit contact form |
| `/api/auth/login/` | POST | Login and get token |
| `/api/auth/register/` | POST | Register new user |
| `/api/auth/logout/` | POST | Logout and delete token |

## Environment Variables

Create a `.env` file with the following:

```
env
# Django Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (leave empty for SQLite)
DB_NAME=

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

## Management Commands

```
bash
# Create migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Create superuser
python manage.py createsuperuser

# Generate about page
python create_about.py
```

## Deployment

### Docker (Recommended)

```
bash
# Production build
docker-compose up --build -d

# View logs
docker-compose logs -f web
```

### Traditional

```
bash
# Server setup
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
gunicorn Portpro.wsgi:application --bind 0.0.0.0:8000
```

## Docker Configuration

The project includes:
- PostgreSQL 15 database
- Health checks for database readiness
- Volume mounts for static and media files
- Gunicorn WSGI server
- Whitenoise for static file serving

## License

MIT License - feel free to use this project for your own portfolio.

---

Built with ❤️ by HARSHIT RAJ
