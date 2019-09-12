import numpy as np
import brdffunc as b
np.seterr(divide='ignore', invalid='ignore')

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
    return (np.dot(half, normal))/(np.linalg.norm(half)*np.linalg.norm(normal))

def alpha(incident, view):
    return np.dot(incident, view)/(2*np.linalg.norm(incident)*np.linalg.norm((view)))

def deg2rad(degree):
    return degree * np.pi /180
