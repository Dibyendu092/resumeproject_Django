from django.shortcuts import render

# Create your views here.
def achivements(request):
    return render(request, 'achivements/achivements.html')

