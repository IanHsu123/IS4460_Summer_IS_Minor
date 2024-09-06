import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')
django.setup()

from u_parking.models import Driver

Driver.objects.all().delete()

#Driver1

driver1 = Driver()
driver1.driver_first_name = "John"
driver1.driver_middle_name = "Doe"
driver1.driver_last_name = "Smith"
driver1.driver_type = "Student"
driver1.address = "5678 W 200 S, Salt Lake City, UT 84104"
driver1.save()

#Driver2

driver2 = Driver()
driver2.driver_first_name = "Ethan"
driver2.driver_middle_name = "Alexander"
driver2.driver_last_name = "Mitchell"
driver2.driver_type = "Staff"
driver2.address = "1234 S Main St, Salt Lake City, UT 84115"
driver2.save()

#Driver3

driver3 = Driver()
driver3.driver_first_name = "Jasmine"
driver3.driver_middle_name = "Alex"
driver3.driver_last_name = "Montgomery"
driver3.driver_type = "Student"
driver3.address = "910 E 900 S, Salt Lake City, UT 84105"
driver3.save()

# Driver4

driver4 = Driver()
driver4.driver_first_name = "Olivia"
driver4.driver_middle_name = "Marie"
driver4.driver_last_name = "Johnson"
driver4.driver_type = "Staff"
driver4.address = "2345 N Temple St, Salt Lake City, UT 84116"
driver4.save()

# Driver5

driver5 = Driver()
driver5.driver_first_name = "William"
driver5.driver_middle_name = "James"
driver5.driver_last_name = "Brown"
driver5.driver_type = "Staff"
driver5.address = "6789 S State St, Salt Lake City, UT 84107"
driver5.save()

# Driver6

driver6 = Driver()
driver6.driver_first_name = "Sophia"
driver6.driver_middle_name = "Grace"
driver6.driver_last_name = "Petty"
driver6.driver_type = "Student"
driver6.address = "1357 W North Temple St, Salt Lake City, UT 84116"
driver6.save()

# Driver7

driver7 = Driver()
driver7.driver_first_name = "Liam"
driver7.driver_middle_name = "Henry"
driver7.driver_last_name = "Moore"
driver7.driver_type = "Staff"
driver7.address = "2468 E 1300 S, Salt Lake City, UT 84108"
driver7.save()

# Driver8

driver8 = Driver()
driver8.driver_first_name = "Isabella"
driver8.driver_middle_name = "Renee"
driver8.driver_last_name = "Jackson"
driver8.driver_type = "Student"
driver8.address = "975 W 800 S, Salt Lake City, UT 84104"
driver8.save()

# Driver9

driver9 = Driver()
driver9.driver_first_name = "Mason"
driver9.driver_middle_name = "Lee"
driver9.driver_last_name = "Martin"
driver9.driver_type = "Staff"
driver9.address = "1100 E 400 S, Salt Lake City, UT 84102"
driver9.save()

# Driver10

driver10 = Driver()
driver10.driver_first_name = "Ava"
driver10.driver_middle_name = "Rose"
driver10.driver_last_name = "Martinez"
driver10.driver_type = "Student"
driver10.address = "385 E 3300 S, Salt Lake City, UT 84115"
driver10.save()

# Driver11
driver11 = Driver()
driver11.driver_first_name = "Charlotte"
driver11.driver_middle_name = "Elizabeth"
driver11.driver_last_name = "Davis"
driver11.driver_type = "Student"
driver11.address = "1500 E 2100 S, Salt Lake City, UT 84106"
driver11.save()

# Driver12
driver12 = Driver()
driver12.driver_first_name = "James"
driver12.driver_middle_name = "Michael"
driver12.driver_last_name = "Williams"
driver12.driver_type = "Staff"
driver12.address = "305 W 600 N, Salt Lake City, UT 84116"
driver12.save()

# Driver13
driver13 = Driver()
driver13.driver_first_name = "Amelia"
driver13.driver_middle_name = "Faith"
driver13.driver_last_name = "Flores"
driver13.driver_type = "Student"
driver13.address = "428 E 800 S, Salt Lake City, UT 84111"
driver13.save()

# Driver14
driver14 = Driver()
driver14.driver_first_name = "Benjamin"
driver14.driver_middle_name = "Robert"
driver14.driver_last_name = "Scott"
driver14.driver_type = "Staff"
driver14.address = "7890 W 3500 S, Salt Lake City, UT 84120"
driver14.save()

# Driver15
driver15 = Driver()
driver15.driver_first_name = "Mia"
driver15.driver_middle_name = "Ann"
driver15.driver_last_name = "Walker"
driver15.driver_type = "Student"
driver15.address = "562 E 300 S, Salt Lake City, UT 84102"
driver15.save()

# Driver16
driver16 = Driver()
driver16.driver_first_name = "Henry"
driver16.driver_middle_name = "Samuel"
driver16.driver_last_name = "Harris"
driver16.driver_type = "Staff"
driver16.address = "1900 N 2200 W, Salt Lake City, UT 84116"
driver16.save()

# Driver17
driver17 = Driver()
driver17.driver_first_name = "Ella"
driver17.driver_middle_name = "Marie"
driver17.driver_last_name = "Thompson"
driver17.driver_type = "Student"
driver17.address = "672 E 200 S, Salt Lake City, UT 84111"
driver17.save()

# Driver18
driver18 = Driver()
driver18.driver_first_name = "Daniel"
driver18.driver_middle_name = "Joseph"
driver18.driver_last_name = "Sanchez"
driver18.driver_type = "Staff"
driver18.address = "445 W 300 N, Salt Lake City, UT 84103"
driver18.save()

# Driver19
driver19 = Driver()
driver19.driver_first_name = "Emily"
driver19.driver_middle_name = "Jane"
driver19.driver_last_name = "King"
driver19.driver_type = "Student"
driver19.address = "255 S 700 E, Salt Lake City, UT 84102"
driver19.save()

# Driver20
driver20 = Driver()
driver20.driver_first_name = "Matthew"
driver20.driver_middle_name = "David"
driver20.driver_last_name = "Torres"
driver20.driver_type = "Staff"
driver20.address = "800 W 300 S, Salt Lake City, UT 84104"
driver20.save()