from scipy.optimize import curve_fit
import pandas as pd

def model(x,m,b):
    return m*x+b

