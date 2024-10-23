import requests
from django.shortcuts import render

def get_client_ip(request):
    # ดึง IP address ของผู้ใช้
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(ip_address):
    # ใช้ IPstack API เพื่อดึงข้อมูลตำแหน่ง
    api_key = '45f090bf47e9a05b860deffbea12cdab'
    url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:  # ตรวจสอบสถานะการตอบกลับ
        location_data = response.json()
    else:
        location_data = {}  # กำหนดค่าเริ่มต้นถ้าไม่สามารถดึงข้อมูลได้
    
    return location_data

def get_language(request):
    # ดึงภาษาจาก HTTP_ACCEPT_LANGUAGE
    language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    return language.split(',')[0] if language else 'en'

def home(request):
    # ตรวจสอบว่า visits count มีใน session หรือไม่
    visits = request.session.get('visits', 0)
    visits += 1
    request.session['visits'] = visits

    # ดึง IP address และข้อมูลตำแหน่งที่ตั้ง
    ip_address = get_client_ip(request)
    location_data = get_location(ip_address)
    
    # ดึงข้อมูลภาษา
    language = get_language(request)

    # ส่งข้อมูลไปยัง template
    return render(request, 'base/home.html', {
        'visits': visits,
        'ip': ip_address,
        'location': location_data,
        'language': language  # ส่งข้อมูลภาษาไปยัง template
    })
