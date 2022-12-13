from Dados import *
import matplotlib.pyplot as plt

def euler(a : float, b : float, h : float, omega_0 : float, theta_0 : float) -> list[float]:
    t = np.arange(a, b + h, h)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    theta[0] = theta_0
    omega[0] = omega_0
    for i in range(0,len(t) - 1):
        theta[i+1] = theta[i] + h * df1(omega[i], theta[i], t[i])
        omega[i+1] = omega[i] + h * df2(omega[i], theta[i], t[i])
    return theta, t

def rk2(a : float, b : float, h : float, omega_0 : float, theta_0 : float) -> list[float]:
    t = np.arange(a, b + h, h)
    theta = np.zeros(len(t))
    omega = np.zeros(len(t))
    y = np.zeros(len(t))
    theta[0] = theta_0
    omega[0] = omega_0
    for i in range(0,len(t) - 1):
        theta_k1 = df1(omega[i], theta[i], t[i])
        theta_k2 = df1(omega[i] + theta_k1 * h, theta[i] + theta_k1 * h, t[i] + h)
        omega_k1 = df2(omega[i], theta[i], t[i])
        omega_k2 = df2(omega[i] +  omega_k1 * h, theta[i] +  omega_k1 * h, t[i] + h)
        theta[i+1] = theta[i] + h * (theta_k1 + theta_k2)/2
        omega[i+1] = omega[i] + h * (omega_k1 + omega_k2)/2
    return theta, t


