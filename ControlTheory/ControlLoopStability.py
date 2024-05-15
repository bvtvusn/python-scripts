import control
import numpy as np
import matplotlib.pyplot as plt


# Transfer function for PI controller
Kp = 1.0
Ti = 8.4
#Kp = 1.63
#Ti = 15
Hp = control.tf([Kp*Ti,Kp],[Ti,0])

# Transfer function for process
time_const = 17.9
heater_gain = 2.27
time_delay = 2.2
num = np.array([heater_gain])
den = np.array([time_const,1])
H1 = control.tf(num,den) # The TF without time delay
num_pade, den_pade = control.pade(time_delay,2) 
H_delay = control.tf(num_pade,den_pade) # TF for time delay
H_process = control.series(H1,H_delay) # Complete TF


# Transfer function for lowpass filter 
Tf = 1
num_f = [1]
den_f = [Tf,1]
Hf = control.tf(num_f,den_f)

# The loop transfer function
L = control.series(Hp,H_process,Hf)

# Tracking transfer function
T = control.feedback(L,1)

#Draw step response
t,y = control.step_response(T)
plt.figure(1)
plt.plot(t,y)
plt.title("Step response of setpoint change")
plt.grid()

# Draw bode plot
plt.figure(2)
control.bode(L,dB=True, deg=True,margins=True)

# Draw Pole map
plt.figure(3)
control.pzmap(T)
p = control.pole(T)
z = control.zero(T)
print("Poles = ",p)

# Calculating stability margins and crossover frequencies
gm, pm, w180, wc = control.margin(L)
gmdb = 20*np.log10(gm)
print("wc=", f'{wc:.2f}',"rad/s") # Gain crossover frequency. (Freq where gain crosses below 1. WC must be smaller than W180 for the system to be stable
print("w180=", f'{w180:.2f}',"rad/s") # phase Crossover frequency. (phase crosses -180 at this frequency)
print("GM=", f'{gm:.2f}') # 
print("GM=", f'{gmdb:.2f}',"dB")
print("PM=", f'{pm:.2f}',"deg")
