from django.shortcuts import render
from hector.models import *

# Create your views here.
def index(request, border=None):
    all_entries = Appareil.objects.all()
    with open("hector/info.txt", "r") as f:
        client, immatriculation, mise_en_circulation = f.readline().split()
    for i in all_entries:
        if client not in str(i.client):
            appareil = Appareil.objects.create(client=client, immatriculation=immatriculation,
                            mise_en_circulation = mise_en_circulation, dernier_passage="Aucun", status="Hors Ligne")
    
    oignon_style = ""
    salade_style = ""
    carotte_style = ""
    button_style = "border: 2px solid black;"

    if border == "oignon":
        oignon_style = button_style
        salade_style = ""
        carotte_style = ""
    elif border == "salade":
        oignon_style = ""
        salade_style = button_style
        carotte_style = ""
    elif border == "carotte":
        oignon_style = ""
        salade_style = ""
        carotte_style = button_style
    elif border == "reset":
        oignon_style = ""
        salade_style = ""
        carotte_style = ""

    context = {"immat":appareil.immatriculation, "circulation":appareil.mise_en_circulation,
                "last_mission":appareil.dernier_passage, "status":appareil.status,
                "oignon_style":oignon_style, "salade_style":salade_style, "carotte_style":carotte_style}

    return render(
        request,
            "hector/index.html",
        context=context,
    )   

# VALUES TO SEND TO THE GCODE GENERATOR
X_INTERVAL = 0
Y_INTERVAL = 0

def oignon(request):
    print("Oignon clicked")
    return index(request, "oignon")

def carotte(request):
    print("Carotte clicked")
    return index(request, "carotte")

def salade(request):
    print("Salade clicked")
    return index(request, "salade")

def reset(request):
    print("Reset clicked")
    return index(request, "reset")

def start_mission(request):
    print("Start clicked")
    return index(request)