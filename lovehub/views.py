from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date

ALLOWED_USERS = ["Guddya", "guddu", "admin"]


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
    if request.user.username not in ALLOWED_USERS:
        logout(request)
        messages.error(request, "Access denied 🤍")
        return redirect("login")
    
    try:
        from .models import Memory, ImportantDate, LoveNote, LoveLetter
        
        recent_memories = Memory.objects.all()[:3]
        upcoming_dates = ImportantDate.objects.filter(date__gte=date.today())[:3]
        unread_notes = LoveNote.objects.filter(is_read=False).exclude(sender=request.user)
        love_letters = LoveLetter.objects.all()[:5]
        
        context = {
            'recent_memories': recent_memories,
            'upcoming_dates': upcoming_dates,
            'unread_notes_count': unread_notes.count(),
            'love_letters': love_letters,
        }
    except:
        context = {
            'recent_memories': [],
            'upcoming_dates': [],
            'unread_notes_count': 0,
            'love_letters': [],
        }
    
    return render(request, "lovehub/home.html", context)


@login_required(login_url="login")
def memories(request):
    if request.user.username not in ALLOWED_USERS:
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


@login_required(login_url="login")
def love_notes(request):
    if request.user.username not in ALLOWED_USERS:
        logout(request)
        return redirect("login")
    
    try:
        from .models import LoveNote
        
        if request.method == "POST":
            message = request.POST.get("message")
            LoveNote.objects.create(sender=request.user, message=message)
            messages.success(request, "Love note sent! 💌")
            return redirect("love_notes")
        
        received_notes = LoveNote.objects.exclude(sender=request.user)
        sent_notes = LoveNote.objects.filter(sender=request.user)
        
        received_notes.filter(is_read=False).update(is_read=True)
        
        context = {
            'received_notes': received_notes,
            'sent_notes': sent_notes,
        }
    except:
        context = {
            'received_notes': [],
            'sent_notes': [],
        }
    
    return render(request, "lovehub/love_notes.html", context)


@login_required(login_url="login")
def important_dates(request):
    if request.user.username not in ALLOWED_USERS:
        logout(request)
        return redirect("login")
    
    try:
        from .models import ImportantDate
        
        if request.method == "POST":
            title = request.POST.get("title")
            date_value = request.POST.get("date")
            description = request.POST.get("description", "")
            is_recurring = request.POST.get("is_recurring") == "on"
            
            ImportantDate.objects.create(
                title=title,
                date=date_value,
                description=description,
                is_recurring=is_recurring,
                created_by=request.user
            )
            messages.success(request, "Important date added! 📅")
            return redirect("important_dates")
        
        all_dates = ImportantDate.objects.all()
        context = {"dates": all_dates}
    except Exception as e:
        context = {"dates": [], "error": str(e)}
    
    return render(request, "lovehub/important_dates.html", context)


@login_required(login_url="login")
def love_letters(request):
    if request.user.username not in ALLOWED_USERS:
        logout(request)
        return redirect("login")
    
    try:
        from .models import LoveLetter
        
        if request.method == "POST":
            title = request.POST.get("title")
            content = request.POST.get("content")
            emoji = request.POST.get("emoji", "💌")
            
            LoveLetter.objects.create(
                title=title,
                content=content,
                emoji=emoji,
                created_by=request.user
            )
            messages.success(request, "Love letter created! 💝")
            return redirect("love_letters")
        
        all_letters = LoveLetter.objects.all()
        context = {"letters": all_letters}
    except:
        context = {"letters": []}
    
    return render(request, "lovehub/love_letters.html", context)


def about(request):
    return render(request, "lovehub/about.html")


def logout_view(request):
    logout(request)
    messages.success(request, "See you soon! 💕")
    return redirect("login")


from django.http import HttpResponse
from django.contrib.auth.models import User

def check_users(request):
    """Temporary debug - DELETE AFTER CHECKING"""
    users = User.objects.all()
    output = f"<h1>Production Database Users</h1>"
    output += f"<p>Total users: {users.count()}</p><ul>"
    for user in users:
        output += f"<li><b>{user.username}</b> - Staff: {user.is_staff} - Superuser: {user.is_superuser}</li>"
    output += "</ul>"
    return HttpResponse(output)