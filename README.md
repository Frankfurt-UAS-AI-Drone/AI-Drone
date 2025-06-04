# AI-Drone

## Proof of Concept - Banana Stalker

We set ourselves a defined and achievable goal in the initial phase of the project:

A drone with integrated object detection which autonomously follows an object of a predefined type (for example a banana). 

Key attributes of the drone:

- Long range / low to medium speed
- Able to lift atleast additional 50g

---

## Hardware selection
### Initial components
- Propeller: HQProp T2-8X2-4X3GP-PC 2,8 Zoll 3-Blatt Propeller Grau (2CW+2CCW) (Gewicht: 4 a 1.83g/Propeller = 7.32g, Preis: 2,90€)
	+ 2CW (Clock-Wise), 2CCW (Counter-Clock-Wise)
    + Dickere Propeller, Traglast/"Power" > Geschwindigkeit
	
- Frame: FlyFishRC Volador VX3.5 O3 Freestyle Frame Kit 3.5 Zoll schwarz (Gewicht: 1 a 70.5g = 70.5g, Preis: 35,90€)
	+ Sieht gut aus und hat ein entsprechendes Gewicht
	
- Flight Controller (FC)/Electronic Speed Controller (ESC): SpeedyBee F405 AIO 40A Bluejay 3-6S FPV Flight Controller (Gewicht: 1 a 13.6g = 13.6g, Preis: 69,90€)
	+ All-in-One (AIO): FC + ESC, kompakte Bauweise (25,5 x 25,5mm)
	+ bestellt durch Prof. Baun

- Motoren: Flywoo NIN 1404 V2 3750KV FPV Motor Titan (Gewicht: 4 a 9.5/Motor = 38g, Preis: 16,90€)
	+ kompatible Akkus: 4S 650mAh, 750mAh, 850mAh, 1000mAh
	
- Batterie: Tattu R-Line Lipo Akku Long Pack 850mAh 4S 15.2V 95C XT30U-F (Gewicht: 1 a 74g (+- 20g), Preis: 22,90€)
	+ Größere Flugzeit als 650 mAh (nur 1 Minute auf full-throttle laut ChatGPT)
    + +- 20g Gewicht nicht genau bekannt, ggf. Ladezustand

- Ladegerät: SkyRC S100 Neo Ladegerät Charger LiPo 1-6s 10A 100W AC (Preis: 57,90€)
	+ Schnelles laden (bestellt durch Prof. Baun)

- Kamera: Caddx Ratel Pro Analog FPV Kamera 1500TVL Schwarz (Gewicht: 1 a 9.5g = 9.5g, Preis: 54,90€)
	+ Analog, kann Tag und Nacht, Weitwinkel, bestellt durch Prof. Baun

- Video Transmitter: SpeedyBee TX800 FPV VTX (Gewicht: 1 a 5.6g = 5.6g, Preis: 38,90€)
	+ bestellt durch Prof. Baun

- Video Receiver ELRS: SpeedyBee Nano 2.4GHz ELRS Empfänger (Gewicht: 1 a (0.7g + 0.6g Antenne) = 1,3g, Preis: 11,90€)
	-> hat er schon bestellt

- Brille: Fat Shark FPV Videobrille Goggles ECHO (Preis: 129,90€)
	-> für analoge Videos

- RC Controller: Radiomaster Pocket ELRS RC Fernsteuerung Transparent Grau (Preis: 78,90€)
	-> hat er schon bestellt (glaube ich)

**Gesamtgewicht: 229,32g (+-20g)**

**Gesamtpreis: 520,90€**



### Removed parts

### Additional parts

### Final parts list
- Remote controller: Radiomaster Boxer ELRS GRYM2
- ![Radiomaster Boxer ELRS GRYM2](https://github.com/user-attachments/assets/4adf8ed4-f03f-4ecb-ad39-d1dbb5ff5a88)
- Goggles: FATSHARK ECHO FPV Video Headset - Part Number: FSV1131-04
- ![FATSHARK ECHO FPV Video Headset  Part Number FSV113104](https://github.com/user-attachments/assets/0145a024-5f2b-45b6-9705-da1cc0ebc2b3)
- Charger: SKYRC S100 neo AC/DC Smart Balance Charger
- ![SKYRC S100 neo ACDC Smart Balance Charger](https://github.com/user-attachments/assets/b35d5ff0-f878-428d-853c-3ee3fe6bcec9)
- Heavy battery: R-LINE Tattu 95C - 750mAh
- ![RLINE Tattu 95C  750mAh](https://github.com/user-attachments/assets/5f975007-0e8f-49c7-a3bd-7873df062c15)
- Light battery: Gaoneng LiPo Akku 4S 650mAh 15.2V
- ![Gaoneng LiPo Akku 4S 650mAh](https://github.com/user-attachments/assets/b190d3b9-eec9-43b0-8376-fe19a671c3a8)
- Flight controller: SPEEDYBEE F4-40A-AIO
- ![SPEEDYBEE F440AAIO](https://github.com/user-attachments/assets/6e0381af-ce7d-42b8-8952-ee0ca2a79f7b)
- Video connector: SPEEDYBEE TX800
- ![SPEEDYBEE TX800](https://github.com/user-attachments/assets/8626cc11-8d90-4382-bc53-8b9d50c9d130)
- Camera: 
    + Caddx Ratel PRO MN01 - 4000B
    + ![Caddx Ratel PRO MN01 4000B](https://github.com/user-attachments/assets/a70b9940-852c-4d9c-a8c5-6bd6b7b3c6fd)
    + Raspberry Pi Camera: RB-Camera_JT-V2-120
    + ![Raspberry Pi Camera RBCamera_JTV2120](https://github.com/user-attachments/assets/cac13b23-45ce-48fe-9eee-c64ce7497e05)
- Propellers: 
    + Hurricane 51477-3 Clear Blue PC 2L2R
    + ![Hurricane 514773 Clear Blue PC 2L2R](https://github.com/user-attachments/assets/b917f35a-fa97-4a60-b910-e3395011b26b)
    + EthixS4-LL-PC (2CW+2CCW)
    + ![EthixS4LLPC (2CW+2CCW)](https://github.com/user-attachments/assets/375c510a-bc02-4880-a5ab-9c0989cb4da5)
- Propeller engine: 4x XING E-Pro 2308 2450kv
- Frame: Volador II VX5 FPV Freestyle T700 Frame Kit-Black
- ![Volador II VX5 FPV Freestyle T700 Frame KitBlack](https://github.com/user-attachments/assets/a61b6ecd-448b-4420-9caf-d5142df20b10)
- Smoke stopper: TBS Smoke Stopper
- ![TBS Smoke Stopper](https://github.com/user-attachments/assets/a22b24e2-8f63-4cc3-8b30-570295c3c4cc)
- Single board computer: Raspberry Pi Zero WH PI3G
- ![Raspberry Pi Zero WH PI3G](https://github.com/user-attachments/assets/b2f03447-e45f-4378-a3f8-38b82df81dcf)
- Storage: Samsung microSDHC EVO+ MB-MC32GA/EU
- ![Samsung microSDHC EVO+ MBMC32GAEU](https://github.com/user-attachments/assets/16a44967-3cef-4965-b33a-8c88ee5f1853)
- AI accelerator: Coral Google Edge TPU ML accelerator
- ![Coral Google Edge TPU ML accelerator](https://github.com/user-attachments/assets/a86a48e5-1b78-4d44-b2a3-e914d33bc955)


## Software:

- **Ardupilot:** This is the autopilot firmware that runs on the flight controller hardware. It handles the core flight stabilization, navigation, sensor reading, and control logic. Think of it as the drone's "operating system."
    - Supports "SpeedyBee F405 V3".
	- Uses **MAVLink (Micro Air Vehicle Link)**: This is the communication protocol that ArduPilot (and PX4) primarily uses to talk to the outside world - specifically Ground Control Stations (GCS) like Mission Planner/QGroundControl, companion computers (like a Raspberry Pi), and other MAVLink-aware devices. It defines a standard set of messages for sending commands (like "go to waypoint," "arm," "change flight mode") and receiving data (like GPS position, altitude, battery voltage, attitude).
	- Works with the Pythn Dronekit.
	- Alternatives:
		- **PX4:** Does not support "SpeedyBee F405 V3"
		- **Betaflight:** Does not use MAVLink

- **Raspberry Pi OS Lite:** The official OS from the Raspberry Pi Foundation, specifically stripped down for devices like the Zero.
(https://www.raspberrypi.com/software/operating-systems/)
    - **Raspberry Pi Imager**, Guide: https://www.youtube.com/watch?v=yn59qX-Td3E

- **Python Dronekit:** Library for controlling the drone through Python code using the MAVLink protocol under the hood.


## Anschlussplan
- TODO: Make a graphic schematic.
- Flight Controller:
    - 4 Motoren: Jeweil an Motor 1-4 (Mapping kann in der Firmware erfolgen)
    - ![Motor and Power Cabel Wires](https://github.com/user-attachments/assets/a2c0cc8a-4f55-4a8a-bb12-4fffb33648a3)
      
    - Video transmitter: Yellow to VTX, Grün zu T3, Schwarz zu Ground A, Rot zu 5V(B)
    - ![Analog VTX Connection Wire](https://github.com/user-attachments/assets/7be183e3-ed4c-479a-bf2f-3e61480d98b1)
      
    - Camera: Ein ende des Kabels ablösen und and die Ecke des Controllers löten
    - ![Camera zu Menu Board](https://github.com/user-attachments/assets/9e980b05-f491-4ae1-89ca-7c9d233cdc9c)

    - Raspberry Pi: Power an Verlängerung des Controllers mit 5V (PP1)/GND (PP6) Anschließen. Kommunikation via Data + (PP22) Data - (PP23)
    - ![Pi Power Anschluss Rueckseite](https://github.com/user-attachments/assets/d7a57e30-853c-4a0b-abb1-b59ea10bdfbf)
    - ![Power Expander](https://github.com/user-attachments/assets/f73d136a-1662-44c5-b087-f6eaa22abd16)

    - ELRS Receiver: Schwarz zu G, Rot zu 4V5, RX (Grün) zu T6, TX (Weiß) zu RX (R6)
    - ![ELRS Receiver Connection Wire](https://github.com/user-attachments/assets/ac138282-b6d5-46f5-80b2-f327775bc414)

    - Battery: Battery + and Battery -
    - ![Motor and Power Cabel Wires](https://github.com/user-attachments/assets/dd43df77-3be3-4b10-884c-460a0c77ebef)
 
    - TYP-C USB -
    - ![Typ-C Extern](https://github.com/user-attachments/assets/f95ba354-f742-484a-bd3c-ed8984650e06)
 
    - GPS Module -
    - ![GPS Modul Wire](https://github.com/user-attachments/assets/5e98777f-95f9-4d4e-a9cd-49165bcf5ae7)

# Radiomaster Boxer notes
## Startup Warnings
- **Throttle Warning** – Throttle (left) stick is not at the lowest position when turned on 
- **Switch Warning** (aka Control Warning) – some of the switches are not in their default positions. -> Put all the switches to UP position (pointing away) to remove this warning.
- **Alarms Warning** – This warning will appear if Sound mode is set to mute
- **SD Card Warning** – SD card content version does not match the firmware version. -> [Fix](https://oscarliang.com/fix-sd-card-warning-opentx/)
## Channel Mappings
- The two ***most common channel map settings*** for FPV drones are:
	- AETR (Aileron, Elevator, Throttle, Rudder) -> Betaflight default (AETR1234):
		- *CH 1:* **A (Aileron)** = Roll (left/right)
		- *CH 2:* **E (Elevator)** = Pitch (forward/backward)
		- *CH 3:* **T (Throttle)** = Throttle (speed up/down)
		- *CH 4:* **R (Rudder)** = Yaw (rotate left/right)
	- TAER (Throttle, Aileron, Elevator, Rudder) -> Different betaflight option

- ***Channel order*** for the drone can be viewed on the MIXES page in any EdgeTX radio.
- Channel order can also be set up in EdgeTX in the remote controller itself. -> Process:
	1. From the home screen, press the **Model** button. 
	2. Navigate to **Mixes** tab by pressing the *Page* button until the heading shows up.
	3. The following maps the channels according to the AETR (Betaflight default):
		1. **Channel 1 (Roll)**:
		    - Highlight **CH1** using the jog wheel and press to enter the setup.
		    - Set **Source** to *aileron* stick. -> Optionally, adjust **Weight** (how much stick movement passed to output) or apply **Expo** for smoother control.
		2. **Channel 2 (Pitch)** -> Highlight **CH2** and set the **Source** to the *elevator* stick.
		3. **Channel 3 (Throttle)** -> Highlight **CH3** and set the **Source** to the *throttle* stick.
		4. **Channel 4 (Yaw)** -> Highlight **CH4** and set the **Source** to the *rudder* stick.
	
- To set the ***default channel*** order in EdgeTX do the following:
	1. Press the **SYS** button and navigate to the *Settings* tab with the **PAGE** button.
	2. Scroll down to find the *Default Channel Order* setting and set it to **AETR**
	3. Press return to save the changes.

- ***Setting up switches*** -> for uses like arming, flight modes or GPS rescue:
	- It is recommended to use *CH 5* for the **Arm switch** -> Process:
		1. Navigate to Mixes page, highlight CH 5 and press jog wheel to enter settings
		2. Scroll to source and flip the switch you want to use for arming (e.g. SA & SD)
		3. Leave the remaining values default and save the settings.
	- For configuring **flight modes** a 3-position switch is recommended (e.g. SC & SD):
		- To achieve this, repeat the process to assign a switch to e.g. *CH 6*

- ***Testing*** the channel mapping setup:
	1. Connect your drone and open the Receiver tab in Betaflight Configurator
	2. Move the sticks and see if the corresponding channels respond correctly.
		1. CH 5 corresponds to AUX 1, CH 6 corresponds to AUX 2 and so on...

- ***Setting up modes*** in Betaflight *(Requires channels to be set up)*:
	1. Go to the modes tab in the Betaflight Configurator
	2. Select the mode (e.g. ARM) and click "Add Range"
	3. Select AUX 1 (CH 5) and drag the range to the desired position.
		1. For a 2 position switch: UP = 1000 and DOWN = 2000
		2. For a 3 position switch: UP = 1000, MID = 1500 and DOWN = 2000

- ***The most important modes are:***
	- **ARM** - Starts the motors -> Should be immediately disabled upon a crash
		- *MOTOR STOP* option only spins motors, once throttle is increased.
	- **ACRO** - Drone files without any assistance from the FC. -> Every movement will require direct command input from the pilot. -> *"Ultimate flight mode"*
	- **ACRO TRAINER** - Acro mode with tilt angle limit to prevent drone from flipping over.
	- **ANGLE** - Drone self-levels when the sticks are released to the centered position.
		- Limits the max. tilt angle -> *Requires accelerometer to be activated.*
	- **HORIZON** - Angle mode with ability to do flips, when the stick passes a threshold.
		- *Requires accelerometer to be activated.*
	- **GPS RESCUE** - Let's the drone fly back from where it took off (requires GPS module)
	- **FAILSAFE** - Simulates failsafe (for testing), which occurs in the event of RC link loss.
	- **ANTI GRAVITY** - Reduces sudden dips on rapid throttle changes
	- **BLACKBOX** - Start/stop blackbox logging
	- **FLIP OVER AFTER CRASH** - Flip quad if stuck upside down to take off after a crash

# Raspberry Pi notes
- Use 32-Bit slim image (V1.1) or a 64-Bit slim image (V2) for better performance
	- Default device name is `bananapi` -> `pi` user has passphrase `banana`
	- Configure the Pi to use a WiFi of your choosing and allow SSH with passphrase
	- `dtoverlay=imx219 & camera_auto_detect=0` to `/boot/config.txt` for [Camera](https://joy-it.net/de/products/rb-camera-jt-v2-120)
		- Test the camera with `libcamera-hello`
	- Find the IP-Address of the Raspberry pi and connect to it with pi@ipaddress
	- Install [libedgetpu1-std](https://coral.ai/docs/accelerator/get-started/#runtime-on-linux) 
	- Install python3-pycoral (requires python < 3.10)
	- Install python3-opencv (requires python < 3.12)
	- Install python3-picamera2
	- Install pip3 -> MultiWii (requires python > 3.7)and pyserial
	- Install the Docker Engine using the guide for [Debian](https://docs.docker.com/engine/install/debian/) NOT SUPPORTED YET!!!
		- Maybe useful for other components or if the camera can be made to work with the legacy camera stack (no picamera2 available) 
