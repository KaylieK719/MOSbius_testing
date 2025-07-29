# MOSbius Testing Interface

A collection of MicroPython helper functions for running automated tests on the MOSbius PCB and on-chip modules (ring oscillator, current bias, etc.) via a Raspberry Pi Pico and an ILI9341 display. This interface tests the functionality of the [MOSBius](https://mosbius.org/0_front_matter/intro.html) PCB and chip.

## Table of Contents

- [Features](#features)
- [Schematics](#Schematics)
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Testing Proceedure](#testing-proceedure)
  - [Testing Setup](#setup)  
  - [Power-Supply Test](#power-supply-test)  
  - [Digital Level-Shifter Tests](#digital-level-shifter-tests)  
  - [Manual Enable Test](#manual-enable-test)  
  - [Full PCB Test Suite](#full-pcb-test-suite)  
  - [On-Chip Manual Tests](#on-chip-manual-tests)  
- [License](#license)

---

## Features

- Automated **power supply + power supply protection** circuit test  
- Automated sequential **DT/CK/EN** header digital-level shifter tests  
- Automatted **Manual enable** voltage test  
- Full run of **PCB test**  
- Interactive **NMOS/PMOS current bias** confirmation  
- Interactive **ring oscillator** scope-based waveform check  

---
## Schematics 
!(images/MOSbius_testing_pcb_v1.pdf)

---

## Requirements
- Raspberry Pi Pico (or compatible RP2040 board)    
- ILI9341 SPI display  
- MicroPython firmware [Thonny](https://thonny.org/) (follow the website's directions for installation)
---

## Installation
1. Download and copy ALL FILES in `lcd_interface` folder onto your Pico's filesystem (DO NOT CHANGE FILE NAMES)
2. Download and copy the following files from external libraries onto your Pico's filesystem:
    - LCD → [rdagger micropython-ili9341](https://github.com/rdagger/micropython-ili9341) (`ili9341.py`)
    - MOSbius MicroPython Flow → [Jianxun MOSbius_MicroPython_Flow](https://github.com/Jianxun/MOSbius_MicroPython_Flow) (`MOSbius.py`) 

## MISC (TBE)
- ADC wiring:  
  - Orange → pin 27 (sensorO)  
  - Green  → pin 26 (sensorG)  
  - Yellow → pin 28 (sensorY)  
- Output pins:  
  - DT → pin 12  
  - CK → pin 11  
  - EN → pin 10  

## Testing Proceedure  
1. In progress
