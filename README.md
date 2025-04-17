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
- Goggles: FATSHARK ECHO FPV Video Headset - Part Number: FSV1131-04
- Charger: SKYRC S100 neo AC/DC Smart Balance Charger
- Heavy battery: R-LINE Tattu 95C - 750mAh
- Light battery: Gaoneng LiPo Akku 4S 650mAh 15.2V
- Flight controller: SPEEDYBEE F4-40A-AIO 
- Video connector: SPEEDYBEE TX800 
- Camera: 
    + Caddx Ratel PRO MN01 - 4000B
    + Raspberry Pi Camera: RB-Camera_JT-V2-120
- Propellers: 
    + Hurricane 51477-3 Clear Blue PC 2L2R
    + EthixS4-LL-PC (2CW+2CCW)
- Propeller engine: 4x XING E-Pro 2308 2450kv
- Frame: Volador II VX5 FPV Freestyle T700 Frame Kit-Black
- Smoke stopper: TBS Smoke Stopper
- Single board computer: Raspberry Pi Zero WH PI3G
- Storage: Samsung microSDHC EVO+ MB-MC32GA/EU
- AI accelerator: Coral Google Edge TPU ML accelerator

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
    - Video transmitter: Yellow to VTX, Grün zu T3, Schwarz zu Ground A, Rot zu 5V(B)
    - Camera: Ein ende des Kabels ablösen und and die Ecke des Controllers löten
    - Raspberry Pi: Power an Ecke des Controllers mit USB-C. Kommunikation via USB-C zu Micro-usb
    - ELRS Receiver: Schwarz zu G, Rot zu 4V5, RX (Grün) zu T6, TX (Weiß) zu RX (R6)
    - Battery: Battery + and Battery -
    - 
