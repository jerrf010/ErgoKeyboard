# ErgoKeyboard

This repository contains the firmware and configuration for my custom split ergonomic keyboard, built on the **Cyberpunkish Dactyl Manuform Skeleton Edition 3x5+3** case and powered by **KMK firmware**.

---

## Overview

This keyboard is a fully split ergonomic design with a 3x5 key layout plus a 3-key thumb cluster per hand.  
It is powered by **KMK firmware**, written in CircuitPython, and runs independently on each half (Left and Right).  
**NOTE:** The thumb cluster is from https://github.com/atsuyuki/dactyl-manuform-skeleton-edition-4x5

Each half contains:
- `kmk/` (the KMK firmware folder)
- `boot.py`
- `code.py` (keyboard configuration and keymap)

---

## Repository Structure
<img width="140" height="240" alt="image" src="https://github.com/user-attachments/assets/2992d9a5-d28a-47fd-93e6-ef3db737ff01" />

- **L_keyboard/** → Firmware files for the left half  
- **R_keyboard/** → Firmware files for the right half  

---

## Installation

1. **Flash CircuitPython**  
   - Install CircuitPython (version 8.0 or newer) on your microcontrollers.  
   - You can download it from: https://circuitpython.org/downloads  

2. **Copy Files**  
   - On each half (Left and Right), copy the following into the CircuitPython drive:  
     - `kmk/` folder  
     - `boot.py`  
     - `code.py`

3. **Connect the Keyboard**  
   - Plug both halves into your computer using a TRRS cable (or USB depending on your wiring).  
   - The halves will communicate, and the keyboard should be recognized as a standard USB HID keyboard.  

4. **Customize Keymap**  
   - Edit `code.py` to configure your personal keymap.  
   - The file is in Python, so you can easily customize layers, macros, and functionality.

---

## Photos

Below are some photos of the assembled keyboard:

![Fig 1](https://github.com/user-attachments/assets/92095cff-39e8-481b-9a42-bcd6c77796d1)
![Fig 2](https://github.com/user-attachments/assets/7b43fd40-f869-431d-82be-5eedee9ba2ac)
![Fig 3](https://github.com/user-attachments/assets/ff8d7851-9365-4869-9821-a49a3b243dd0)


---

## Credits

- **Firmware:** [KMK Firmware](https://github.com/KMKfw/kmk_firmware)  
- **3D Model :** [Cyberpunkish Dactyl Manuform Skeleton Edition 3x5+3 by Oleksandr](https://www.printables.com/model/240700-cyberpunkish-dactyl-manuform-skeleton-edition-3x53)  
