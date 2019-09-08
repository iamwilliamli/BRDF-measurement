import numpy as np
import pandas as pd

def incident(theta_i, phi_i):
    return np.array([np.sin(theta_i)*np.cos(phi_i), np.sin(theta_i)*np.cos(phi_i),np.cos(phi_i)])

def view(theta_r, phi_r):
    return np.array([np.sin(theta_r)*np.cos(phi_r), np.sin(theta_r)*np.sin(phi_r), np.cos(theta_r)])

def normal():
    return np.array([0, 0, 1])

def half(theta_i, phi_i, theta_r, phi_r):
    return np.array([(np.sin(theta_i)*np.cos(phi_i)+np.sin(theta_r)*np.cos(phi_r))/2, (np.sin(theta_i)*np.sin(phi_i)+np.sin(theta_r)*np.sin(phi_r))/2, (np.cos(theta_i)+np.cos(theta_r))/2])

def normalize(array):
    normalized_v = array/np.linalg.norm(array)
    return normalized_v

def delta(half, normal):
    return np.dot(half, normal())/normalize(half)

def alpha(incident, view):
    return normalize(np.dot(incident, view))/2
