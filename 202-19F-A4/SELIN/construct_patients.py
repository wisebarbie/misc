import doctest
import numpy as np
import matplotlib.pyplot as plt
#helper 
    #helper function to clean up status
def clean_status(token):
    possible_status = {'I':'I', 'M':'D', 'R':'R', 'D':'D'}
    for status in possible_status.keys():
        if status in token.upper():
            return possible_status[status]
def clean_gender(token):
    m = ['M', 'H', 'B']
    f = ['F', 'G', 'W']
    if any(char in m for char in token):
        return m[0]
    elif any(char in f for char in token):
        return f[0]
    else:
        return 'X'
def toString(token, l):
    l.append(str(token))
    
class Patient:
    '''
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> print(str(p))
        0 42 F H3Z 0 I 12 39.0
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40,0 C', '13')
        >>> p.update(p1)
        >>> print(str(p))
        0 42 F H3Z 0 I 13 39.0;40.0
    '''
    #constructor
    def __init__(self, num, d_d, age, s_g, postal, state, temp, d_s):
        #self.num: the number of the patient, an int
        self.num = int(num)
        #self.age: the age of the patient, an int
        self.age = int(age)
        #self.sex_gender: the sex/gender of the patient, a string that is either M, F or X
        self.sex_gender = clean_gender(s_g)
        #self.postal: the 1st three characters of the patient's postal code, a string
        self.postal = postal[:3]
        #self.day diagnosed: which day into the pandemic they were diagnosed, an int
        self.day_diagnosed = int(d_d)
        #self.state: the state of the patient. Assume the input will be one of I, R or D.
        self.state = clean_status(state)
        self.temps = []
        if not any(char.isdigit() for char in temp):
            temperature = 0
        else:
            temperature = float(temp.replace(',', '.').replace(' ','').replace('C', '').replace('F',''))
        if temperature > 45 :
            temperature = round((5.0/9)*(temperature-32), 2)
        self.temps.append(temperature)
        self.days_symptomatic = int(d_s)
    
    def __str__(self):
        l = []
        toString(self.num, l)
        toString(self.age, l)
        toString(self.sex_gender, l)
        toString(self.postal, l)
        toString(self.day_diagnosed, l)
        toString(self.state, l)
        toString(self.days_symptomatic, l)
        l.append(';'.join([str(f) for f in self.temps]))
        
        return '\t'.join(l)
    
    def equals(self, another_patient):
        return (self.num == another_patient.num) and (self.sex_gender == another_patient.sex_gender) and (self.postal == another_patient.postal) 
    
    def update(self, another_patient):
        if(self.equals(another_patient)):
            self.days_symptomatic = another_patient.days_symptomatic
            self.state = another_patient.state
            self.temps.extend(another_patient.temps)
        else:
            raise AssertionError('The patient has a different number/gender/postal code')

def stage_four(input_filename, output_filename):
    '''
    >>> p = stage_four('stage3.tsv', 'stage4.tsv')
    >>> len(p)
    1716
    >>> print(str(p[0]))
    0 42 F H3Z 0 I 12 40.0;39.13;39.45;39.5;39.36;39.2;39.0;39.04;38.82;37.7

    '''
    # open input files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
     # store lines from input_filename as a list
    input_lines = input_file.readlines()
    d = {}
    for line in input_lines:
        ln_lst = line.split('\t')
        p = Patient(ln_lst[1], ln_lst[2], ln_lst[3], ln_lst[4], ln_lst[5], ln_lst[6], ln_lst[7], ln_lst[8])
        d[int(ln_lst[1])] = p
        output_file.write(str(p))
    # close relevant files
    input_file.close()
    output_file.close()
    return d

    
    