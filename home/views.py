
import profile
from unicodedata import name
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, ProfileForm
import math
# Create your views here.


@login_required(login_url='login')
def home(request):
    profile = Profile.objects.filter(username=request.user.username).first()
    expenses = Expense.objects.filter(username=request.user.username)
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get("expense_type")
        expense = Expense(name=text, amount=amount,
                          expense_type=expense_type, username=request.user.username)
        expense.save()
        profile = Profile(username=request.user.username)
        if expense_type == "Positive":
            profile.balance += float(amount)
            profile.income += float(amount)
        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)
        profile.save()
        return redirect('home')
    context = {'profile': profile, 'expenses': expenses}
    return render(request, "index.html", context)


@login_required(login_url='login')
def home1(request):
    profile = Profile.objects.filter(username=request.user.username).first()
    expenses = Expense.objects.filter(username=request.user.username)
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get("expense_type")
        expense = Expense(name=text, amount=amount,
                          expense_type=expense_type, username=request.user.username)
        expense.save()
        # profile = Profile(username=request.user.username)
        if expense_type == "Positive":
            profile.balance += float(amount)
            profile.income += float(amount)
        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)
        profile.save()
        return redirect('home')

    context = {'profile': profile, 'expenses': expenses}
    return render(request, "index.html", context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def update(request):

    profile = Profile.objects.filter(username=request.user.username).first()

    # profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            income = form.cleaned_data.get('income')
            expense = form.cleaned_data.get('expenses')
            balance = income-expense
            profile = Profile(income=income, expenses=expense, balance=balance)

            profile.save()
            print(balance)
            form.save()
            return redirect('/home')

    context = {'form': form}
    return render(request, 'update_form.html', context)


@login_required(login_url='login')
def delete(request):
    profile = Profile.objects.all()
    if request.method == "POST":
        profile.delete()
        return redirect('/')

    context = {'item': profile}
    return render(request, 'delete.html', context)


# def edit(request, slug):
#     profile = get_object_or_404(Profile, slug=slug)
#     if request.method == "POST":
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.username = request.user.username
#             profile.save()
#             return redirect("/home")
