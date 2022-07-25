import pandas as pd
import datetime

from setuptools import Command
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
import tkinter as tk
from tkinter import ttk
from tkinker.messagebox import showinfo

from metrics import *

class main:
    root = tk.Tk()
    root.title('StockView')
    root.geometry('300x200')
    root.resizable(True, True)

    shouldIButton = ttk.Button(root, text="Decision", command=recommendation)

    
        name = input("Which company would you like to analyze?")
        if name.isupper() and name.isalpha():
            break
        else:
            print('Please enter only uppercase letters!')
    
    