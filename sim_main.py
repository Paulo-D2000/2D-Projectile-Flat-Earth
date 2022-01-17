#################
# 2022 - PU4THZ #
#################

############################
# 2D PROJECTILE FLAT EARTH #
############################

import numpy as np
import matplotlib.pyplot as plt

km_h = 1.0/3.6  #m/s

g = -9.89     #m^2/s

h0 = 500    #m
v00 = 300 #km/h
ang0 = 45      #deg

dt = 0.1

v0 = v00*km_h

t = np.arange(0,20,dt)

vel = np.zeros((2,len(t)))
pos = np.zeros((2,len(t)))


vel[:,0] = [ v0*np.cos(ang0*np.pi/180), v0*np.sin(ang0*np.pi/180)]
pos[:,0] = [0,h0]

for i in range(len(t)-1):
    pos[:,i+1] = pos[:,i] + vel[:,i]*dt
    vel[:,i+1] = vel[:,i] + np.array([0,g])*dt

    if(pos[1,i]<0):
        print("Impact!\n Time: %f seconds\n Speed: %f m/s"%(t[i], np.sqrt(vel[0,i]**2+vel[1,i]**2)))
        break


plt.plot(t[pos[1]>0],pos[1,pos[1]>0],label='angle: %d'%(ang0))
plt.title('"Package"\nV = %dKm/h, H = %dm, ang = %d deg'%(v00,h0,ang0))
plt.xlabel('t (s)')
plt.ylabel('h (m)')
plt.legend()
plt.show()
