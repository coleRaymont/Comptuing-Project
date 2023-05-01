import numpy as np      
import matplotlib.pyplot as plt

def projectile(M,g,V,ang,K):
    #calculate initial velocity for X and Y
    Vx = V * np.cos(ang/180 * np.pi)
    Vx = float(Vx)
    Vy = V * np.sin(ang/18 * np.pi)
    Vy = float(Vy)

    #Drag force
    F = K * V**2
    #calculate initial acceleration
    
    ax = [-(F * np.cos(ang/180 * np.pi)/M)]
    ay = [-g-(F * np.sin(ang/180 * np.pi)/M)]   

    #calculate time value on the object

    t = [0]
    counter = 0
    dt = 0.2
    x = [0]
    y = [0]
    while(counter < 10):
        t.append(t[counter] + dt)
        Vx.append(Vx[counter] + dt * ax[counter])
        Vy.append(Vy[counter] + dt * ay[counter])

        x.append(x[counter] + dt * Vx[counter])
        y.append(y[counter] + dt * Vy[counter])

        #calculate magnitude of new velocity 
        Vel = np.sqrt(Vx[counter+1]**2 + Vy[counter+1]**2)
        F = K * Vel**2
        ax.append(-(F * np.cos(ang/180 * np.pi))/M)
        ay.append(-g-(F * np.sin(ang/180 * np.pi)/M))
        counter = counter + 1

    plt.plot(x,y, 'go') 
    plt.ylabel("Y ")
    plt.xlabel("X ")
    plt.grid()
    plt.show()
        
    
    
    
projectile(1,9.8,30,60.0,0.05)

    