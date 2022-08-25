import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf # Yahoo Finance stock data
import tkinter as tk
from metrics import * 
import pandas_datareader.data as web
import config

from setuptools import Command
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class main:
    root = tk.Tk()
    root.title('StockView')
    root.geometry('600x400')
    root.resizable(True, True)

    def get_stock():
        name = input("Which company would you like to analyze?")
        while True:
            if name.isupper() and name.isalpha():
                return name
            else:
                print('Please enter only uppercase letters!')

    name = get_stock()
    metrics.def_download(name)
        
    