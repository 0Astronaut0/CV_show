from .models import inp_data
from django.shortcuts import render


def showcv_view(request):
    data = inp_data.objects.first()
    return render(request,'home.html',{'data':data})
