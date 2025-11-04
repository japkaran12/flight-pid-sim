import numpy as np
from pid_controller import PIDController
from aircraft_model import AircraftPitchModel

def run_simulation(kp, ki, kd, target_angle=10.0, duration=10.0, dt=0.01):
    pid = PIDController(kp=kp, ki=ki, kd=kd, dt=dt)
    aircraft = AircraftPitchModel(dt=dt)
    t = np.arange(0.0, duration, dt)
    theta_values = []
    for _ in t:
        error = target_angle - aircraft.theta
        control = pid.update(error)
        theta = aircraft.step(control)
        theta_values.append(theta)
    return t, np.array(theta_values)
