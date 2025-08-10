ErgoKeyboard
=======================================

Overview
--------

This repository contains instructions for installing KMK firmware on your microcontroller (MCU). KMK is an open-source project designed for keyboard firmware and is easy to set up and customize.

Prerequisites
-------------

- Microcontroller compatible with KMK (e.g., ATmega32U4, ESP32)
- Python 3.x installed on your computer
- Git installed on your computer
- A USB cable to connect the MCU to your computer

Installation Steps
------------------

1. Clone the Repository

   git clone https://github.com/KMKfw/kmk_firmware.git
   cd kmk_firmware

2. Install Dependencies

   Install the required Python packages:

   pip install -r requirements.txt

3. Configure Your Keyboard

   - Navigate to the `kmk_firmware` directory.
   - Edit the `config.py` file to match your keyboard layout and key mappings.

4. Build the Firmware

   Run the following command to build the firmware:

   make

5. Flash the Firmware

   Connect your MCU to your computer and flash the firmware using:

   make flash

6. Test Your Keyboard

   After flashing, test your keyboard to ensure all keys are functioning as expected.

Credits
-------

- KMK Firmware: This project is built upon the KMK firmware. For more information, visit the KMK GitHub Repository:
  https://github.com/KMKfw/kmk_firmware

- Model Reference: The keyboard model used in this project is based on the "Cyberpunkish Dactyl Manuform Skeleton Edition 3x5+3"
  by Oleksandr, available on Printables:
  https://www.printables.com/model/240700-cyberpunkish-dactyl-manuform-skeleton-edition-3x53

