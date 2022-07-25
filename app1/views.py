import csv
from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Measure
from .forms import MeasureForm, PredictForm
from .randomforest import randomforest_pred
from .calcGFRv2 import main
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
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
        #POST data is submitted, process data
        form = PredictForm(data = request.POST)
        if form.is_valid():
            #form.save(commit=False)
            #return redirect('app1:index')
            """Write func to use form here"""
            dict = form.cleaned_data
            list = [[x for x in dict.values()]]
            ip = [list[0][5:21]]    #input values
            result = randomforest_pred(ip)

            #part2: start
            name = list[0][0]
            age = list[0][1]
            wt = list [0][2]
            gender = list[0][3]
            sc = list[0][4]
            var, mssg = main(gender,age ,sc ,wt)
            #part2: stop
            temp = {'Name':name,'Result':result,'CKD-GFR':var,'Diagnosis': mssg}
            context = {'result':temp}
            return render(request,'app1/result.html',context)
    #display blank or invalid form
    context = {'form':form}
    return render(request,'app1/predict.html', context)
"""
def result(request):
    #measures = Measure.objects.order_by('id')
    #context = {'result':result.dict()}
    temp = {'result':'result'}
    context = {'result':'result'}
    return render(request, 'app1/result.html',context)
"""

def importcsv(request):
    path = 'app1\Datasets\ckd_clean_16_new.csv'
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Measure.objects.get_or_create(
                name = row[0],
                age = row[1],
                weight = row[2],
                gender = row[3],
                serum = row[4],
                sg = row[5],
                rbc = row[6],
                pc = row[7],
                pcc = row[8],
                ba = row[9],
                bgr = row[10],
                bu = row[11],
                pot = row[12],
                pcv = row[13],
                wbcc = row[14],
                rbcc = row[15],
                htn = row[16],
                dm = row[17],
                cad = row[18],
                pe = row[19],
                ane = row[20],
                yclass = row[21],
                )
    return HttpResponse('You have added data successfully.')

def renderpdf(template_src, context={}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type = 'application/ppdf')
    return None

data={
    "1":"oje",
    "2":"dfdf",
}

class Downloadpdf(View):
    def get(self,request, *args,**kwargs):
        pdf = renderpdf('app1/result.html',data)
        response =  HttpResponse(pdf,content_type= 'application/pdf')
        #filename = "demo_%s.pdf" %("report")
        #content = "attachment; filename = '%s'" %(filename)
        #response['Content-Disposition'] = content
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response
