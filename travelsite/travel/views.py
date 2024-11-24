# travel_package/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import TravelPackage, Booking
from .serializers import TravelPackageSerializer, BookingSerializer

@api_view(['GET'])
def travel_package_list(request):
    packages = TravelPackage.objects.all()
    serializer = TravelPackageSerializer(packages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def travel_package_detail(request, pk):
    try:
        package = TravelPackage.objects.get(pk=pk)
    except TravelPackage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TravelPackageSerializer(package)
    return Response(serializer.data)

@api_view(['POST'])
def booking_create(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def package_list(request):
    packages = TravelPackage.objects.all()
    return render(request, 'home.html', {'packages': packages})

def package_detail(request, pk):
    package = TravelPackage.objects.get(pk=pk)
    #images = package.images.all()
    if request.method == 'POST':
        form_data = request.POST
        booking = Booking(
            package=package,
            travel_date=form_data['travel_date'],
            number_of_people=form_data['number_of_people'],
            customer_name=form_data['customer_name'],
            customer_email=form_data['customer_email'],
            mobile_number=form_data['mobile_number']  # Save the mobile number
        )
        booking.save()
        return redirect('booking_confirmation', pk=booking.id)  # Redirect to the confirmation page with the booking ID
    
    return render(request, 'package_detail.html', {'package': package})

def booking_confirmation(request, pk):
    booking = Booking.objects.get(pk=pk)
    return render(request, 'confirmation.html', {'booking': booking})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
