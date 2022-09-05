# 4G Surveillance Drone (prototype)
###### By Oluwafemi Oreoluwa
In the partial fulfillment of the requirements for the award of the Bachelor of Engineering in Computer Engineering, I began the engineering design of an e-UAV and completed implementation four days to final year defense.This project aimed at reducing CO2 emissions contributed during aerial surveillance in the aviation industry by introducing a Network of electric 4G Surveillance Unmanned Aerial Vehicles.


## Requirements

| Minimum Hardware Requirements    | Software Requirements |
|-----------|------------|
|	500 Gigabyte Secondary Storage (SDD /HDD)|  Operating Systems Mininum:Microsoft Windows 10 |
| Network Interface card (NIC) capable of setting up a hotspot connection |   |
| 4GB Random Access memory stick (RAM)   | 


## Design 
| System Design |  Network Diagram | 
|--------------|-----------|
| ![image](https://user-images.githubusercontent.com/75027292/186240077-b275ccb4-2f3e-41ff-a0a3-b5ef013c380b.png) |![image](https://user-images.githubusercontent.com/75027292/186240302-cc7d08a3-3ad2-48c3-a4b1-305490a04321.png) |

## Bill of Materials (In progress....) 
The components listed in the table below is for a quadcoper configuration. Although, the quantity of some components may vary for othe configurations 
| Components       | Description   | Quantity|  ₦Price (2022) |
|--------------|-----------|------------| ------------|
|[1045 Propeller](https://binged.it/3Bm6YIN) | Description: Item name: 1045 Propeller Diameter: 10in Pitch: 4.5in Propeller diameter: 25.4cm Centre bore diameter : 6mm front and 9mm reverse side. Centre seat TH: 6mm Weight: about 14g/pair |  4 |2,091.69|
|[Aluminium Sheet 500mm x 500mm ](https://binged.it/3QfUJ4k) | Aluminium is a chemical element with the symbol Al and atomic number 13. Aluminium has a density lower than those of other common metals, at approximately one third that of steel.  |  1 | 15,000.00|
|[3S 5000mAh 11.1v Battery. 60c XT60 ](https://binged.it/3AJzNxb)  | An electric battery is a source of electric power consisting of one or more electrochemical cells with external connections for powering electrical devices. The battery utilized in the prototype comprises of 3 cells , appreviated (3S)  |   1 | 30,000.00 |
| [Raspberry Pi Zero WH](https://binged.it/3q7gxov) | Raspberry Pi is a series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation in association with Broadcom. The Raspberry Pi Zero W extends the Pi Zero family and comes with added wireless LAN and Bluetooth connectivity. | 1  | 35,778.99 |
| [Raspberry Pi Zero Camera](https://binged.it/3KS7lOk)  | Raspberry Pi currently sell two types of camera board: an 8MP device and a 12MP High Quality (HQ) camera. The 8MP device is also available in NoIR form without an IR filter. The original 5MP device is no longer available from Raspberry Pi.All Raspberry Pi cameras are capable of taking high-resolution photographs, along with full HD 1080p video, and can be fully controlled programmatically. |   1 | 3,522.85 |
|[Pi Zero WH Flex Cable](https://binged.it/3cLv2Lu) | The Cable for the raspberry pi zero is different|   1 | 1,748.72 |
|[Bolt and Nut](https://binged.it/3D4u3k6) | fastening materials |  30 | 7,000.00 |
|[Zip Ties](https://binged.it/3AKdaZj)  | fastening materials |  20 | 563.15  |
|[Battery Charger](https://binged.it/3wU4ZZu)  | The module charges the 5200mAh 11.1v battery  | 1  | 3,836.19 |
|[Electronic Speed Controller 40A](https://bit.ly/oreesc)   | An electronic speed control is an electronic circuit that controls and regulates the speed of an electric motor| 4 | 8,300.35|
|[Ardupilot Flight Controller](https://binged.it/3q9LS9Z) | ArduPilot is a trusted, versatile, and open source autopilot system supporting many vehicle types: multi-copters, traditional helicopters, fixed wing aircraft, boats, submarines, rovers and more  | 1  | 23,313.15  |
|[ 2300kv Brushless Motor](https://binged.it/3ATJXLQ) | It has a strong and unique performance thanks to its quality copper windings. 2300KV is the best quality motor model you can buy in the brushless motor category. Features: KV (rpm/v): 2300. Material: Metal. Rotation: CW. Motor diameter: 28mm. Motor height: 15mm (shaft excluded) Shaft diameter: 5mm. | 4  | 14,000.00  |
|[FS-IA6 Controller](https://binged.it/3eovbVL) | Channels: 6 Channels,Model type: Airplane / Glider / Helicopter / Multirotor,Frequency range: 2.4--2.48GHZ,Band width number: 160,Transmitting power: not more than 20dBm,RF receiver sensitivity: -105dbm,2.4G modes: automatic frequency second generation digital systems,Encoding: GFSK,Antenna length: 26mm,Input power: 4.0-6.5V DC,Dimension: 40 * 21 * 7mm,Weight: 6.4g,Color: Black,i-Bus interface: No,Data acquisition interface: None | 1  | 19,384.17 |


## Ground Station Software
The Mission planner software is a ground station application I used for my final year project.Note: some versions are buggy although the software works if you follow the installation and setup instructions properly

- [ ] [About Mission Planner](https://ardupilot.org/planner/docs/mission-planner-overview.html)  
- [ ] [Install Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html)  

## End Results 
| Frame Material  | Full Assembly  | Flight |
|--------------|-----------|------------|
| ![image](https://user-images.githubusercontent.com/75027292/186236744-8c30b7e8-f129-4f69-8ac2-61a19b94e8e3.png)|  ![image](https://user-images.githubusercontent.com/75027292/186237465-8e3c2c9b-1934-495d-a1f7-fc9e90147f48.png) | ![image](https://user-images.githubusercontent.com/75027292/186239196-a33fff34-c9ae-4228-909a-4655c8b2fd27.png)|
|![image](https://user-images.githubusercontent.com/75027292/186236875-5cd0b15d-be1e-4f40-8713-ed92fbd48646.png) | ![image](https://user-images.githubusercontent.com/75027292/186237381-5bd7bc6a-ad53-40de-bc78-2130f1bb2b81.png)|![image](https://user-images.githubusercontent.com/75027292/186239565-ac8e6164-e1e8-4640-a357-9d2af41c9338.png)|

## Useful Tutorials
- [ ] [How to make Quadcopter frame]( https://www.youtube.com/watch?v=H6jjlcwGJwY&list=PL4B0LEKY-jrR5_988bfV39yGzMQSas-v4)  
- [ ] [How to make Quadcopter drone with APM 2.8 and GPS | APM 2.8 connections (Part 1) | step by step](https://youtu.be/UW1-gSySgxg)  
- [ ] [APM 2.8 flight controller setup | How to make Quadcopter with APM2.8(Part 2) | Mission planner setup](https://www.youtube.com/watch?v=S7VZ796W8VA)  
- [ ] [APM 2.5 Ardupilot controller- setup guide 1 of 4](https://www.youtube.com/watch?v=QAFdHnoae0s)  
- [ ] [Autonomous Drone with ArduCopter pixhawk and OpenCV.](https://youtu.be/Nrzs3dQ9exw)  
