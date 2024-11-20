
from django.shortcuts import render, redirect,reverse
from main.forms import KambingEntryForm
from main.models import KambingEntry
from django.http import HttpResponse , HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import JsonResponse
import json # Assignment 9
@csrf_exempt # Assignment 9
def create_kambing_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_product = KambingEntry.objects.create(
        user=request.user,
        name=data['name'],
        price=data['price'],
        description=data['description'],
        )
        new_product.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    


# Create your views here.
@login_required(login_url='/login')
def show_main(request):

    context = {
        'Nama_Aplikasi': 'KambingKu',
        'Name': request.user.username,
        "NPM" : "2306275821",
        'Class': 'PBP D',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_kambing_entry(request):
    form = KambingEntryForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        kambing_entry = form.save(commit=False)
        kambing_entry.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_kambing_entry.html", context)

@csrf_exempt
@require_POST
def add_kambing_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    user = request.user

    new_kambing = KambingEntry(
        name=name, description=description,
        price=price,
        user=user
    )
    new_kambing.save()

    return HttpResponse(b"CREATED", status=201)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_kambing(request, id):
    # Get kambing entry berdasarkan id
    kambing = KambingEntry.objects.get(pk = id)

    # Set kambing entry sebagai instance dari form
    form = KambingEntryForm(request.POST or None, instance=kambing)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_kambing.html", context)

def delete_kambing(request, id):
    # Get kambing berdasarkan id
    kambing = KambingEntry.objects.get(pk = id)
    # Hapus mood
    kambing.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = KambingEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = KambingEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = KambingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = KambingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")