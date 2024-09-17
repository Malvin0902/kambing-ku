
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import KambingEntryForm
from main.models import KambingEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    kambing_entries = KambingEntry.objects.all()

    context = {
        'Nama_Aplikasi': 'KambingKu',
        'Name': 'Malvin Muhammad Raqin',
        'Class': 'PBP D',
        'kambing_entries': kambing_entries
    }

    return render(request, "main.html", context)

def create_kambing_entry(request):
    form = KambingEntryForm(request.POST or None)
    

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_kambing_entry.html", context)

def show_xml(request):
    data = KambingEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = KambingEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = KambingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = KambingEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")