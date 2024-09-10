from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Kambing_Master' : 'Malvin',
        'Role': 'Owner',
        'Class': 'S-Class'
    }

    return render(request, "main.html", context)