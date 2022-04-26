import sys
def GFR(sexip, ageip, scrip, wtip):
    global sex, age, scr, weight, patient_sex
    sex = sexip
    age = ageip
    scr = scrip
    weight = wtip
    if sex == 'm':
        patient_sex = 'male'
    elif sex == 'f':
        patient_sex = 'female'
    print(age)


#var = GFR('m', 12, 2, 40)

def age_checker(age):
    if age <0:
        print('INCORRECT DATATYPE.')
        sys.exit(1)
    elif age <= 2:
        print('\n The patient\'s age is too young. Use inulin clearance to determine GFR!')
        sys.exit(1)
    elif age <= 18:
        print('\n Be careful! Data on GFR may be inaccurate due to the patient\'s age.')

def ckd_epi(age, weight, creatinine):
    men = ((140 - age) * 1.23 * weight) / creatinine
    print('CKD-EPI: {}'.format(men))



def gfr_count(scr, age):
    if sex == 'm':
        k = 79.6
        α = -0.411
    elif sex == 'f':
        k = 61.9
        α = -0.329
    
    minimal = min((scr/k), 1)
    maximus = max((scr/k), 1)

    gfr_male  = 141 * (minimal ** α) * (maximus ** -1.209) * (0.993 ** age)
    
    gfr_female  = gfr_male  * 1.018

    

    if sex == 'm':
        gfr = gfr_male 
    elif sex == 'f':
        gfr = gfr_female 

    return gfr

def renal_failure(gfr):
    '''Determines the degree of renal failure by Glomerular Filtration Rate '''

    mark = '\n If the patient has GFR, which corresponds to stages I or II, but has no markers of kidney damage, the diagnosis of CKD is not established.'

    if sex == 'm' and age <= 40 and 100 <= gfr <= 130:
        disease = 'Normal GFR for men under 40 years of age.'
    elif sex == 'm' and gfr > 130:
        disease = 'Increased GFR for males.'
    elif sex == 'f' and gfr > 120:
        disease = 'Increased GFR for women.'
    elif sex == 'f' and age <= 40 and 90 <= gfr <= 120:
        disease = 'Normal GFR for women under 40 years of age.'
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

    return disease

def main(sexip, ageip, scrip, wtip):
    GFR(sexip, ageip, scrip, wtip)
    age_checker(age)
    #except:
    gfr_count(scr, age)
    print('Your patient: \n', 'Sex: {}'.format(patient_sex),
    'Age: {} years'.format(age), 
    'Serum creatinine: {} μmol/L \n'.format(scr), 
    'CKD-EPI is: {}'.format(gfr_count(scr, age)), sep='\n')

    #print(renal_failure(gfr_count(scr, age)))
    return gfr_count(scr, age),renal_failure(gfr_count(scr, age))

if __name__ == "__main__":
    main('m', 65, 120, 70)
    #print('finale',var)