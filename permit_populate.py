import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')
django.setup()

from u_parking.models import Permit, Vehicle


Permit.objects.all().delete()

vehicle1 = Vehicle.objects.get (license_plate_number = "VHS1234")
vehicle2 = Vehicle.objects.get (license_plate_number = "UWL1846")
vehicle3 = Vehicle.objects.get (license_plate_number = "LQN2957")
vehicle4 = Vehicle.objects.get (license_plate_number = "XYZ1234")
vehicle5 = Vehicle.objects.get (license_plate_number = "LMN5678")
vehicle6 = Vehicle.objects.get (license_plate_number = "JKL9101")
vehicle7 = Vehicle.objects.get (license_plate_number = "QRS3456")
vehicle8 = Vehicle.objects.get (license_plate_number = "TUV7890")
vehicle9 = Vehicle.objects.get (license_plate_number = "PQR4321")
vehicle10 = Vehicle.objects.get (license_plate_number = "GHI8765")
vehicle11 = Vehicle.objects.get (license_plate_number = "ABC2345")
vehicle12 = Vehicle.objects.get (license_plate_number = "DEF3456")
vehicle13 = Vehicle.objects.get (license_plate_number = "GHI4567")
vehicle14 = Vehicle.objects.get (license_plate_number = "JKL5678")
vehicle15 = Vehicle.objects.get (license_plate_number = "MNO6789")
vehicle16 = Vehicle.objects.get (license_plate_number = "PQR7890")
vehicle17 = Vehicle.objects.get (license_plate_number = "STU8901")
vehicle18 = Vehicle.objects.get (license_plate_number = "VWX9012")
vehicle19 = Vehicle.objects.get (license_plate_number = "YZA0123")
vehicle20 = Vehicle.objects.get (license_plate_number = "BCD1234")


#Permit1

permit1 = Permit()
permit1.vehicle = vehicle1
permit1.permit_type = "U Permit"
permit1.purchase_date = "2024-08-19"
permit1.expiry_date = "2025-01-12"
permit1.cost = 172.5
permit1.save()

#Permit2

permit2 = Permit()
permit2.vehicle = vehicle2
permit2.permit_type = "CU Permit"
permit2.purchase_date = "2024-08-11"
permit2.expiry_date = "2025-01-12"
permit2.cost = 414
permit2.save()

#Permit3

permit3 = Permit()
permit3.vehicle = vehicle3
permit3.permit_type = "SHU Permit"
permit3.purchase_date = "2024-08-07"
permit3.expiry_date = "2025-01-12"
permit3.cost = 414
permit3.save()

#Permit4

permit4 = Permit()
permit4.vehicle = vehicle4
permit4.permit_type = "M Permit"
permit4.purchase_date = "2024-07-29"
permit4.expiry_date = "2025-01-12"
permit4.cost = 57.5
permit4.save()

#Permit5

permit5 = Permit()
permit5.vehicle = vehicle5
permit5.permit_type = "HU Permit"
permit5.purchase_date = "2024-08-3"
permit5.expiry_date = "2024-01-12"
permit5.cost = 172.5
permit5.save()

#Permit6

permit6 = Permit()
permit6.vehicle = vehicle6
permit6.permit_type = "HCU Permit"
permit6.purchase_date = "2024-08-1"
permit6.expiry_date = "2025-01-12"
permit6.cost = 414
permit6.save()


#Permit7

permit7 = Permit()
permit7.vehicle = vehicle7
permit7.permit_type = "RP Permit"
permit7.purchase_date = "2024-07-16"
permit7.expiry_date = "2025-01-12"
permit7.cost = 414
permit7.save()

#Permit8

permit8 = Permit()
permit8.vehicle = vehicle8
permit8.permit_type = "U Permit"
permit8.purchase_date = "2024-08-13"
permit8.expiry_date = "2025-01-12"
permit8.cost = 172.5
permit8.save()

#Permit9

permit9 = Permit()
permit9.vehicle = vehicle9
permit9.permit_type = "U Permit"
permit9.purchase_date = "2024-08-9"
permit9.expiry_date = "2025-01-12"
permit9.cost = 172.5
permit9.save()

#Permit10

permit10 = Permit()
permit10.vehicle = vehicle10
permit10.permit_type = "HU Permit"
permit10.purchase_date = "2024-07-26"
permit10.expiry_date = "2025-01-12"
permit10.cost = 172.5
permit10.save()

# Permit11

permit11 = Permit()
permit11.vehicle = vehicle11
permit11.permit_type = "U Permit"
permit11.purchase_date = "2024-08-25"
permit11.expiry_date = "2025-01-12"
permit11.cost = 172.5
permit11.save()

# Permit12

permit12 = Permit()
permit12.vehicle = vehicle12
permit12.permit_type = "CU Permit"
permit12.purchase_date = "2024-08-28"
permit12.expiry_date = "2025-01-12"
permit12.cost = 414
permit12.save()

# Permit13

permit13 = Permit()
permit13.vehicle = vehicle13
permit13.permit_type = "SHU Permit"
permit13.purchase_date = "2024-08-30"
permit13.expiry_date = "2025-01-12"
permit13.cost = 414
permit13.save()

# Permit14

permit14 = Permit()
permit14.vehicle = vehicle14
permit14.permit_type = "M Permit"
permit14.purchase_date = "2024-09-02"
permit14.expiry_date = "2025-01-12"
permit14.cost = 57.5
permit14.save()

# Permit15

permit15 = Permit()
permit15.vehicle = vehicle15
permit15.permit_type = "HU Permit"
permit15.purchase_date = "2024-09-05"
permit15.expiry_date = "2025-01-12"
permit15.cost = 172.5
permit15.save()

# Permit16

permit16 = Permit()
permit16.vehicle = vehicle16
permit16.permit_type = "HCU Permit"
permit16.purchase_date = "2024-09-08"
permit16.expiry_date = "2025-01-12"
permit16.cost = 414
permit16.save()

# Permit17

permit17 = Permit()
permit17.vehicle = vehicle17
permit17.permit_type = "RP Permit"
permit17.purchase_date = "2024-09-10"
permit17.expiry_date = "2025-01-12"
permit17.cost = 414
permit17.save()

# Permit18

permit18 = Permit()
permit18.vehicle = vehicle18
permit18.permit_type = "U Permit"
permit18.purchase_date = "2024-09-12"
permit18.expiry_date = "2025-01-12"
permit18.cost = 172.5
permit18.save()

# Permit19

permit19 = Permit()
permit19.vehicle = vehicle19
permit19.permit_type = "U Permit"
permit19.purchase_date = "2024-09-15"
permit19.expiry_date = "2025-01-12"
permit19.cost = 172.5
permit19.save()

# Permit20

permit20 = Permit()
permit20.vehicle = vehicle20
permit20.permit_type = "HU Permit"
permit20.purchase_date = "2024-09-18"
permit20.expiry_date = "2025-01-12"
permit20.cost = 172.5
permit20.save()
