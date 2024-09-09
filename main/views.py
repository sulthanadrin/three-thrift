from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : '3Thrift',
        'name': 'Sulthan Adrin Pasha Siregar',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
