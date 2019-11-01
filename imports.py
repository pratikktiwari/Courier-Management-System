#all ok
#import numpy as np
#import pandas as pd
from tkinter import *
from tkinter import messagebox
from db_func import *
import time
import random
import string
from datetime import datetime
from dateutil import tz
import time

#from tkinter import ttk 

def rand_num_generator():
    return random.randint(11111,99999)

def rand_str_generator():
    N=5
    res = ''.join(random.choices(string.ascii_uppercase+string.digits, k = N))
    return res

def check_captcha(orginal,entered):
    if orginal==entered:
        return True
    else:
        return False


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset
def convert_timestamp(pro_time):
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        # utc = datetime.utcnow()
        utc = datetime.strptime(pro_time, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        # Convert time zone
        central = utc.astimezone(to_zone)
        return central
