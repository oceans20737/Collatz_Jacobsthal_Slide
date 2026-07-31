# -*- coding: utf-8 -*-
"""code_01_collatz_j2_slide.ipynb
"""

# Jacobsthal Slide and Shiftless Orbit in Collatz Trajectory
# Author: Hiroshi Harada
# Date: August 1, 2026
#
# Description:
# This Python script computes the Shiftless Orbit of any odd initial value
# under the Collatz mapping, using the Jacobsthal-based Shiftless Model.
# The program generates:
#   - J2 Expansion
#   - Marge (Adjacent Sum)
#   - J2 Slide (Wave Switching)
# and verifies that each generated J2 Slide exactly matches the analytical
# J2 spinor expansion of the next odd Collatz kernel.
#
# The output is written both to the console (tab-separated) and to a CSV file
# in an Excel-friendly format. All numeric values are protected against
# Excel's automatic date conversion.
#
# License:
#   Research Document: CC BY 4.0
#   Python Source Code: MIT License
# © 2026 Hiroshi Harada

import csv
from fractions import Fraction

def get_j2_value(x1, x2, k):
    """Compute the J2 sequence value at index k using Fraction."""
    a, b = Fraction(x1), Fraction(x2)

    if k == 0:
        return a
    if k == 1:
        return b

    if k > 1:
        for _ in range(k - 1):
            a, b = b, b + 2 * a
        return b

    # k < 0 (reverse recurrence)
    for _ in range(-k):
        a, b = (b - a) / 2, a
    return a


def W(n_val, k):
    """Normalized J2 wave: W(k) = n * 2^k + J2(0,1)_k."""
    power2 = Fraction(2**k) if k >= 0 else Fraction(1, 2**(-k))
    return Fraction(n_val) * power2 + get_j2_value(0, 1, k)


def fmt_console(frac):
    """Human-readable Fraction formatting."""
    return str(frac.numerator) if frac.denominator == 1 else f"{frac.numerator}/{frac.denominator}"


def fmt_csv(frac):
    """Excel-safe formatting (prevent automatic date conversion)."""
    if frac.denominator == 1:
        return f"'{frac.numerator}"
    return f"'{frac.numerator}/{frac.denominator}"


def compute_shiftless_orbit(initial_val):
    """Compute Shiftless Orbit and all J2 waves."""
    n = initial_val
    nodes = []
    shifts = []

    # Odd Collatz orbit
    while True:
        nodes.append(n)
        if n == 1:
            break
        nxt = 3 * n + 1
        s = 0
        while nxt % 2 == 0:
            nxt //= 2
            s += 1
        shifts.append(s)
        n = nxt

    # Level range
    total_shifts = sum(shifts)
    levels = list(range(-total_shifts - 3, 4))

    # Cumulative offsets
    offsets = [0]
    for s in shifts:
        offsets.append(offsets[-1] + s)

    j2_base = [get_j2_value(0, 1, L) for L in levels]

    results = []
    all_verified = True

    # First node: J2 Expansion
    wave = [W(nodes[0], L + offsets[0]) for L in levels]
    results.append({"name": "J2 Expansion", "data": wave})

    # Marge & Slide
    for i in range(1, len(nodes)):
        prev_n = nodes[i - 1]
        next_n = nodes[i]

        # Marge (Adjacent Sum)
        marge = [
            wave[j] + W(prev_n, L + 1 + offsets[i - 1])
            for j, L in enumerate(levels)
        ]
        results.append({"name": "Marge", "data": marge})

        # Slide
        slide = []
        for j, L in enumerate(levels):
            idx = L + offsets[i]
            base = get_j2_value(0, 1, idx)
            s_val = marge[j] + base
            slide.append(s_val)

            # Verification
            if s_val != W(next_n, idx):
                all_verified = False

        results.append({"name": "J2 Slide", "data": slide})
        wave = slide

    return levels, j2_base, results, all_verified


def main():
    print("==================================================")
    print(" Shiftless Model: Excel Table Generator & Verifier")
    print("==================================================")

    initial_val = 7
    user_input = input(f"Enter an odd initial value (default: {initial_val}): ").strip()
    if user_input:
        try:
            initial_val = int(user_input)
            if initial_val <= 0 or initial_val % 2 == 0:
                print("Please enter a positive odd integer.")
                return
        except ValueError:
            print("Invalid input. Using default value.")

    levels, j2_base, results, verified = compute_shiftless_orbit(initial_val)

    print(f"\nInitial Value\t{initial_val}\n")
    header = "Level\t" + "\t".join(str(L) for L in levels)
    print(header)
    print("J2(0,1)\t" + "\t".join(fmt_console(v) for v in j2_base))
    print()

    print(header)
    for row in results:
        print(row["name"] + "\t" + "\t".join(fmt_console(v) for v in row["data"]))

    print("\n--- Verification Result ---")
    print("[SUCCESS] All J2 Slides match analytical J2 waves."
          if verified else "[ERROR] Verification failed.")

    # CSV output
    filename = f"collatz_j2_slide_{initial_val}.csv"
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Initial Value", initial_val])
        writer.writerow([])
        writer.writerow(["Level"] + levels)
        writer.writerow(["J2(0,1)"] + [fmt_csv(v) for v in j2_base])
        writer.writerow([])
        writer.writerow(["Level"] + levels)
        for row in results:
            writer.writerow([row["name"]] + [fmt_csv(v) for v in row["data"]])

    print(f"\n[INFO] Saved as '{filename}' (Excel-safe format).")


if __name__ == "__main__":
    main()

