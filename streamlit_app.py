import streamlit as st
import matplotlib.pyplot as plt
import simulator

st.title("✈️ Flight Stability and PID Simulator")
st.write("Tune the PID controller to stabilize aircraft pitch angle.")

kp = st.slider("Kp (Proportional)", 0.0, 5.0, 2.0, 0.1)
ki = st.slider("Ki (Integral)", 0.0, 2.0, 0.5, 0.1)
kd = st.slider("Kd (Derivative)", 0.0, 2.0, 0.8, 0.1)
target = st.slider("Target Pitch Angle (°)", 0.0, 20.0, 10.0, 0.5)
duration = st.slider("Simulation Duration (s)", 2.0, 20.0, 10.0, 0.5)

if st.button("Run Simulation"):
    t, theta = simulator.run_simulation(kp, ki, kd, target_angle=target, duration=duration)
    fig, ax = plt.subplots()
    ax.plot(t, theta, label="Pitch Angle (deg)")
    ax.axhline(target, color='r', linestyle='--', label="Target Angle")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Pitch Angle (deg)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
