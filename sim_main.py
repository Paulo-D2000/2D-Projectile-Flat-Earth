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

h0 = 24384    #m
v00 = 3675.13 #km/h
m0 = 1360.777 #kg
ang0 = 5      #deg

dt = 10.0

v0 = v00*km_h

t = np.arange(0,30e4,dt)

vel = np.zeros((2,len(t)))
pos = np.zeros((2,len(t)))


vel[:,0] = [ v0*np.cos(ang0*np.pi/180), v0*np.sin(ang0*np.pi/180)]
pos[:,0] = [0,h0]

for i in range(len(t)-1):
    pos[:,i+1] = pos[:,i] + vel[:,i]*dt
    vel[:,i+1] = vel[:,i] + np.array([0,g/m0])*dt

    if(pos[1,i]<0):
        print("Impact!\n Time: %f seconds\n Speed: %f m/s"%(t[i], np.sqrt(vel[0,i]**2+vel[1,i]**2)))
        break


plt.plot(t[pos[1]>0],pos[1,pos[1]>0],label='angle: %d'%(ang0))
plt.title('SR-71 "Package" EXPRESS Delivery\nV = %dKm/h, H = %dm, M = %dKg\nV = MACH 3, H = 80000ft, M = 3000 pounds'%(v00,h0,m0))
plt.xlabel('t (s)')
plt.ylabel('h (m)')
plt.legend()
plt.show()
