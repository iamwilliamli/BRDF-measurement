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


# Math Calculation Vector form
theta_i = deg2rad(float(input('输入光源天顶角角度: '))) # Input the Zenith angle of the light source
theta_r = deg2rad(float(input('输入相机天顶角角度： '))) # input the Zenith angle of the camera
phi_i = 0 #光源方位角固定为0 Azimuth angle of light source is fixed to zero
phi_r = deg2rad(float(input('输入相机方位角: ')))




incident_vector = incident(theta_i, phi_i) # 入射光向量
camera_vector = view(theta_r, phi_r) # 出射光线向量
normal = normal() # 平面法向量
half_angle = half(theta_i, phi_i, theta_r, phi_r) # 半角向量 H
delta_angle = delta(half_angle, normal)
alpha_angle = alpha(incident_vector, camera_vector)
#print(half_angle)
#print(alpha_angle)
#print(delta_angle)

print(delta_angle)
d = b.Beckmann_D(1, delta_angle)
#d = b.CT_D(delta_angle)
#print(d)
f = b.Fresnel(0.919, alpha_angle)
#print(f)
g = b.G_shadow(alpha_angle, delta_angle, theta_r, theta_i)
#print(g)
known = b.BRDF_known(d, f, g, theta_i, theta_r)
print(known)