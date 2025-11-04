# ✈️ Flight Stability and PID Simulator

A lightweight and interactive simulator for testing and visualizing **PID controller performance in aircraft pitch stabilization**.  
This project helps understand how proportional, integral, and derivative gains affect flight dynamics using simple Python-based physics.

Built using **Python**, **NumPy**, **Matplotlib**, and **Streamlit**, this tool lets users interactively tune PID gains and visualize how the aircraft stabilizes toward a target pitch angle.

---

## 🧠 What It Does
- Simulates aircraft pitch dynamics with a PID control loop  
- Lets users tune **Kp**, **Ki**, and **Kd** values in real-time  
- Displays pitch response over time (angle vs time graph)  
- Shows how controller stability changes with different PID parameters  
- Interactive web interface built with **Streamlit**

---

## ⚙️ Features
- Real-time simulation with adjustable parameters  
- Clean plots of aircraft pitch response  
- Visual understanding of controller performance  
- Easy to extend for roll/yaw control or full 6-DOF modeling

---

## 🧩 Project Structure
flight-pid-sim/
│
├── aircraft_model.py # Defines aircraft pitch dynamics model
├── pid_controller.py # PID control logic
├── simulator.py # Runs the full simulation loop
├── streamlit_app.py # Web dashboard for tuning and visualization
├── requirements.txt # Dependencies
└── README.md # Project overview (this file)

---

## 🚀 Run Locally
1. **Clone the repository**
   ```bash
   git clone https://github.com/japkaran12/flight-pid-sim.git
   cd flight-pid-sim

🌐 Deployed Version

If deployed on Streamlit Cloud, you can access it here:
👉 Flight Stability Simulator (Streamlit App)

📘 Concepts Used

Proportional–Integral–Derivative (PID) control

Aircraft pitch motion modeling

Dynamic simulation with time-stepping

Real-time visualization using Streamlit and Matplotlib

🧑‍💻 Author

Japkaran Singh Arneja
Aerospace Engineering Student | Lovely Professional University
Passionate about flight dynamics, control systems, and autonomous aerial vehicles.

📄 License

This project is open-source under the MIT License — feel free to use, modify, and improve it.

⭐ Contribute

Pull requests are welcome! If you find a bug or want to suggest a new feature, open an issue or create a PR.

🛠 Example Output

You can visualize aircraft pitch angle settling over time like this:

Target Pitch: 10°
Kp = 3.0, Ki = 1.5, Kd = 0.6


→ Smooth convergence to stable flight within a few seconds.

🚀 Why This Project Matters

This simulator provides an intuitive way to learn control theory for aerospace applications without needing complex flight simulators.
It’s ideal for students, researchers, and engineers exploring basic flight stability systems.