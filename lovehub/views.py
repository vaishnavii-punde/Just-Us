from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Only these users can access
ALLOWED_USERS = ["Guddya", "guddu"]

def is_allowed_user(user):
    """Check if user is in allowed list"""
    return user.is_authenticated and user.username in ALLOWED_USERS


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.username in ALLOWED_USERS:
                login(request, user)
                return redirect("home")
            else:
                logout(request)
                messages.error(request, "This space is not meant for everyone 🤍")
        else:
            messages.error(request, "Wrong username or password")

    return render(request, "lovehub/login.html")


@login_required(login_url="login")
def home(request):
    if not is_allowed_user(request.user):
        logout(request)
        messages.error(request, "Access denied 🤍")
        return redirect("login")
    
    try:
        from .models import Memory, ImportantDate
        from datetime import date
        
        recent_memories = Memory.objects.all()[:3]
        upcoming_dates = ImportantDate.objects.filter(date__gte=date.today()).order_by('date')[:3]
        
        context = {
            'recent_memories': recent_memories,
            'upcoming_dates': upcoming_dates,
        }
    except:
        context = {
            'recent_memories': [],
            'upcoming_dates': [],
        }
    
    return render(request, "lovehub/home.html", context)


@login_required(login_url="login")
def memories(request):
    if not is_allowed_user(request.user):
        logout(request)
        return redirect("login")
    
    try:
        from .models import Memory
        
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            memory_date = request.POST.get("date")
            image = request.FILES.get("image")
            
            Memory.objects.create(
                title=title,
                description=description,
                date=memory_date,
                image=image,
                created_by=request.user
            )
            messages.success(request, "Memory added! 💕")
            return redirect("memories")
        
        all_memories = Memory.objects.all()
        context = {"memories": all_memories}
    except:
        context = {"memories": []}
    
    return render(request, "lovehub/memories.html", context)



def about(request):
    return render(request, "lovehub/about.html")


def logout_view(request):
    logout(request)
    messages.success(request, "See you soon! 💕")
    return redirect("login")


from django.http import HttpResponse
from django.contrib.auth.models import User

def debug_database(request):
    """Temporary debug view - DELETE AFTER CHECKING"""
    users = User.objects.all()
    
    output = "<h1>Database Debug Info</h1>"
    output += f"<h2>Total Users: {users.count()}</h2>"
    
    if users.count() == 0:
        output += "<p style='color:red;'>❌ NO USERS IN DATABASE!</p>"
    else:
        output += "<ul>"
        for user in users:
            output += f"<li><strong>{user.username}</strong> - {user.email} - Is superuser: {user.is_superuser}</li>"
        output += "</ul>"
    
    # Check if our specific users exist
    guddya_exists = User.objects.filter(username='Guddya').exists()
    guddu_exists = User.objects.filter(username='guddu').exists()
    
    output += f"<p>Guddya exists: {'✅ YES' if guddya_exists else '❌ NO'}</p>"
    output += f"<p>guddu exists: {'✅ YES' if guddu_exists else '❌ NO'}</p>"
    
    return HttpResponse(output)