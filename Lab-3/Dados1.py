import matplotlib.pyplot as plt
import numpy as np

n = 540

def rgb2gray(rgb):
    rgb = rgb.astype(float)
    return (rgb[:,:,0]+rgb[:,:,1]+rgb[:,:,2])*1/3

# Deixa a imagem preto e branco
img = plt.imread('Arquivos/selfie.jpg')
imggray = rgb2gray(img)
plt.imshow(imggray, cmap="gray")

# Adiciona ruído
t = imggray.shape
imgruido = imggray + np.random.rand(t[0],t[1])
plt.imshow(imgruido, cmap="gray")

