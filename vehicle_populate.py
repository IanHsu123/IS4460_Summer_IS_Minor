import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')
django.setup()

from u_parking.models import Vehicle, Driver

Vehicle.objects.all().delete()

driver1 = Driver.objects.get (driver_last_name = "Smith")
driver2 = Driver.objects.get (driver_last_name = "Mitchell")
driver3 = Driver.objects.get (driver_last_name = "Montgomery")
driver4 = Driver.objects.get (driver_last_name = "Johnson")
driver5 = Driver.objects.get (driver_last_name = "Brown")
driver6 = Driver.objects.get (driver_last_name = "Petty")
driver7 = Driver.objects.get (driver_last_name = "Moore")
driver8 = Driver.objects.get (driver_last_name = "Jackson")
driver9 = Driver.objects.get (driver_last_name = "Martin")
driver10 = Driver.objects.get (driver_last_name = "Martinez")
driver11 = Driver.objects.get (driver_last_name = "Davis")
driver12 = Driver.objects.get (driver_last_name = "Williams")
driver13 = Driver.objects.get (driver_last_name = "Flores")
driver14 = Driver.objects.get (driver_last_name = "Scott")
driver15 = Driver.objects.get (driver_last_name = "Walker")
driver16 = Driver.objects.get (driver_last_name = "Harris")
driver17 = Driver.objects.get (driver_last_name = "Thompson")
driver18 = Driver.objects.get (driver_last_name = "Sanchez")
driver19 = Driver.objects.get (driver_last_name = "King")
driver20 = Driver.objects.get (driver_last_name = "Torres")

#vehicle1

vehicle1 = Vehicle()
vehicle1.driver = driver1
vehicle1.license_plate_number = "VHS1234"
vehicle1.vehicle_make = "BMW"
vehicle1.model = "X3"
vehicle1.color = "White"
vehicle1.year = "2012"
vehicle1.save()

#vehicle2

vehicle2 = Vehicle()
vehicle2.driver = driver2
vehicle2.license_plate_number = "UWL1846"
vehicle2.vehicle_make = "Toyota"
vehicle2.model = "4Runner"
vehicle2.color = "White"
vehicle2.year = "2011"
vehicle2.save()

#vehicle3

vehicle3 = Vehicle()
vehicle3.driver = driver3
vehicle3.license_plate_number = "LQN2957"
vehicle3.vehicle_make = "Hyundai"
vehicle3.model = "Tucson"
vehicle3.color = "Grey"
vehicle3.year = "2015"
vehicle3.save()

# vehicle4
vehicle4 = Vehicle()
vehicle4.driver = driver4
vehicle4.license_plate_number = "XYZ1234"
vehicle4.vehicle_make = "Toyota"
vehicle4.model = "Corolla"
vehicle4.color = "Blue"
vehicle4.year = "2018"
vehicle4.save()

# vehicle5
vehicle5 = Vehicle()
vehicle5.driver = driver5
vehicle5.license_plate_number = "LMN5678"
vehicle5.vehicle_make = "Ford"
vehicle5.model = "Escape"
vehicle5.color = "White"
vehicle5.year = "2020"
vehicle5.save()

# vehicle6
vehicle6 = Vehicle()
vehicle6.driver = driver6
vehicle6.license_plate_number = "JKL9101"
vehicle6.vehicle_make = "Chevrolet"
vehicle6.model = "Malibu"
vehicle6.color = "Black"
vehicle6.year = "2017"
vehicle6.save()

# vehicle7
vehicle7 = Vehicle()
vehicle7.driver = driver7
vehicle7.license_plate_number = "QRS3456"
vehicle7.vehicle_make = "Honda"
vehicle7.model = "Civic"
vehicle7.color = "Red"
vehicle7.year = "2019"
vehicle7.save()

# vehicle8
vehicle8 = Vehicle()
vehicle8.driver = driver8
vehicle8.license_plate_number = "TUV7890"
vehicle8.vehicle_make = "Nissan"
vehicle8.model = "Altima"
vehicle8.color = "Silver"
vehicle8.year = "2016"
vehicle8.save()

# vehicle9
vehicle9 = Vehicle()
vehicle9.driver = driver9
vehicle9.license_plate_number = "PQR4321"
vehicle9.vehicle_make = "Mazda"
vehicle9.model = "CX-5"
vehicle9.color = "Grey"
vehicle9.year = "2021"
vehicle9.save()

# vehicle10
vehicle10 = Vehicle()
vehicle10.driver = driver10
vehicle10.license_plate_number = "GHI8765"
vehicle10.vehicle_make = "Kia"
vehicle10.model = "Soul"
vehicle10.color = "Green"
vehicle10.year = "2014"
vehicle10.save()

# Vehicle11
vehicle11 = Vehicle()
vehicle11.driver = driver11
vehicle11.license_plate_number = "ABC2345"
vehicle11.vehicle_make = "Audi"
vehicle11.model = "A4"
vehicle11.color = "Black"
vehicle11.year = "2013"
vehicle11.save()

# Vehicle12
vehicle12 = Vehicle()
vehicle12.driver = driver12
vehicle12.license_plate_number = "DEF3456"
vehicle12.vehicle_make = "Subaru"
vehicle12.model = "Outback"
vehicle12.color = "Blue"
vehicle12.year = "2014"
vehicle12.save()

# Vehicle13
vehicle13 = Vehicle()
vehicle13.driver = driver13
vehicle13.license_plate_number = "GHI4567"
vehicle13.vehicle_make = "Volkswagen"
vehicle13.model = "Jetta"
vehicle13.color = "White"
vehicle13.year = "2015"
vehicle13.save()

# Vehicle14
vehicle14 = Vehicle()
vehicle14.driver = driver14
vehicle14.license_plate_number = "JKL5678"
vehicle14.vehicle_make = "Mercedes-Benz"
vehicle14.model = "C-Class"
vehicle14.color = "Silver"
vehicle14.year = "2016"
vehicle14.save()

# Vehicle15
vehicle15 = Vehicle()
vehicle15.driver = driver15
vehicle15.license_plate_number = "MNO6789"
vehicle15.vehicle_make = "Tesla"
vehicle15.model = "Model S"
vehicle15.color = "Red"
vehicle15.year = "2017"
vehicle15.save()

# Vehicle16
vehicle16 = Vehicle()
vehicle16.driver = driver16
vehicle16.license_plate_number = "PQR7890"
vehicle16.vehicle_make = "Volvo"
vehicle16.model = "XC90"
vehicle16.color = "Grey"
vehicle16.year = "2018"
vehicle16.save()

# Vehicle17
vehicle17 = Vehicle()
vehicle17.driver = driver17
vehicle17.license_plate_number = "STU8901"
vehicle17.vehicle_make = "Ford"
vehicle17.model = "F-150"
vehicle17.color = "Blue"
vehicle17.year = "2019"
vehicle17.save()

# Vehicle18
vehicle18 = Vehicle()
vehicle18.driver = driver18
vehicle18.license_plate_number = "VWX9012"
vehicle18.vehicle_make = "Chevrolet"
vehicle18.model = "Tahoe"
vehicle18.color = "Black"
vehicle18.year = "2020"
vehicle18.save()

# Vehicle19
vehicle19 = Vehicle()
vehicle19.driver = driver19
vehicle19.license_plate_number = "YZA0123"
vehicle19.vehicle_make = "Jeep"
vehicle19.model = "Wrangler"
vehicle19.color = "Green"
vehicle19.year = "2021"
vehicle19.save()

# Vehicle20
vehicle20 = Vehicle()
vehicle20.driver = driver20
vehicle20.license_plate_number = "BCD1234"
vehicle20.vehicle_make = "Toyota"
vehicle20.model = "Camry"
vehicle20.color = "White"
vehicle20.year = "2022"
vehicle20.save()