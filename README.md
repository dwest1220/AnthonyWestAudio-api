# Anthony West Audio API

A robust Django REST API backend powering the Anthony West Audio business management platform. This API provides comprehensive endpoints for managing client inquiries, bookings, staff scheduling, and administrative operations for a professional audio engineering company.

## 📋 Project Overview

**NSS Full-Stack Capstone Project** - This API was developed as the backend component of my final project for Nashville Software School's Full-Stack Engineering program, demonstrating proficiency in Python, Django, REST API design, and database architecture.

This API serves as the backbone for a full-featured business management platform, handling everything from public inquiries to complex administrative workflows.

## 🚀 API Features

### Core Functionality
- **RESTful API Design**: Clean, consistent endpoints following REST principles
- **Client Inquiry Management**: Capture and process service requests
- **Booking System**: Convert inquiries to scheduled projects
- **Staff Management**: Handle team scheduling and availability
- **Cost Estimation**: Generate project quotes and pricing
- **Administrative Dashboard**: Backend support for business analytics

### Technical Features
- **Authentication & Authorization**: Secure access control for admin features
- **Data Validation**: Comprehensive input validation and error handling
- **Database Relationships**: Optimized relational data structure
- **CORS Configuration**: Proper cross-origin resource sharing setup
- **API Documentation**: Clear endpoint documentation

## 🛠️ Tech Stack

- **Framework**: Django 4.x
- **API**: Django REST Framework
- **Database**: SQLite (development)
- **Environment Management**: Pipenv
- **Authentication**: Django's built-in authentication system
- **Language**: Python 3.x

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- Pipenv

### Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AnthonyWestAudio-api.git
   cd AnthonyWestAudio-api
   ```

2. **Install dependencies with Pipenv**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

4. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **API Access**
   - API Root: `http://localhost:8000/api/`
   - Admin Panel: `http://localhost:8000/admin/`

## 🔗 Frontend Integration

This API is designed to work with the Anthony West Audio React frontend.

**Frontend Repository**: [anthony-west-audio](https://github.com/dwest1220/anthony-west-audio)

## 📊 Database Models

### Core Models
Based on the project structure, the API likely includes:
- **User**: Authentication and user management
- **Inquiry**: Client service requests and contact information
- **Booking**: Scheduled projects and appointments
- **Service**: Available service types and descriptions
- **Staff**: Team member information and assignments
- **BookingStaff**: Junction table for staff-booking relationships

### Model Relationships
```
Inquiry → Booking → Staff (Many-to-Many)
Service → Inquiry (Foreign Key)
Booking → Estimate (One-to-One)
```

## 🛣️ API Endpoints

### Public Endpoints
```
GET  /services/              # List available services
POST /inquiries/             # Submit new inquiry
```

### Authentication Endpoints
```
POST /auth/register/         # User registration
POST /auth/login/            # User login
POST /auth/logout/           # User logout
GET  /auth/user/             # User profile information
```

### Administrative Endpoints (Authentication Required)
```
GET    /inquiries/           # List all inquiries
PUT    /inquiries/{id}/      # Update inquiry status
GET    /users/               # User management
GET    /staff/               # Staff information
GET    /bookings/            # List all bookings
POST   /bookings/            # Create new booking
GET    /booking-staff/       # Staff booking assignments
```

## 🗄️ Project Structure

```
AnthonyWestAudio-api/
├── manage.py
├── Pipfile                    # Pipenv dependencies
├── Pipfile.lock              # Locked dependencies
├── seed_database.sh          # Database seeding script
├── audioproject/             # Main Django project
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
└── audioapi/                # Main Django app
    ├── __init__.py
    ├── admin.py             # Django admin configuration
    ├── apps.py              # App configuration
    ├── fixtures/            # Initial data fixtures
    ├── migrations/          # Database migrations
    ├── models/              # Database models
    ├── serializers/         # DRF serializers
    ├── views/               # API views
    ├── tests.py             # Unit tests
    └── urls.py              # App URL routing
```

## 🔧 Development

### Key Management Commands
```bash
# Database operations
python manage.py makemigrations
python manage.py migrate

# Development server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic
```

### Testing
```bash
python manage.py test
```

## 🔒 Security Features

- **CSRF Protection**: Built-in Django CSRF middleware
- **Authentication**: Session-based authentication for admin features
- **Input Validation**: DRF serializers for data validation
- **SQL Injection Protection**: Django ORM prevents SQL injection
- **CORS Configuration**: Proper cross-origin request handling

## 📈 API Design Principles

- **RESTful Architecture**: Consistent HTTP methods and status codes
- **Serialization**: DRF serializers for clean data transformation
- **Pagination**: Efficient data retrieval for large datasets
- **Error Handling**: Comprehensive error responses
- **Documentation**: Clear API documentation and examples

## 🚀 Deployment

### Production Considerations
- Switch to PostgreSQL for production database
- Configure proper environment variables
- Set up static file serving
- Enable SSL/HTTPS
- Configure production-ready web server (Gunicorn + Nginx)

### Environment Variables for Production
```env
SECRET_KEY=production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://...
```

## 🌟 Business Logic Highlights

### Inquiry to Booking Workflow
1. Client submits inquiry through frontend
2. Admin reviews inquiry in dashboard
3. Staff availability checked
4. Cost estimate generated
5. Booking created with scheduled dates

### Administrative Features
- **Inquiry Filtering**: Sort by service type, date, status
- **Cost Calculator**: Automated pricing based on service parameters
- **Staff Scheduler**: Manage team assignments and availability

## 👨‍💻 Developer

Built by [Your Name] as a capstone project for Nashville Software School's Full-Stack Engineering program.

**LinkedIn**: https://www.linkedin.com/in/david-west-a205a8274/
**GitHub**: https://github.com/dwest1220

---

*This API demonstrates proficiency in Python, Django, REST API design, database modeling, authentication systems, and backend architecture for real-world business applications.*