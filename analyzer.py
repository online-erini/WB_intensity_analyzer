# ===== western-blot-analyzer repository =====
# This canvas shows the contents of three files you will place in your GitHub repo.

# --------------------------------------------------
# File: analyzer.py
# --------------------------------------------------
"""Western Blot Band Analyzer
Author: Erini Galatis (replace with your name)
Description: Quantifies Western blot band intensities using OpenCV.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def load_image(image_path: str | Path) -> np.ndarray:
    """Load an image in grayscale."""
    img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image not found at: {image_path}")
    return img


def crop_band(image: np.ndarray, top_left: tuple[int, int], bottom_right: tuple[int, int]) -> np.ndarray:
    """Return a cropped region representing a single band."""
    x1, y1 = top_left
    x2, y2 = bottom_right
    return image[y1:y2, x1:x2]


def quantify_band(band: np.ndarray) -> float:
    """Calculate band intensity (inverted grayscale sum)."""
    # Invert grayscale (white background → 0, dark band → large)
    return float(np.sum(255 - band))


def analyze_bands(image_path: str | Path, band_coords: list[tuple[tuple[int, int], tuple[int, int]]]):
    """Return a list of (band_index, intensity)."""
    image = load_image(image_path)
    intensities = []
    for idx, (top_left, bottom_right) in enumerate(band_coords):
        band = crop_band(image, top_left, bottom_right)
        intensity = quantify_band(band)
        intensities.append((idx + 1, intensity))
    return intensities


def plot_results(results: list[tuple[int, float]]):
    """Plot band intensities as a bar chart."""
    bands, values = zip(*results)
    plt.figure()
    plt.bar(bands, values)
    plt.xlabel("Band")
    plt.ylabel("Intensity (a.u.)")
    plt.title("Western Blot Band Quantification")
    plt.tight_layout()
    plt.show()


def main():
    """Example usage with hard‑coded coordinates."""
    image_path = "western_blot_example.png"  # Put your image in repo root

    # Each tuple: ((x1, y1), (x2, y2))  –  pixel coords from top‑left
    band_coords = [
        ((30, 50), (130, 100)),
        ((30, 110), (130, 160)),
        ((30, 170), (130, 220)),
    ]

    results = analyze_bands(image_path, band_coords)
    print("Band Intensities:")
    for band_num, intensity in results:
        print(f"Band {band_num}: {intensity:.2f}")

    plot_results(results)


if __name__ == "__main__":
    main()

