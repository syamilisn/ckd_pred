def main(sex,age,sc,wt):
    if sex == 'm' or sex == 'M':
        sex = 'm'
    if sex == 'f' or sex == 'F':
        sex = 'f'
    #CALCULATE GFR
    if sex == 'm':
        k = 79.6
        a = -0.411
    elif sex == 'f':
        k = 61.9
        a = -0.329    
    minimal = min((sc/k), 1)
    maximus = max((sc/k), 1)
    gfr_male  = 141 * (minimal ** a) * (maximus ** -1.209) * (0.993 ** age)
    gfr_female  = gfr_male  * 1.018 
    if sex == 'm':
        gfr = gfr_male 
    elif sex == 'f':
        gfr = gfr_female 
    #Determines the degree of renal failure by Glomerular Filtration Rate
    mark = '\n If the patient has GFR, which corresponds to stages I or II, but has no markers of kidney damage, the diagnosis of CKD is not established.'

    if sex == 'm' and age <= 40 and 100 <= gfr <= 130:
        disease = 'Normal GFR for patient under 40 years of age.'
    elif sex == 'm' and gfr > 130:
        disease = 'Increased GFR for patient.'
    elif sex == 'f' and gfr > 120:
        disease = 'Increased GFR for patient.'
    elif sex == 'f' and age <= 40 and 90 <= gfr <= 120:
        disease = 'Normal GFR for patient under 40 years of age.'
    elif gfr >= 90:
        disease = 'Normal or elevated GFR. CKD I stage.'
        disease += mark
    elif gfr >= 60:
        disease = 'Moderately reduced GFR. CKD stage II.'
        disease += mark
    elif gfr >= 30:
        disease = 'The average degree of reduction of GFR. Initial renal failure. CKD stage III.'
    elif gfr >= 15:
        disease = 'Significant reduction in GFR. Severe renal failure. CKD stage IV.'
    elif gfr < 15:
        disease = 'Terminal renal failure. CKD stage V. '
    return gfr, disease