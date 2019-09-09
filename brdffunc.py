import matplotlib.pyplot as plt
import numpy as np


#import matplotlib.pyplot as plt
# 引用自CSDN

def TorranceSparrow_D(roughness, theta):
    c = 1
    return c * np.exp(-np.power(theta/roughness, 2))

def Phong_D(roughness, theta):
    return (roughness + 2)/(2*np.pi)*np.power(np.cos(theta), roughness)


# Beckmann D分布，from cook paper, ggx paper
def Beckmann_D(roughness, delta):
    cos_theta = np.cos(delta)
    tan_theta = np.tan(delta)
    return np.exp(-np.power(tan_theta / roughness, 2)) / (np.pi * roughness * roughness * np.power(cos_theta, 4))

def CT_D(delta):
    cos_theta = np.cos(delta)
    tan_theta = np.tan(delta)
    return np.exp(-np.power(tan_theta, 2)) / (np.pi * np.power(cos_theta, 4))

def TrowbridgeReitz_D(roughness, theta):
    c = 1 / np.pi / roughness / roughness
    return np.power(roughness * roughness / (np.power(np.cos(theta), 2) * (roughness * roughness - 1) + 1), 2) * c


def GGX_D(roughness, theta):
    cos_theta = np.cos(theta)
    tan_theta = np.tan(theta)
    return roughness * roughness / (np.pi * np.power(cos_theta, 4) * np.power(roughness * roughness + np.power(tan_theta, 2), 2))

def G_shadow(alpha, delta, theta_r, theta_i):
    first = 2*np.cos(delta)*np.cos(theta_r)/np.cos(alpha)
    second = 2*np.cos(delta)*np.cos(theta_i)/np.cos(alpha)
    minimum = min(1, first, second)
    return minimum

def Fresnel(C_spec, alpha):
    return C_spec+(1-C_spec)*np.power(1-np.cos(alpha), 5)

def BRDF_known(D, F, G, theta_i, theta_r):
    return D*F*G/(4*np.cos(theta_i)*np.cos(theta_r))