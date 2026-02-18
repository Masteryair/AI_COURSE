import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


def main():
	# Geometry: square with X bracing
	nodes = np.array(
		[
			[0.0, 0.0],
			[0.0, 2.0],
			[2.0, 2.0],
			[2.0, 0.0],
		]
	)
	wall_x = 0.0
	wall_y = 5.0
	load_point = (2.0, 0.0)
	load_force = (0.0, -1000.0)
	bars = [
		(0, 1),
		(1, 2),
		(2, 3),
		(3, 0),
		(0, 2),
		(1, 3),
	]

	# Mechanical properties for bars
	rod_side = 0.035  # meters
	youngs_modulus = 69e9  # Pa
	yield_stress = 276e6  # Pa
	rod_area = rod_side * rod_side
	moment_of_inertia = (rod_side ** 4) / 12
	axial_rigidity = youngs_modulus * rod_area

	print(f"Rod side: {rod_side:.4f} m")
	print(f"Rod area: {rod_area:.6f} m^2")
	print(f"Moment of inertia: {moment_of_inertia:.6e} m^4")
	print(f"Young's modulus: {youngs_modulus:.2e} Pa")
	print(f"Yield stress: {yield_stress:.2e} Pa")
	print(f"Axial rigidity EA: {axial_rigidity:.2e} N")

	# Plot the system
	fig, ax = plt.subplots(figsize=(6, 6))
	ymin = nodes[:, 1].min() - 0.5
	ymax = nodes[:, 1].max() + 0.5
	xmin = nodes[:, 0].min() - 0.5
	xmax = nodes[:, 0].max() + 0.5
	ax.plot([wall_x, wall_x], [ymin, ymax], color="black", linewidth=3)
	ax.plot([xmin, xmax], [wall_y, wall_y], color="black", linewidth=3)
	for i, j in bars:
		xi, yi = nodes[i]
		xj, yj = nodes[j]
		ax.plot([xi, xj], [yi, yj], color="tab:blue", linewidth=2)

	arrow_scale = 0.001
	load_arrow = FancyArrowPatch(
		load_point,
		(load_point[0] + load_force[0] * arrow_scale, load_point[1] + load_force[1] * arrow_scale),
		color="tab:red",
		arrowstyle="-|>",
		mutation_scale=15,
		linewidth=2,
	)
	ax.add_patch(load_arrow)

	ax.scatter(nodes[:, 0], nodes[:, 1], color="tab:orange", s=60, zorder=5)
	ax.set_aspect("equal", adjustable="box")
	ax.grid(True, linestyle="--", alpha=0.4)
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_title("Square with X Bracing")
	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	main()
