# NOTE:
# Plotting and file-export utilities were developed with assistance
# from OpenAI ChatGPT. The optimization algorithm, mapping procedure,
# and simulation data were developed and validated by the authors.

import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# =========================================================
# User settings
# =========================================================

input_dir = Path("./structures")
save_dir = Path("./structure_plots")
save_dir.mkdir(parents=True, exist_ok=True)

etch_depth_list = [0.04, 0.06, 0.08, 0.10, 0.12]
constraint_size_list_nm = [50, 75, 100]

design_region_width = 30.0
design_region_height = 10.0
design_region_resolution = 100

Nx = int(design_region_width * design_region_resolution + 1)
Ny = int(design_region_height * design_region_resolution + 1)

save_png = True
save_pdf = True

dpi = 600


# =========================================================
# Plot structures
# =========================================================
for constraint_nm in constraint_size_list_nm:
    for etch_depth in etch_depth_list:

        input_file = (
            input_dir
            / f"structure_{constraint_nm}nm_{etch_depth:.2f}.txt"
        )

        # Load and reshape
        structure = np.loadtxt(input_file).reshape(Nx, Ny).T

        # 0 = white, 1 = black
        fig = plt.figure(figsize=(6, 2))
        ax = fig.add_axes([0, 0, 1, 1])

        ax.imshow(
            structure,
            cmap="binary",
            vmin=0,
            vmax=1,
            interpolation="nearest",
            origin="lower",
            aspect="equal",
        )

        # Remove axes
        ax.set_axis_off()

        base_name = (
            save_dir
            / f"structure_{constraint_nm}nm_{etch_depth:.2f}"
        )

        if save_png:
            fig.savefig(
                f"{base_name}.png",
                dpi=dpi,
                bbox_inches="tight",
                pad_inches=0,
            )

        plt.close(fig)

        print(f"Saved: {base_name}")