## Western Blot Band Analyzer

A practice tool to quantify Western blot band intensities using OpenCV.

![demo blot](./docs/demo.png)

## Features
* **Loads** grayscale Western blot images (PNG, TIFF, JPEG)
* **User‑defined boxes** for each band
* **Quantifies** band intensity (inverted grayscale sum)
* **Plots** the results as a bar graph
* **Outputs** intensities in the console – easy to copy into spreadsheets or further scripts

## Installation
```bash
# 1. Clone the repo
$ git clone https://github.com/your‑username/western‑blot‑analyzer.git
$ cd western‑blot‑analyzer

# 2. Create a virtual environment (optional but recommended)
$ python -m venv .venv
$ source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
$ pip install -r requirements.txt
```

## Usage
1. Place your blot image (e.g., `western_blot_example.png`) in the repo root.
2. Open **`analyzer.py`** and edit `band_coords` with the pixel coordinates for each band.
3. Run the script:
```bash
python analyzer.py
```
4. View the printed intensities and the pop‑up bar graph.

## How to Get Band Coordinates
Use image viewer (ImageJ, FIJI, etc) to read pixel positions:
* **(x1, y1)** = top‑left corner of the band box
* **(x2, y2)** = bottom‑right corner

"""

