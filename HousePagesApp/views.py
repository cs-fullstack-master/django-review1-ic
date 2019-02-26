from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import House

# Create your views here.

def index(request):

    allHouses = House.objects.all()

    context = {
        "allHouses": allHouses
    }

    return render(request, 'HousePagesApp/index.html', context)


def details(request, houseID):
    selectedHouse = get_object_or_404(House, pk=houseID)

    context = {
        "house": selectedHouse
    }

    return render(request, "HousePagesApp/details.html", context)


def add5(request):
    print(request.POST["add5"])
    newNumber = int(request.POST["add5"])+5

    context = {
        "number": newNumber,
    }
    return render(request, "HousePagesApp/tonOPages.html", context)
    # return

def sub10(request):
    print(request.POST["add5"])
    newNumber = int(request.POST["add5"])-10

    context = {
        "number": newNumber,
    }
    return render(request, "HousePagesApp/tonOPages.html", context)

def mult2(request):
    print(request.POST["add5"])
    newNumber = int(request.POST["add5"])*2

    context = {
        "number": newNumber,
    }
    return render(request, "HousePagesApp/tonOPages.html", context)

def div10(request):
    print(request.POST["add5"])
    newNumber = int(request.POST["add5"])/10

    context = {
        "number": newNumber,
    }
    return render(request, "HousePagesApp/tonOPages.html", context)

def tonOPages(request):

    context = {
        "number": 0
    }

    return render(request, "HousePagesApp/tonOPages.html", context)