from django.shortcuts import render
import requests
from django.http import JsonResponse

ESP_IP = ""

def kontrol_panel(request):
    return render(request, "base.html")

def komut_gonder(request, komut):
    print("GELEN KOMUT:", komut)
    try:
        r = requests.get(f"{ESP_IP}/{komut}", timeout=2)
        print("ESP RESPONSE:", r.status_code)
        return JsonResponse({"status": "ok"})
    except Exception as e:
        print("HATA:", e)
        return JsonResponse({"status": "esp baglanamadi"})