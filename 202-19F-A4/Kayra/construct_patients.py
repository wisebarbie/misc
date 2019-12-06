# COMP 202 Assignment 4
# Name: Kayra Aker
# Student ID: 260837168


import doctest
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


class Patient:
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
        # state of the patient (I/R/D)
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

