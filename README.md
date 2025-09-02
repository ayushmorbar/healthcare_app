# Healthcare App - Django Authentication System

A Django web application with role-based user authentication for Patients and Doctors.

## Features

- **User Registration**: Separate signup forms for Patients and Doctors
- **Role-based Authentication**: Automatic redirection to role-specific dashboards
- **Profile Management**: Complete user profiles with profile pictures
- **Responsive Design**: Bootstrap 5 with mobile-friendly interface
- **Admin Panel**: Django admin interface for user management

## Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/ayushmorbar/healthcare_app.git
cd healthcare_app
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Main app: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## User Types

### Patient Features
- Personal information management
- Medical history access
- Appointment booking interface
- Prescription viewing

### Doctor Features
- Professional profile management
- Patient management interface
- Appointment scheduling
- Prescription creation tools

## Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript
- **Authentication**: Django's built-in auth with custom User model
- **File Upload**: Pillow for image processing

## Project Structure

```
healthcare_app/
├── authentication/          # Main app
│   ├── models.py           # User, Patient, Doctor models
│   ├── forms.py            # Registration and login forms
│   ├── views.py            # Authentication views
│   └── admin.py            # Admin configuration
├── templates/              # HTML templates
├── static/                 # CSS, JS files
├── healthcare_app/         # Project settings
└── requirements.txt        # Dependencies
```

## Screenshots

### Home Page
The landing page with options to sign up as Patient or Doctor.

### User Registration
- Comprehensive signup forms with validation
- Profile picture upload
- Address information collection
- Password confirmation

### Dashboards
- **Patient Dashboard**: Personal information and medical tools
- **Doctor Dashboard**: Professional interface and patient management

## Key Features

### Form Validation
- Real-time password confirmation
- Pincode validation (6 digits)
- Email uniqueness validation
- Profile picture preview

### Security
- CSRF protection on all forms
- User role-based access control
- Secure file upload handling
- Django's built-in password validation

### User Experience
- Responsive Bootstrap design
- Auto-dismissing alerts
- Interactive form validation
- Clean, professional interface

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/signup/` | GET | User type selection |
| `/signup/patient/` | GET/POST | Patient registration |
| `/signup/doctor/` | GET/POST | Doctor registration |
| `/login/` | GET/POST | User login |
| `/logout/` | POST | User logout |
| `/dashboard/patient/` | GET | Patient dashboard |
| `/dashboard/doctor/` | GET | Doctor dashboard |
| `/admin/` | GET | Admin interface |

## Models

### User (Custom)
- Extends Django's AbstractUser
- Fields: user_type, profile_picture, address information
- Supports both Patient and Doctor types

### Patient
- One-to-one relationship with User
- Extensible for patient-specific data

### Doctor
- One-to-one relationship with User
- Extensible for doctor-specific data

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## Deployment

### Environment Variables
Create a `.env` file with:
```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
```

### Production Settings
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use PostgreSQL for production database
- Set up static file serving
- Configure HTTPS

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For support and questions:
- Create an issue in the repository
- Check Django documentation
- Review the code comments and docstrings