import numpy as np

class AircraftPitchModel:
    def __init__(self, damping=0.5, stiffness=0.2, dt=0.01):
        self.damping = damping
        self.stiffness = stiffness
        self.dt = dt
        self.theta = 0.0
        self.theta_dot = 0.0

    def step(self, control_input):
        theta_ddot = control_input - self.damping * self.theta_dot - self.stiffness * self.theta
        self.theta_dot += theta_ddot * self.dt
        self.theta += self.theta_dot * self.dt
        return self.theta
