import control
import matplotlib.pyplot as plt

time_const = 17.9
heater_gain = 2.27
time_delay = 2.2

num = [heater_gain]
den = [time_const,1]

H1 = control.tf(num,den) # The TF without time delay
num_pade, den_pade = control.pade(time_delay,5) 
H_delay = control.tf(num_pade,den_pade) # TF for time delay
H = control.series(H1,H_delay) # Complete TF

t,y = control.step_response(H)
plt.plot(t,y)
plt.show()
