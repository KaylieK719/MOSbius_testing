# Setting up each test:
## 1. PCB Tests: insert PCB into board WITHOUT chip
### 1.1 Power Test 
    - Connect GPIO 27 (ADC) to + power rail inserted into the breadboard
    - Connect Raspberry Pi Pico power to LDOI header 

### 1.2 Digital Level Shifters Test 
*Note: Each Header can be run individually or all at once `digitalLvlTestV2.py`* 
  #### 1.2.1 DT Header `dtDigitalLvlTest.py` 
    - Connect GPIO 27 (ADC) to DT pin (left cornder)
    - Connect GPIO 1 (signal source) to DT header (top) 
  #### 1.2.2 CK Header `ckDigitalLvlTest.py`
    - Connect GPIO 27 (ADC) to CK pin (left cornder)
    - Connect GPIO 1 (signal source) to CK header (top) 
  #### 1.2.3 EN Header `enDigitalLvlTest.py`
    - Connect GPIO 27 (ADC) to EN pin (left cornder)
    - Connect GPIO 1 (signal source) to EN header (top) 

### 1.3 Manual Enable Test 
    - Place jumper on EM_PU 
    - Connect LDOI to + power rail inserted into the breadboard
    - Connect GPIO 27 (ADC) to EM pin (left corner) 

## 2. Chip Tests: insert chip into board AFTER PCB tests 
### 2.1 Current Bias Potentiometer Test *Note: includes both NMOS and PMOS potentiometer tests* 
    - Connect ammeter to `I_REFN` or `I_REFP`
    - Use screwdriver to change resistance of potentiometers
### 2.2 Ring Oscillator Test 
    - Connect power, dt, clk, en jumpers to headers
    - Connect oscilloscope probes (using ADALM2000) to each stage 
  
