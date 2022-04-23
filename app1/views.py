import csv
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Measure
from .forms import MeasureForm, PredictForm
from .randomforest import randomforest_pred

def index(request):
    measures = Measure.objects.order_by('id')
    context = {'measures':measures}
    return render(request, 'app1/index.html',context)

def input(request):
    """Take user input"""
    if request.method != 'POST':
        #no data submitted, return blank form
        form = MeasureForm()
    else:
        #POST data is submittes, process data
        form = MeasureForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:index')
    #display blank or invalid form
    context = {'form':form}
    return render(request,'app1/input.html', context)

def export(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['name','age','gender','serum','sg','rbc','pc','pcc','ba','bgr','bu','pot','pcv','wbcc','rbcc','htn','dm','cad','pe','ane','yclass'])
    for row in Measure.objects.all().values_list('name','age','gender','serum','sg','rbc','pc','pcc','ba','bgr','bu','pot','pcv','wbcc','rbcc','htn','dm','cad','pe','ane','yclass'):
        writer.writerow(row)
    response['Content-Disposition'] = 'attachment; filename="values.csv"'
    return response

def dataset(request):
    measures = Measure.objects.order_by('id')
    context = {'measures':measures}
    return render(request, 'app1/dataset.html',context)

def predict(request):
    """Take user input for prediction"""
    if request.method != 'POST':
        #no data submitted, return blank form
        form = PredictForm()
    else:
        #POST data is submittes, process data
        form = PredictForm(data = request.POST)
        if form.is_valid():
            #form.save(commit=False)
            #return redirect('app1:index')
            """Write func to use form here"""
            dict = form.cleaned_data
            list = [[x for x in dict.values()]]
            ip = [list[0][4:20]]    #input values
            result = randomforest_pred(ip)
            return HttpResponse(f'The patient is {result}')
    #display blank or invalid form
    context = {'form':form}
    return render(request,'app1/predict.html', context)