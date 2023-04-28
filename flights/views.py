from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import Flight, Passenger

# Create your views here.

# view to display all flights on index.html


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    # get a flight whose id is flight_id
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passenger": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        # get the flight id
        flight = Flight.objects.get(pk=flight_id)
        # tell what passenger is booking the flight -
        # by picking data from a form with an input field whose name is passenger
        # convert it into an integer so that you get an int value
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # add the passenger to the flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id, )))
