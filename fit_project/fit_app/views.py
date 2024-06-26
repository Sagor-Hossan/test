from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date, timedelta, datetime

# Create your views here.

def signin(r):
    if r.method=='POST':
        username = r.POST['username']
        password = r.POST['password']

        user = authenticate(username=username,password=password)
        if user:
            login(r,user)
            return redirect('home')

    return render(r,'register/signin.html')

def signup(r):
    if r.method=='POST':
        name = r.POST['name']
        username = r.POST['username']
        password = r.POST['password']
        gender = r.POST['gender']
        dob = r.POST['dob']
        height = r.POST['height']
        weight = r.POST['weight']
        goal = r.POST['goal']
        profile_pic = r.FILES['profile_pic']

        user = customUser.objects.create_user(
            username=username,
            password=password,
            name=name,
            gender=gender,
            dob=dob,
            height=height,
            weight=weight,
            goal=goal,
            profile_pic=profile_pic)
        user.save()
        
        if user:
            login(r,user)
            return redirect('home')
    
    return render(r,'register/signup.html')

def signout(r):
    logout(r)
    return redirect('signin')

@login_required
def home(r):
    
    return render(r,'common/home.html')


@login_required
def profilepage(r):
    user = customUser.objects.get(id=r.user.id)
    return render(r,'profile/profilepage.html',{'user':user})


@login_required
def addFood(r):
    if r.method=='POST':
        food_name = r.POST['food_name']
        calories = r.POST['calories']
        image = r.FILES['image']

        food = foodModel(user=r.user,food_name=food_name,calories=calories,image=image)
        food.save()
        return redirect('viewFood')

    return render(r,'foods_by_user/addFood.html')

@login_required
def viewFood(r):
    foods = foodModel.objects.filter(user=r.user)
    return render(r,'foods_by_user/viewFood.html',{'foods':foods})

@login_required
def editFood(r,id):
    food = foodModel.objects.get(id=id)
    if r.method=='POST':
        food.food_name = r.POST['food_name']
        food.calories = r.POST['calories']

        image = r.FILES.get('image')
        if image:
            food.image = image
        else:
            image1 = r.POST.get('image1')
            if image1:
                food.image = image1

        food.save()
        return redirect('viewFood')

    return render(r,'foods_by_user/editFood.html',{'food':food})

@login_required
def deleteFood(r,id):
    food = foodModel.objects.get(id=id)
    food.delete()
    return redirect('viewFood')

def userAge(r):
    today = date.today()
    age = today.year - r.user.dob.year - ((today.month, today.day) < (r.user.dob.month, r.user.dob.day))
    return age

def userBMR(r):
    user = r.user
    age = userAge(r)
    if user.gender == 'male':
        bmr = 66.47 + (13.75 * user.weight) + (5.003 * user.height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.563 * user.weight) + (1.850 * user.height) - (4.676 * age)
    return bmr

def today_consumed(r):
    consumed = ConsumedCalories.objects.filter(user=r.user, date=date.today())
    return consumed

def today_calories(r):
    consumed = ConsumedCalories.objects.filter(user=r.user, date=date.today())
    calSum = sum(c.calorie_consumed for c in consumed)
    return calSum

@login_required
def addConsumedCalories(r):
    if r.method=='POST':
        item_name = r.POST['item_name']
        calorie_consumed = float(r.POST['calorie_consumed'])

        consumed = ConsumedCalories(user=r.user,item_name=item_name,calorie_consumed=calorie_consumed)
        consumed.save()
        return redirect('viewConsumedCalories')
    return render(r,'calories/addConsumedCalories.html')

@login_required
def viewConsumedCalories(r):
    bmr = userBMR(r)
    consumed = today_consumed(r)
    calSum = today_calories(r)

    return render(r, 'calories/viewConsumedCalories.html', {'consumed': consumed, 'bmr': bmr, 'calSum': calSum})

# @login_required
# def calories_by_date(r):
    # specific_date = r.GET.get('specific_date')
    # total_calories = ConsumedCalories.get_total_calories_by_date(r.user, specific_date)
    # return render(r, 'calories/calories_by_date.html', {'total_calories': total_calories})

# @login_required
# def total_calories(r):
#     total_calories = ConsumedCalories.objects.filter(user=r.user).aggregate(Sum('calorie_consumed'))
#     return render(r,'calories/total_calories.html',{'total_calories':total_calories['calorie_consumed__sum']})


@login_required
def restaurantListPage(request):
    return render(request, 'foods/restaurantList.html')

@login_required
def gymPage(request):
    return render(request, 'fitness/gym.html')

@login_required
def exercisePage(request):
    return render(request, 'fitness/exercise.html')

@login_required
def restOrSleepPage(request):
    return render(request, 'fitness/restOrSleep.html')


