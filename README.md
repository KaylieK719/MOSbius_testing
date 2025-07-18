# MOSbius Test Helper Functions

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

- Automated **power rail** voltage check  
- Sequential **DT/CK/EN** digital-level shifter tests  
- **Manual enable** voltage test  
- One-button run of **full PCB test suite**  
- Interactive **NMOS/PMOS current bias** confirmation  
- Interactive **ring oscillator** scope-based waveform check  

---

## Requirements

- Raspberry Pi Pico (or compatible RP2040 board)  
- MOSbius PCB programmed via `programChip` module  
- ILI9341 SPI display  
- MicroPython firmware  
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

1. Clone or download this repository.  
2. Copy `helperFunctions.py` into your Pico’s filesystem.  
3. Ensure dependencies are installed on the Pico:  
   ```bash
   # From REPL on the Pico
   import ili9341, machine, time, interface, programChip
