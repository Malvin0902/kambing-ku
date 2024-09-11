from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Nama_Aplikasi' : 'KambingKu',
        'Name': 'Malvin Muhammad Raqin',
        'Class': 'PBP D'
    }

    return render(request, "main.html", context)