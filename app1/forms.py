from dataclasses import field
from django import forms
from . models import Measure
class MeasureForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ['name','age','gender','serum','sg','rbc','pc','pcc','ba','bgr','bu','pot','pcv','wbcc','rbcc','htn','dm','cad','pe','ane','yclass']
        
        labels = {
            'name':'Name',
            'age':'Age (years)',
            'gender':'Gender (M/F)',
            'serum':'Serum Creatinine (μmol/L)',
            'sg':'Specific Gravity (1.005,1.010,1.015,1.020.1.025)',
            'rbc':'Red Blood Cells (Normal:1, abnormal:0)',
            'pc':'Pus Cell (Normal:1, abnormal:0)',
            'pcc':'Pus Cell Clumps (Present:1, Not present:0)',
            'ba':'Bacteria (Present:1, Not present:0)',
            'bgr':'Blood Glucose Random (mgs/dl)',
            'bu':'Blood Urea (mgs/dl)',
            'pot':'Potassium (mEq/L)',
            'pcv':'Packed Cell Volume (numerical)',
            'wbcc':'White Blood Cells Count (cells/cumm)',
            'rbcc':'Red Blood Cells Count (millions/cumm)',
            'htn':'Hypertension (yes:1, no:2)',
            'dm':'Diabetes Mellitus (yes:1, no:2)',
            'cad':'Coronary Artery Disease (yes:1, no:2)',
            'pe':'Pedal Edema (yes:1, no:2)',
            'ane':'Anemia (yes:1, no:2)',
            'yclass':'Patient Condition (ckd/ notckd)'
        }