# COMP 202 Assignment 4
# Name: Kayra Aker
# Student ID: 260837168


import doctest
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


class Patient:
    '''
    Define new class.
    >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
    >>> str(p) == '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t39.0'
    True
    >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
    >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40,0 C', '13')
    >>> p.update(p1)
    >>> str(p) == '0\\t42\\tF\\tH3Z\\t0\\tI\\t13\\t39.0;40.0'
    True
    '''
    def __init__(self, num, day_diagnosed, age, sex_gender, postal, state, temps, days_symptomatic):
        # number of the patient (int)
        self.num = int(num)
        # day into the pandemic on which they were diagnosed (int)
        self.day_diagnosed = int(day_diagnosed)
        # age of the patient (int)
        self.age = int(age)
        # sex/gender of the patient (M/F/X) (string)
        self.sex_gender = self.assign_gender(sex_gender)
        # first three characters of the patient's postal code (string)
        self.postal = self.assign_postal(postal)
        # state of the patient (I/R/D) (string)
        self.state = state
        # all the temperatures observed for this patient in Celsius (list of floats)
        self.temps = [self.assign_temps(temps)]
        # number of days the patient has been symptomatic (int)
        self.days_symptomatic = int(days_symptomatic)

    def assign_gender(self, sex_gender):
        gender = sex_gender[0].upper()
        gender_dict = {'M': 'MHB', 'F': 'FWG'}
        for key, options in gender_dict.items():
            if gender in options:
                return key
        return 'X'

    def assign_postal(self, postal):
        # if len(postal) < 3 or postal == 'N.A.':
        #     return '000'
        if postal[0] == 'H' and postal[1].isdigit() and postal[2].isalpha():
            return postal[:3]
        return '000'

    def assign_temps(self, temps):
        temps = temps.replace(',', '.').replace('°', '').replace(' ', '')
        new = ''
        for letter in temps:
            if not (letter.isalpha()):
                new += letter
        temps = float(new)
        if temps > 45:
            return (temps - 32) * 5 / 9
        else:
            return temps

    def __str__(self):
        '''
        (Patient) -> str
        '''
        fields = [self.num, self.age, self.sex_gender, self.postal, self.day_diagnosed, self.state, self.days_symptomatic]
        string = ''
        # concatenate fields as a string with the delimiter tab
        for field in fields:
            string += str(field) + '\t'
        # concatenate temperatures with the deimiter semi-colon, added to the above string
        for temp in self.temps:
            string += str(temp) + ';'
        # remove last ';' for lists as it seems to be expected in the example
        string = string[:-1]
        return string

    def update(self, patient):
        '''
        (Patient, Patient) -> ()
        '''
        # check if number, gender and postal code of patient match before updating patient record
        if patient.num == self.num and patient.sex_gender == self.sex_gender and patient.postal == self.postal:
            self.days_symptomatic = patient.days_symptomatic
            self.state = patient.state
            self.temps.append(patient.temps[0])
        # otherwise raise error
        else:
            raise AssertionError("Number, gender and postal code of patient must match.")


if __name__ == '__main__':
    doctest.testmod()