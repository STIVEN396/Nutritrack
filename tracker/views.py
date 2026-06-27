from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum
from datetime import date
from .models import FoodEntry

DAILY_GOAL = 2000  # kcal goal

@login_required
def dashboard(request):
    today = date.today()
    entries = FoodEntry.objects.filter(user=request.user, date=today)

    totals = entries.aggregate(
        cal=Sum('calories'), pro=Sum('protein'),
        car=Sum('carbs'), fat=Sum('fat')
    )
    cal_total  = totals['cal'] or 0
    pro_total  = totals['pro'] or 0
    car_total  = totals['car'] or 0
    fat_total  = totals['fat'] or 0

    cal_pct  = min(int(cal_total / DAILY_GOAL * 100), 999)
    pro_goal = 150  # g
    car_goal = 250  # g
    fat_goal = 65   # g
    pro_pct  = min(int(pro_total / pro_goal * 100), 999)
    car_pct  = min(int(car_total / car_goal * 100), 999)
    fat_pct  = min(int(fat_total / fat_goal * 100), 999)

    return render(request, 'tracker/dashboard.html', {
        'entries': entries,
        'cal_total': cal_total,  'cal_pct': cal_pct,
        'pro_total': round(pro_total, 1), 'pro_pct': pro_pct,
        'car_total': round(car_total, 1), 'car_pct': car_pct,
        'fat_total': round(fat_total, 1), 'fat_pct': fat_pct,
        'daily_goal': DAILY_GOAL,
        'remaining': max(DAILY_GOAL - cal_total, 0),
        'today': today,
    })

@login_required
def add_entry(request):
    if request.method == 'POST':
        name     = request.POST.get('name', '').strip()
        calories = request.POST.get('calories', 0)
        protein  = request.POST.get('protein', 0)
        carbs    = request.POST.get('carbs', 0)
        fat      = request.POST.get('fat', 0)
        if name and calories:
            FoodEntry.objects.create(
                user=request.user, name=name,
                calories=int(calories), protein=float(protein),
                carbs=float(carbs), fat=float(fat)
            )
            messages.success(request, f'"{name}" added successfully!')
        return redirect('dashboard')
    return redirect('dashboard')

@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(FoodEntry, pk=pk, user=request.user)
    entry.delete()
    messages.success(request, 'Entry deleted.')
    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})