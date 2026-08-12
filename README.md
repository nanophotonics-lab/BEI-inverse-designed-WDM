# BEI-inverse-designed-WDM
binary structure data and a visualization script for inverse-designed lithium niobate wavelength demultiplexer

# Binary Structure Visualization

This repository contains binary structure data and a visualization script for inverse-designed lithium niobate (LN) photonic devices.

The script converts binary structure files (`0` = air, `1` = LN) into black-and-white images suitable for visualization and publication.

---

## Directory Structure

```text
.
├── structures/
│   ├── structure_50nm_0.04.txt
│   ├── structure_50nm_0.06.txt
│   ├── ...
│   └── structure_100nm_0.12.txt
│
├── structure_plots/
│   ├── structure_50nm_0.04.png
│   ├── ...
│
├── plot_structures.py
└── README.md
```

---

## Input Format

Each structure file is a plain text matrix containing binary values.

- `0` → Air (white)
- `1` → Lithium niobate (black)

Example

```text
0 0 0 1 1 1 ...
0 1 1 1 0 0 ...
...
```

Each file represents the final projected design after topology optimization and binary thresholding.

---

## File Naming

Structure files follow the convention

```text
structure_<constraint_size>nm_<etch_depth>.txt
```

Examples

```text
structure_50nm_0.04.txt
structure_75nm_0.08.txt
structure_100nm_0.12.txt
```

where

- `<constraint_size>` is the target minimum feature/void size (nm)
- `<etch_depth>` is the LN etch depth (µm)

---

## Usage

Run

```bash
python plot_structures.py
```

The script automatically reads all binary structure files in the `structures/` directory and generates corresponding images in

```text
structure_plots/
```

PNG images are exported at 600 dpi.

---

## Notes

The binary structures were obtained by applying the same conic filtering and projection procedures used during topology optimization.

The visualization script displays

- White → Air (`0`)
- Black → Lithium niobate (`1`)

without axes or annotations.

---

## Citation

If these structure files are useful in your research, please cite the associated publication.

> *A Birefringent Effective-Index Method for Efficient Inverse Design of Lithium Niobate Photonic Devices* (to be updated after publication).

---

## AI-assisted Code Disclosure

The plotting and file-export utilities were developed with assistance from OpenAI ChatGPT. The optimization algorithm, mapping procedure, and simulation data were designed, implemented, and validated by the authors.
