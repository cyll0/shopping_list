from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Clayton Nagle',
        'class': 'PBD KKI'
    }

    return render(request, 'main.html', context)