import numpy as np 
import matplotlib.pyplot as plt 

time = np.linspace(0, 100, 101)  # 100 evenly spaced numbers between 0 and 10
# print(time) 
# amplitude = np.sin(time)  # Sine wave values for the given time points  
# print(amplitude)

altitude = np.zeros(101)  # Array of zeros to represent altitude
# print(altitude)
for i in range(1, len(time)):
    altitude[i] = .01 * time[i] ** 2  # Simulating altitude as a function of time (quadratic growth)
# print(altitude)

plt.figure(figsize=(8,6))
plt.plot(time, altitude, 'b-', label='Spacecraft Altitude')
plt.title('Spacecraft Ascent: Altitude vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude (kilometers)')
plt.grid(True)
plt.legend()
plt.show()

