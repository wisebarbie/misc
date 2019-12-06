# COMP 202: A4
# NAME: Chin Yiap Ong
# ID: 260823566

import doctest
import numpy as np
import matplotlib.pyplot as plt

#helper 
#helper function to clean up status
def correct_status(token):
    if 'I' in token:
        return 'I'
    if 'M' in token or 'D' in token:
        return 'D'
    if 'R' in token:
        return 'R'
def summarize_gender(token):
    m = ['M', 'H', 'B']
    f = ['F', 'G', 'W']
    n = ['N']
    
    if any(char in m for char in token) and not any(char in f for char in token) and not any(char in n for char in token):
        return m[0]
    elif any(char in f for char in token):
        return f[0]
    else:
        return 'X'
def verify_temp(token):
    do_we_have_num =  False
    period_is_there= 0
    cleanTemp = []
    for char in token:
        if char.isdigit():
            do_we_have_num=True
            cleanTemp.append(char)
        if char == '.' and do_we_have_num and period_is_there == 0:
            period_is_there += 1
            cleanTemp.append(char)
    return ''.join(cleanTemp)
def add_as_str(token, l):
    l.append(str(token))
def from_fahrenheit_to_celsius(f):
     if f > 45 :
            f = round((5.0/9)*(f-32), 2)
     return f
    
class Patient:
    '''
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> (p.num == 0) and (p.age==42) and (p.sex_gender == 'F') and (p.day_diagnosed == 0) and (p.postal == 'H3Z') and (p.state == 'I') and (p.temps == [39.0]) and (p.days_symptomatic==12) 
        True
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40,0 C', '13')
        >>> p.update(p1)
        >>> (p.num == 0) and (p.age==42) and (p.sex_gender == 'F') and (p.day_diagnosed == 0) and (p.postal == 'H3Z') and (p.state == 'I') and (p.temps == [39.0, 40.0]) and (p.days_symptomatic==13) 
        True
        >>> str(p) == '0\\t42\\tF\\tH3Z\\t0\\tI\\t13\\t39.0;40.0'
        True
        
    '''
    #constructor
    def __init__(self, num, fateful_day, age, gender, postal_code, state, temp, lonely_sad_days):
        #self.num: the number of the patient, an int
        self.num = int(num)
        #self.age: the age of the patient, an int
        self.age = int(age)
        #self.sex_gender: the sex/gender of the patient, a string that is either M, F or X
        self.sex_gender = summarize_gender(gender)
        #self.postal: the 1st three characters of the patient's postal code, a string
        self.postal = postal_code[:3]
        #self.day diagnosed: which day into the pandemic they were diagnosed, an int
        self.day_diagnosed = int(fateful_day)
        #self.state: the state of the patient. Assume the input will be one of I, R or D.
        self.state = correct_status(state)
        
        self.temps = []
        if not any(char.isdigit() for char in str(temp)):
            temperature = 0
        else:
            temperature = float(verify_temp(str(temp).replace(',', '.').replace(' ','').replace('C', '').replace('F','').replace('°','')))
        temperature = from_fahrenheit_to_celsius(temperature)
        self.temps.append(temperature)
        self.days_symptomatic = int(lonely_sad_days)
    
    def __str__(self):
        l = []
        add_as_str(self.num, l)
        add_as_str(self.age, l)
        add_as_str(self.sex_gender, l)
        add_as_str(self.postal, l)
        add_as_str(self.day_diagnosed, l)
        add_as_str(self.state, l)
        add_as_str(self.days_symptomatic, l)
        sublist = []
        for f in self.temps:
            add_as_str(f, sublist)
        l.append(';'.join(sublist))
        
        return '\t'.join(l)
    
    def is_same(self, am_i_not_alone):
        return (self.num == am_i_not_alone.num) and (self.sex_gender == am_i_not_alone.sex_gender) and (self.postal == am_i_not_alone.postal) 
    
    def update(self, am_i_not_alone):
        if(self.is_same(am_i_not_alone)):
            self.days_symptomatic = am_i_not_alone.days_symptomatic
            self.state = am_i_not_alone.state
            self.temps.extend(am_i_not_alone.temps)
        else:
            raise AssertionError('The patient has a different number/gender/postal code')

def stage_four(input_filename, output_filename):
    '''
    >>> p = stage_four('260823566_3.tsv', '260823566_4.tsv')
    >>> len(p)
    1880
    '''
    # open input files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
     # store lines from input_filename as a list
    input_lines = input_file.readlines()
    d = {}
    for line in input_lines:
        l_l = line.split('\t')
        p = Patient(l_l[1], l_l[2], l_l[3], l_l[4], l_l[5], l_l[6], l_l[7], l_l[8])
        if l_l[1] not in d.keys():
            d[int(l_l[1])] = p
            
        else:
            d[int(l_l[1])].update(p)
        output_file.write(str(p)+'\n')
    # close relevant files
    input_file.close()
    output_file.close()
    return d

def fatality_by_age(p_d):
    '''
    shows age vs. fatality_by_age
    >>> p = stage_four('260823566_3.tsv', '260823566_4.tsv')
    >>> fatality_by_age(p)
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9787234042553191, 0.96875, 0.96, 1.0, 1.0, 1.0, 1.0, 1.0, 0, 0]
    '''
    #helper methods
    def to_nearest_five(num):
        return round(num/5.0) * 5
    def sort_by_age(tuple):
        return tuple[0]
    
    grouped_by_age = {}
    for i in range(20):
        grouped_by_age[5*i] = {'D':0, 'R':0} 
    groups = {} 
    for x in ['D', 'R']:
        groups[x] = x
    groups['I'] = None
    
    for patient in p_d.values():
        state_verified = groups[patient.state]
        if state_verified:
            grouped_by_age[to_nearest_five(patient.age)][state_verified] += 1.0
    age_probs = []
    for age, counts in grouped_by_age.items():
        if counts['D'] + counts['R'] > 0:
            prob = counts['D'] / (counts['D'] + counts['R'])
        else:
            prob = 0
        age_probs.append((age, prob))

    age_probs.sort(key=sort_by_age) 
    fig, ax = plt.subplots()
    AGE = []
    PROB = []
    for age, prob in age_probs:
        AGE.append(age)
        PROB.append(prob)
    ax.plot(AGE, PROB)
    ax.set(xlabel = 'Age', ylabel = 'Deaths / (Deaths+Recoveries)',title = 'Probability of death vs. Age')
    plt.ylim((0, 1.2))
    plt.savefig('fatality_by_age.png')

    return PROB
            
if __name__ == '__main__':
    doctest.testmod()
        
    
    
    
    
    