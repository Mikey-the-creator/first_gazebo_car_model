# 🚗 first_gazebo_car_model

A minimal **differential-drive car robot model** for **ROS 2 Humble** with **Gazebo** and **RViz** support.  
This is my first attempt at building and simulating a robot model as part of my robotics learning journey.

---

## ✨ Features
- URDF/Xacro model of a simple car-like robot with two drive wheels  
- Launch files for RViz and Gazebo simulation  
- Custom empty world for Gazebo  
- Joint state and robot state publishers  
- Ready to extend with sensors (LIDAR, camera, etc.)

---

## 📦 Installation

Clone into your ROS 2 workspace:
```bash
cd ~/ros2_ws/src
git clone git@github.com:Mikey-the-creator/first_gazebo_car_model.git
cd ~/ros2_ws
colcon build
source install/setup.bash
