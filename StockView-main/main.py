import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
import tkinter

from metrics import *

class main:
    while True:
        name = input("Which company would you like to analyze?")
        if name.isupper() and name.isalpha():
            break
        else:
            print('Please enter only uppercase letters!')
    