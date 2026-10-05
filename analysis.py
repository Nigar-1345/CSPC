import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]


v = np.gradient(y, t)
a = np.gradient(v, t)


mean_a = np.mean(a)
std_a = np.std(a)

print(f"Mean acceleration: {mean_a:.3f} m/s^2")
print(f"Standard deviation of acceleration: {std_a:.3f} m/s^2")


v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]


y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]


max_diff = np.max(np.abs(y - y_rec))
print(f"Max difference between original and recovered position: {max_diff:.3f} m")


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax1.plot(t, y, label='Measured Position', color='blue')
ax1.set_ylabel('Position y (m)')
ax1.set_title('Motion Analysis from Tracking Data')
ax1.grid(True)
ax1.legend()

ax2.plot(t, v, label='Calculated Velocity', color='green')
ax2.set_ylabel('Velocity v (m/s)')
ax2.grid(True)
ax2.legend()

ax3.plot(t, a, label='Calculated Acceleration', color='orange', alpha=0.7)
ax3.axhline(-9.81, color='red', linestyle='--', label='Theoretical g (-9.81 m/s²)')
ax3.set_xlabel('Time t (s)')
ax3.set_ylabel('Acceleration a (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png', dpi=300)
plt.close()
print("Saved figure as motion.png")


try:
    traj_data = np.loadtxt('trajectory.csv', delimiter=',', skiprows=1)
    t_traj = traj_data[:, 0]
    x_traj = traj_data[:, 1]
    y_traj = traj_data[:, 2]

    
    vx = np.gradient(x_traj, t_traj)
    vy = np.gradient(y_traj, t_traj)
    speed = np.sqrt(vx**2 + vy**2)

    fig_bonus, (ax_path, ax_speed) = plt.subplots(1, 2, figsize=(12, 5))

    
    ax_path.plot(x_traj, y_traj, color='purple')
    ax_path.set_xlabel('x (m)')
    ax_path.set_ylabel('y (m)')
    ax_path.set_title('2D Trajectory (x vs y)')
    ax_path.grid(True)

    
    ax_speed.plot(t_traj, speed, color='crimson')
    ax_speed.set_xlabel('Time t (s)')
    ax_speed.set_ylabel('Speed (m/s)')
    ax_speed.set_title('Speed over Time')
    ax_speed.grid(True)

    plt.tight_layout()
    plt.savefig('trajectory_analysis.png', dpi=300)
    plt.close()
    print("Saved bonus figure as trajectory_analysis.png")
except OSError:
    print("trajectory.csv not found, skipping bonus part.")