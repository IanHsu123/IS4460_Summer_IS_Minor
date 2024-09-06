from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Permit, Vehicle, Driver
from .forms import VehicleForm,PermitForm,DriverForm

class HomePage(View):
    def get(self,request):
        return render(request,'u_parking/home_page.html')
    


class Register(View):
    def get(self,request):
        return render(request,'u_parking/register.html')
    
    def post(self,request):
        return render(request,'u_parking/account.html')



class Permits(View):

    def get(self,request):
        permits = Permit.objects.all()
        context = {'permits':permits}
        return render(request, 'u_parking/permits.html',context)


class PermitEdit(View):

    def get(self,request,permit_id=None):

        if permit_id:
            Permits = Permit.objects.get(pk=permit_id)
        else:
            permit = Permits()

        form = PermitForm(instance=permit)

        return render(request = request,
                      template_name = 'u_parking/permit_edit.html',
                      context = {'permit':permit, 'form':form})

    def post(self,request,permit_id=None):

        if permit_id:
            permit = Permit.objects.get(pk=permit_id)
        else:
            permit = Permit()

        form = PermitForm(request.POST,instance=permit)

        if form.is_valid():
            vehicle = form.save()

            return redirect(reverse("permits"))
        
        return render(request= request,
                      template_name = 'u_parking.permit_edit.html',
                      context = {'permit':permit,'form':form})
    
    
class PermitDelete(View):

    def get(self,request,permit_id=None):

        if permit_id:
            permit = Permit.objects.get(pk=permit_id)
        else:
            permit = Permit()


        form = PermitForm(instance=permit)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'u_parking/permit_delete.html',context = {'permits':permit,'form':form})
      
    
    def post(self,request,permit_id=None):

        permit = Permit.objects.get(pk=permit_id)

        form = PermitForm(request.POST,instance=permit)

        permit.delete()

        return redirect(reverse("permits"))
    
class PermitDetails(View):

    def get(self,request,permit_id=None):

        if permit_id:
            permit = Permit.objects.get(pk=permit_id)
        else:
            permit = Permit()


        form = PermitForm(instance=permit)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'u_parking/permit_details.html',context = {'permit':permit,'form':form})


    def post(self,request,permit_id=None):

        permit = Permit.objects.get(pk=permit_id)

        form = PermitForm(request.POST,instance=permit)

        permit.delete()

        return redirect(reverse("permits"))
    
class PermitAdd(View):

    def get(self,request,permit_id=None):

        if permit_id:
            permit = Permit.objects.get(pk=permit_id)
        else:
            permit = Permit()

        form = PermitForm(instance=permit)

        return render(request = request,
                      template_name = 'u_parking/permit_add.html',
                      context = {'permit':permit, 'form':form})

    def post(self,request,permit_id=None):

        if permit_id:
            permit = Permit.objects.get(pk=permit_id)
        else:
            permit = Permit()

        form = PermitForm(request.POST,instance=permit)

        if form.is_valid():
            permit = form.save()

            return redirect(reverse("permit_add"))
        
        return render(request= request,
                      template_name = 'u_parking.permit_add.html',
                      context = {'permit':permit,'form':form})


class Login(View):
    def get(self,request):
        return render(request,'u_parking/login.html')
    
    def post(self,request):
        return render(request,'u_parking/account.html') 
    
class Account(View):
    def get(self,request):
        return render(request,'u_parking/account.html')
    
    def post(self,request):
        return render(request,'u_parking/home_page.html')
    


class Admin(View):
    def get(self,request):
        return render(request,'u_parking/admin.html')
    
    def post(self,request):
        return render(request,'u_parking/home_page.html')
    


class Vehicles(View):

    def get(self,request):
        Vehicles = Vehicle.objects.all()
        return render(request = request,template_name = 'u_parking/vehicles.html',context = {'vehicles':Vehicles})
    
class VehicleEdit(View):

    def get(self,request,vehicle_id=None):

        if vehicle_id:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        else:
            vehicle = Vehicle()

        form = VehicleForm(instance=vehicle)

        return render(request = request,
                      template_name = 'u_parking/permit_edit.html',
                      context = {'permit':Permit, 'form':form})

    def post(self,request,vehicle_id=None):

        if vehicle_id:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        else:
            vehicle = Vehicle()

        form = VehicleForm(request.POST,instance=vehicle)

        if form.is_valid():
            vehicle = form.save()

            return redirect(reverse("vehicle_edit"))
        
        return render(request= request,
                      template_name = 'u_parking.vehicle_edit.html',
                      context = {'vehicle':vehicle,'form':form})

class VehicleDelete(View):

    def get(self,request,vehicle_id=None):

        if vehicle_id:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        else:
            vehicle = Vehicle()


        form = VehicleForm(instance=vehicle)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'u_parking/vehicle_delete.html',context = {'vehicle':vehicle,'form':form})
      
    
    def post(self,request,vehicle_id=None):

        vehicle = Vehicle.objects.get(pk=vehicle_id)

        form = VehicleForm(request.POST,instance=vehicle)

        vehicle.delete()

        return redirect(reverse("vehicles"))
    
class VehicleDetails(View):

    def get(self,request,vehicle_id=None):

        if vehicle_id:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        else:
            vehicle = Vehicle()


        form = VehicleForm(instance=vehicle)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'u_parking/vehicle_details.html',context = {'vehicle':vehicle,'form':form})


    def post(self,request,vehicle_id=None):

        vehicle = Vehicle.objects.get(pk=vehicle_id)

        form = VehicleForm(request.POST,instance=vehicle)

        vehicle.delete()

        return redirect(reverse("vehicles"))
    
class VehicleAdd(View):

    def get(self,request,vehicle_id=None):

        if vehicle_id:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        else:
            vehicle = Vehicle()

        form = VehicleForm(instance=vehicle)

        return render(request = request,
                      template_name = 'u_parking/vehicle_add.html',
                      context = {'vehicle':vehicle, 'form':form})

    def post(self,request,vehicle_id=None):

        if vehicle_id:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        else:
            vehicle = Vehicle()

        form = VehicleForm(request.POST,instance=vehicle)

        if form.is_valid():
            vehicle = form.save()

            return redirect(reverse("vehicle_add"))
        
        return render(request= request,
                      template_name = 'u_parking.vehicle_add.html',
                      context = {'vehicle':vehicle,'form':form})
    


class Drivers(View):

    def get(self,request):
        drivers = Drivers.objects.all()
        context = {'drivers':drivers}
        return render(request, 'u_parking/drivers.html',context)

class DriverEdit(View):

    def get(self,request,driver_id=None):

        if driver_id:
            driver = Drivers.objects.get(pk=driver_id)
        else:
            driver = Driver()

        form = DriverForm(instance=driver)

        return render(request = request,
                      template_name = 'u_parking/driver_edit.html',
                      context = {'driver':Driver, 'form':form})

    def post(self,request,driver_id=None):

        if driver_id:
            driver = Driver.objects.get(pk=driver_id)
        else:
            driver = Driver()

        form = DriverForm(request.POST,instance=driver)

        if form.is_valid():
            driver = form.save()

            return redirect(reverse("driver_edit"))
        
        return render(request= request,
                      template_name = 'u_parking.driver_edit.html',
                      context = {'driver':driver,'form':form})

class DriverDelete(View):

    def get(self,request,driver_id=None):

        if driver_id:
            driver = Driver.objects.get(pk=driver_id)
        else:
            driver = Driver()


        form = DriverForm(instance=driver)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'u_parking/driver_delete.html',context = {'driver':driver,'form':form})
      
    
    def post(self,request,driver_id=None):

        driver = Driver.objects.get(pk=driver_id)

        form = DriverForm(request.POST,instance=driver)

        driver.delete()

        return redirect(reverse("drivers"))
    
class DriverDetails(View):

    def get(self,request,driver_id=None):

        if driver_id:
            driver = Driver.objects.get(pk=driver_id)
        else:
            driver = Driver()


        form = DriverForm(instance=driver)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'u_parking/driver_details.html',context = {'driver':driver,'form':form})


    def post(self,request,driver_id=None):

        driver = Driver.objects.get(pk=driver_id)

        form = DriverForm(request.POST,instance=driver)

        driver.delete()

        return redirect(reverse("drivers"))
    
class DriverAdd(View):

    def get(self,request,driver_id=None):

        if driver_id:
            driver = Driver.objects.get(pk=driver_id)
        else:
            driver = Driver()

        form = DriverForm(instance=driver)

        return render(request = request,
                      template_name = 'u_parking/driver_add.html',
                      context = {'driver':driver, 'form':form})

    def post(self,request,driver_id=None):

        if driver_id:
            driver = Driver.objects.get(pk=driver_id)
        else:
            driver = Driver()

        form = DriverForm(request.POST,instance=driver)

        if form.is_valid():
            driver = form.save()

            return redirect(reverse("drivers"))
        
        return render(request= request,
                      template_name = 'u_parking.driver_add.html',
                      context = {'driver':driver,'form':form})
    