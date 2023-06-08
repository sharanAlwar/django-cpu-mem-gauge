from django.shortcuts import render
import psutil

# Create your views here.
def main(request):
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None
    temp = {
        'cpu_metric':cpu_metric,
        'mem_metric':mem_metric
    }
    return render(request,'main.html',{'temp':temp})