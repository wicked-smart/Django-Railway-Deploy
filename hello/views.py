from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Flight, Airport, Passenger
# Create your views here.


def index(request):
    flights = Flight.objects.all()
    return render(request, "hello/index.html", {
        "flights": flights
    })

def detail(request, flight_id):
    
    try:
        flight = Flight.objects.get(pk=flight_id)
        passengers = flight.passengers.all()
        non_passengers = Passenger.objects.exclude(flight=flight)

        return render(request, "hello/flight_detail.html", {
            "flight": flight,
            "passengers": passengers,
            "non_passengers": non_passengers
        })
    
    except Flight.DoesNotExist:
        return render(request, "hello/flight_detail.html", {"message": "Flight Does Not Exists!"})


def book(request, flight_id):
    if request.method == "POST":
        try:
           passenger_id = int(request.POST["passenger"])
           passenger = Passenger.objects.get(pk=passenger_id)
           flight = Flight.objects.get(pk=flight_id)

        except KeyError:
            return render(request, "hello/flight_detail.html", {"message": "Passenger not selected!"})
        except Passenger.DoesNotExist:
            return render(request, "hello/flight_detail.html", {"message": "Passenger not found !"})
        except Flight.DoesNotExist:
            return render(request, "hello/flight_detail.html", {"message": "Flight Does Not  Exists !"})



         #Book the ticket
        flight.passengers.add(passenger)
        return HttpResponseRedirect(reverse('flight_detail', args=(flight_id,)))
