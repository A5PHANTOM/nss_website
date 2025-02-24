from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Program, ProgramPhoto, MoreProgramPhoto
from .forms import ProgramForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Only allow staff users
            login(request, user)
            return redirect("admin_dashboard")  # Redirect to dashboard
        else:
            messages.error(request, "Invalid credentials or not an admin!")
    
    return render(request, "admin_login.html")

@login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")  # Create a dashboard page

def programs(request):
    all_programs = Program.objects.all()  # Fetch all programs
    return render(request, 'programs/program_list.html', {'programs': all_programs})

def volunteers(request):
    return render(request, "volunteers.html")

def program_list(request):
    programs = Program.objects.all()  # Fetch all programs
    return render(request, 'programs/program_list.html', {'programs': programs})

def add_program(request):
    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES)
        photos = request.FILES.getlist('photos')  # ✅ Correct field name
        more_photos = request.FILES.getlist('more_photos')  # ✅ Correct field name

        if form.is_valid():
            program = form.save()  # ✅ Save Program first

            # ✅ Save Photos
            for photo in photos:
                ProgramPhoto.objects.create(program=program, image=photo)

            # ✅ Save More Photos
            for photo in more_photos:
                MoreProgramPhoto.objects.create(program=program, image=photo)

            return redirect('programs')  # Redirect to program list after saving

    else:
        form = ProgramForm()
    
    return render(request, 'programs/add_program.html', {'form': form})

def modify_program(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect('programs')
    else:
        form = ProgramForm(instance=program)
    return render(request, 'programs/modify_program.html', {'form': form})

def remove_program(request, pk):
    program = Program.objects.filter(pk=pk).first()  # Avoid 404 error
    if not program:
        messages.error(request, "The selected program does not exist.")
        return redirect('programs')

    program.delete()
    messages.success(request, "Program deleted successfully.")
    return redirect('programs')


def view_program(request, pk):
    program = get_object_or_404(Program, pk=pk)
    photos = ProgramPhoto.objects.filter(program=program)  # Get all program photos
    more_photos = MoreProgramPhoto.objects.filter(program=program)  # Get all more program photos

    context = {
        'program': program,
        'photos': photos,
        'more_photos': more_photos
    }
    return render(request, 'programs/view_program.html', context)

def admin_programs(request):
    programs = Program.objects.all()
    return render(request, 'admin_programs.html', {'programs': programs})

def delete_program_photo(request, photo_id):
    photo = get_object_or_404(ProgramPhoto, id=photo_id)
    photo.delete()
    return redirect(request.META.get("HTTP_REFERER", "programs"))

def delete_more_program_photo(request, photo_id):
    photo = get_object_or_404(MoreProgramPhoto, id=photo_id)
    photo.delete()
    return redirect(request.META.get("HTTP_REFERER", "programs"))

def events(request):
    programs = Program.objects.all()  # Fetch all programs
    return render(request, "events.html", {"programs": programs})

def home(request):
    latest_programs = Program.objects.order_by('-id')[:3]  # Fetch latest 3 programs
    return render(request, "home.html", {"latest_programs": latest_programs})