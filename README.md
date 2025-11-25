# Sinkholes Dashboard 🕳️

A comprehensive web application for monitoring and analyzing sinkholes worldwide, built with Django (backend) and Leaflet (frontend).

## Features

- 🗺️ **Interactive Map**: Leaflet-based map showing sinkhole locations worldwide
- 📊 **Real-time Statistics**: 
  - Total sinkhole count
  - Active vs inactive sinkholes
  - Average diameter and depth
  - Risk level distribution
  - Geological type distribution
- 🔍 **Advanced Filtering**:
  - Filter by risk level (Low, Medium, High, Critical)
  - Filter by geological type (Karst, Dissolution, Subsidence, Collapse, Anthropogenic)
  - Toggle active/inactive sinkholes
- 📍 **Detailed Information**: Click on any marker to see comprehensive sinkhole data including:
  - Physical properties (diameter, depth)
  - Geological characteristics (soil type, bedrock, water table depth)
  - Risk assessment
  - Discovery and inspection dates
  - Activity status

## Technology Stack

### Backend
- **Django 5.2.8**: Web framework
- **Django REST Framework**: API development
- **Django CORS Headers**: Cross-origin resource sharing
- **SQLite**: Database (default)

### Frontend
- **Leaflet 1.9.4**: Interactive maps
- **Vanilla JavaScript**: Frontend logic
- **CSS3**: Modern styling with dark theme
- **CARTO Dark Theme**: Map tiles

## Project Structure

```
Sinkholes_dashboard/
├── be/                          # Backend Django application
│   ├── sinkholes/              # Main Django app
│   │   ├── models.py           # Sinkhole data model
│   │   ├── views.py            # API views and endpoints
│   │   ├── serializers.py      # REST API serializers
│   │   ├── urls.py             # App URL routing
│   │   ├── admin.py            # Django admin configuration
│   │   └── management/         # Custom management commands
│   │       └── commands/
│   │           └── populate_sinkholes.py  # Sample data generator
│   └── sinkholes_project/      # Django project settings
│       ├── settings.py         # Project configuration
│       └── urls.py             # Main URL routing
└── fe/                         # Frontend application
    ├── index.html              # Main HTML file
    ├── styles.css              # Stylesheet
    └── app.js                  # JavaScript application logic
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Virtual environment (included)

### Steps

1. **Activate Virtual Environment** (if not already activated):
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

2. **Install Dependencies** (already installed):
   - Django
   - djangorestframework
   - django-cors-headers

3. **Apply Migrations** (already done):
   ```powershell
   cd be
   python manage.py migrate
   ```

4. **Load Sample Data** (already loaded):
   ```powershell
   python manage.py populate_sinkholes
   ```

## Running the Application

1. **Start the Django Development Server**:
   ```powershell
   cd be
   python manage.py runserver
   ```

2. **Access the Dashboard**:
   - Open your browser and navigate to: `http://localhost:8000`
   - The dashboard will automatically load

## API Endpoints

### Sinkholes
- `GET /api/sinkholes/` - List all sinkholes
- `GET /api/sinkholes/{id}/` - Get specific sinkhole details
- `POST /api/sinkholes/` - Create new sinkhole
- `PUT /api/sinkholes/{id}/` - Update sinkhole
- `DELETE /api/sinkholes/{id}/` - Delete sinkhole

### Statistics
- `GET /api/sinkholes/statistics/` - Get comprehensive statistics

## Sample Data

The application includes 15 real-world sinkholes from around the globe:
- Dead Sea Sinkholes (Israel)
- Guatemala City Sinkhole (Guatemala)
- Xiaozhai Tiankeng (China)
- Bayou Corne Sinkhole (Louisiana, USA)
- Berezniki Sinkhole (Russia)
- Winter Park Sinkhole (Florida, USA)
- And more...

## Django Admin

Access the Django admin panel to manage sinkholes:

1. **Create a superuser**:
   ```powershell
   cd be
   python manage.py createsuperuser
   ```

2. **Access admin panel**:
   - Navigate to: `http://localhost:8000/admin`
   - Login with your superuser credentials

## Features in Detail

### Risk Levels
- **Low**: Stable sinkholes with minimal threat
- **Medium**: Moderate risk requiring monitoring
- **High**: Significant risk, active monitoring needed
- **Critical**: Immediate threat, urgent action required

### Geological Types
- **Karst**: Formed by dissolution of soluble rocks
- **Dissolution**: Chemical weathering processes
- **Subsidence**: Gradual sinking of ground surface
- **Collapse**: Sudden ground failure
- **Anthropogenic**: Human-induced sinkholes

## Customization

### Adding New Sinkholes
You can add sinkholes via:
1. Django Admin interface
2. REST API POST requests
3. Custom management commands

### Modifying the Map
Edit `fe/app.js` to:
- Change default map center and zoom
- Customize marker styles
- Adjust popup content
- Modify filtering logic

### Styling
Edit `fe/styles.css` to customize:
- Color schemes
- Layout dimensions
- Chart appearances
- Responsive breakpoints

## Development

### Adding New Features
1. Backend: Modify models in `be/sinkholes/models.py`
2. API: Update views in `be/sinkholes/views.py`
3. Frontend: Enhance `fe/app.js` and `fe/styles.css`

### Testing
```powershell
cd be
python manage.py test
```

## Production Deployment

Before deploying to production:
1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Update `CORS_ALLOW_ALL_ORIGINS` to specific domains
4. Use a production database (PostgreSQL recommended)
5. Set up proper static file serving
6. Use environment variables for sensitive settings

## License

This project is created for educational and monitoring purposes.

## Support

For issues or questions, please check:
- Django documentation: https://docs.djangoproject.com/
- Leaflet documentation: https://leafletjs.com/
- Django REST Framework: https://www.django-rest-framework.org/
