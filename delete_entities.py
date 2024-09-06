import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')
django.setup()

from u_parking.models import Driver, Permit, Vehicle

# Delete Permit

Permit.objects.all().delete()

# Delete Driver

Driver.objects.all().delete()

# Delete Vehicle

Vehicle.objects.all().delete()