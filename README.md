# MOSbius Testing Interface

A collection of MicroPython helper functions for running automated tests on the MOSbius PCB and on-chip modules (ring oscillator, current bias, etc.) via a Raspberry Pi Pico and an ILI9341 display.

## Table of Contents

- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Helper Functions Overview](#helper-functions-overview)  
  - [Global Setup](#global-setup)  
  - [UI & Timing Helpers](#ui--timing-helpers)  
  - [Power-Supply Test](#power-supply-test)  
  - [Digital Level-Shifter Tests](#digital-level-shifter-tests)  
  - [Manual Enable Test](#manual-enable-test)  
  - [Full PCB Test Suite](#full-pcb-test-suite)  
  - [On-Chip Manual Tests](#on-chip-manual-tests)  
- [License](#license)

---

## Features

- Automated power supply + power supply protection circuit test  
- Automated sequential **DT/CK/EN** digital-level shifter tests  
- Automatted **Manual enable** voltage test  
- Full run of **full PCB test suite**  
- Interactive **NMOS/PMOS current bias** confirmation  
- Interactive **ring oscillator** scope-based waveform check  

---

## Requirements

- Raspberry Pi Pico (or compatible RP2040 board)    
- ILI9341 SPI display  
- MicroPython firmware
- External Libraries:
  - LCD → [rdagger micropython-ili9341](https://github.com/rdagger/micropython-ili9341)
  - MOSbius MicroPython Flow → [Jianxun MOSbius_MicroPython_Flow](https://github.com/Jianxun/MOSbius_MicroPython_Flow) (`MOSbius.py`) 
- ADC wiring:  
  - Orange → pin 27 (sensorO)  
  - Green  → pin 26 (sensorG)  
  - Yellow → pin 28 (sensorY)  
- Output pins:  
  - DT → pin 12  
  - CK → pin 11  
  - EN → pin 10  

---

## Installation

1. Download and copy ALL FILES in `lcd_interface` folder onto your Pico's filesystem (DO NOT CHANGE FILE NAMES)
3. Ensure dependencies are installed on the Pico:  
   ```bash
   # From REPL on the Pico
   import ili9341, machine, time, interface, programChip
