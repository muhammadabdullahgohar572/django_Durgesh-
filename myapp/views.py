from django.shortcuts import render
import datetime  

def Home_page(request):
    return render(request, "Home.html")

def About(request):
    check = None  # ✅ Default value set ki taake error na aaye
    
    if request.method == "POST":
        check = request.POST.get("check", "")  # ✅ get() use kiya taake key error na aaye
        print(f"User Input: {check}")   

    date = datetime.datetime.now()
    is_Active = True
    name = "Code With Harry"

    # ✅ Structured Student Data
    students = {
        "School": "Ahmed",
        "College": "Bilal",
        "University": "Umar"
    }

    data = {
        "is_Active": is_Active,
        "name": name,
        "students": students,  # ✅ Dictionary
        "date": date,
        "check": check  # ✅ Form Input ka data bhejna
    }
    
    return render(request, "About.html", data)

def Services(request):
    return render(request, "services.html")
