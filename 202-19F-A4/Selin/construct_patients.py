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
    if any(char in m for char in token) and not any(char in f for char in token):
        return m[0]
    elif any(char in f for char in token):
        return f[0]
    else:
        return 'X'
def validate_temp(token):
    didNumberStart =  False
    decimalPointCount= 0
    cleanTemp = []
    for char in token:
        if char.isdigit():
            didNumberStart=True
            cleanTemp.append(char)
        if char == '.' and didNumberStart and decimalPointCount == 0:
            decimalPointCount += 1
            cleanTemp.append(char)
    return ''.join(cleanTemp)
def toString(token, l):
    l.append(str(token))
    
class Patient:
    '''
    new class defined
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> (p.num == 0) and (p.age==42) and (p.sex_gender == 'F') and (p.day_diagnosed == 0) and (p.postal == 'H3Z') and (p.state == 'I') and (p.temps == [39.0]) and (p.days_symptomatic==12) 
        True
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40,0 C', '13')
        >>> p.update(p1)
        >>> (p.num == 0) and (p.age==42) and (p.sex_gender == 'F') and (p.day_diagnosed == 0) and (p.postal == 'H3Z') and (p.state == 'I') and (p.temps == [39.0, 40.0]) and (p.days_symptomatic==13) 
        True
        
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
        if not any(char.isdigit() for char in str(temp)):
            temperature = 0
        else:
            temperature = float(validate_temp(str(temp).replace(',', '.').replace(' ','').replace('C', '').replace('F','').replace('°','')))
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
    >>> p = stage_four('260823521_3.tsv', '260823521_4.tsv')
    >>> len(p)
    1912
    >>> p[0].equals(Patient(0, 5, 23, 'M', 'H4C', 'R', 37.25, 10))
    True
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
        if ln_lst[1] not in d.keys():
            d[int(ln_lst[1])] = p
            
        else:
            d[int(ln_lst[1])].update(p)
        output_file.write(str(p)+'\n')
    # close relevant files
    input_file.close()
    output_file.close()
    return d

def fatality_by_age(p_d):
    '''
    shows age vs. fatality_by_age
    >>> p = stage_four('260823521_3.tsv', '260823521_4.tsv')
    >>> fatality_by_age(p)
    [1.0, 1.0, 1.0, 1.0, 0.9782608695652174, 0.9615384615384616, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    
    '''
    #helper methods
    def round_to_5(num):
        return round(num/5.0) * 5
    def sort_by_age(tuple):
        return tuple[0]
    #initialize a (int ,(str, int) dict) dict by dictionary comprehension
    #inspired from python 3 documentation attached in the syllabus: 
    #https://docs.python.org/3/search.html?q=dictionary+comprehension&check_keywords=yes&area=default
    #the key for the outermost dictionary would be the age
    #the subdictionary will have ('D':dead counts), ('R': recover counts)
    
    dead_vs_recover_by_age = {5*i:{'D':0, 'R':0} for i in np.arange(20)}
    dead_or_recovered = {x:x for x in ['D', 'R']} 
    dead_or_recovered['I'] = None
    
    for patient in p_d.values():
        state_verified = dead_or_recovered[patient.state]
        if state_verified:
            dead_vs_recover_by_age[round_to_5(patient.age)][state_verified] += 1.0
    age_probs = []
    for age, counts in dead_vs_recover_by_age.items():
        if counts['D'] + counts['R'] > 0:
            prob = counts['D'] / (counts['D'] + counts['R'])
        else:
            prob = 0
        age_probs.append((age, prob))

    age_probs.sort(key=sort_by_age) 
    fig, ax = plt.subplots()
    ax.plot([age for age, prob in age_probs], [prob for age, prob in age_probs])
    ax.set(xlabel = 'Age', ylabel = 'Deaths / (Deaths+Recoveries)',title = 'Probability of death vs. Age by Selin Cataltepe')
    plt.ylim((0, 1.2))
    plt.savefig('fatality_by_age.png')

    return [prob for age, prob in age_probs]
            
if __name__ == '__main__':
    doctest.testmod()
        
    
    
    
    
    