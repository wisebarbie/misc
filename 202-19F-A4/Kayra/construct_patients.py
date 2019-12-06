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
    >>> str(p)
    '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t39.0'
    >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
    >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40,0 C', '13')
    >>> p.update(p1)
    >>> str(p)
    '0\\t42\\tF\\tH3Z\\t0\\tI\\t13\\t39.0;40.0'
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
        sex_gender = sex_gender.upper()
        gender_dict = {
            'M': ['M','MALE','H','HOMME','MAN','BOY'], 
            'F': ['F','FEMALE','FEMME','WOMAN','GIRL']
        }
        for key, options in gender_dict.items():
            if sex_gender in options:
                return key
        return 'X'

    def assign_postal(self, postal):
        if len(postal) >= 3 and postal[0] == 'H' and postal[1].isdigit() and postal[2].isalpha():
            return postal[:3]
        return '000'

    def assign_temps(self, temps):
        if temps == 'N.A.':
            return 0
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
            print(patient.num, self.num)
            print(patient.sex_gender, self.sex_gender)
            #raise AssertionError("Number, gender and postal code of patient must match.")


def stage_four(input_filename, output_filename):
    '''
    (str, str) -> dict
    Read input_filename.
    Create a new Patient object for each line.
    Keep and return a dictionary, where:
        - the keys are the patient's number (int)
        - the values are the Patient objects
    Update the Patient object for existing entires rather than overwriting it.
    Write to output_filename, every Patient converted to a string, sorted by patient number.
    >>> p = stage_four('example_3.tsv', 'example_4.tsv')
    >>> len(p)
    3
    >>> str(p[0])
    '0\\t42\\tF\\tH3Z\\t0\\tI\\t4\\t40.0;39.13'
    >>> p = stage_four('260837168_3.tsv', '260837168_4.tsv')
    >>> len(p)
    1725
    >>> str(p[0])
    '0\\t20\\tM\\tH3C\\t0\\tI\\t10\\t38.4;38.0;37.1;38.0;35.0;34.26;36.45;34.7;34.6;37.35'
    '''
    # open relevant files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store lines from input_filename as a list
    input_lines = input_file.readlines()
    # initialize dictionary
    patient_dict = {}
    # do for all lines
    for line in input_lines:
        # split line by delimiter into list
        line_list = line.split('\t')
        # create new patient object
        new_patient = Patient(
            line_list[1], line_list[2], line_list[3], line_list[4], 
            line_list[5], line_list[6], line_list[7], line_list[8]
        )
        # update patient dictionary
        if int(line_list[1]) in patient_dict:
            patient_dict[int(line_list[1])].update(new_patient)
        else:
            patient_dict[int(line_list[1])] = new_patient
    # write contents of patient dictionary into output_filename
    for _, value in sorted(patient_dict.items()):
        output_file.write(str(value) + '\n')
    # close relevant files
    input_file.close()
    output_file.close()
    # return patient dictionary
    return patient_dict


if __name__ == '__main__':
    doctest.testmod()