EESchema Schematic File Version 4
LIBS:analog-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Barrel_Jack J5
U 1 1 5D8A52A8
P 1500 6500
F 0 "J5" H 1555 6825 50  0000 C CNN
F 1 "Barrel_Jack" H 1555 6734 50  0000 C CNN
F 2 "Connect:BARREL_JACK" H 1550 6460 50  0001 C CNN
F 3 "~" H 1550 6460 50  0001 C CNN
	1    1500 6500
	1    0    0    -1  
$EndComp
$Sheet
S 2400 5900 1550 1350
U 5D8E6431
F0 "Power" 50
F1 "power.sch" 50
F2 "PWR+" I L 2400 6400 50 
F3 "PWR-" I L 2400 6600 50 
$EndSheet
Wire Wire Line
	1800 6600 2400 6600
Wire Wire Line
	1800 6400 2400 6400
Text Notes 4000 6050 0    50   ~ 10
OUTPUT: +/-9V GLOBAL\n+18V/GND GLOBAL
$Sheet
S 2450 1250 1450 850 
U 5D8EE9F6
F0 "Temperature" 50
F1 "temperature.sch" 50
F2 "RTD+" I L 2450 1550 50 
F3 "RTD-" I L 2450 1650 50 
F4 "RTD_AMP" I R 3900 1600 50 
$EndSheet
$Comp
L Connector:Conn_01x02_Female J1
U 1 1 5D8EEB88
P 1750 1650
F 0 "J1" H 1644 1325 50  0000 C CNN
F 1 "RTD conn" H 1644 1416 50  0000 C CNN
F 2 "Connectors_Phoenix:PhoenixContact_MCV-G_02x3.50mm_Vertical" H 1750 1650 50  0001 C CNN
F 3 "~" H 1750 1650 50  0001 C CNN
	1    1750 1650
	-1   0    0    1   
$EndComp
Wire Wire Line
	1950 1550 2450 1550
Wire Wire Line
	1950 1650 2450 1650
Text Notes 1550 1800 0    50   ~ 0
From external RTD
$Sheet
S 2450 4350 1450 850 
U 5D8EEE10
F0 "Pressure" 50
F1 "pressure.sch" 50
F2 "PRESSURE" I R 3900 4700 50 
$EndSheet
$Sheet
S 2450 2450 1450 850 
U 5D8EEFE9
F0 "sheet5D8EEFE4" 50
F1 "temperature.sch" 50
F2 "RTD+" I L 2450 2750 50 
F3 "RTD-" I L 2450 2850 50 
F4 "RTD_AMP" I R 3900 2800 50 
$EndSheet
$Comp
L Connector:Conn_01x02_Female J3
U 1 1 5D8EEFEF
P 1750 2850
F 0 "J3" H 1644 2525 50  0000 C CNN
F 1 "RTD conn" H 1644 2616 50  0000 C CNN
F 2 "Connectors_Phoenix:PhoenixContact_MCV-G_02x3.50mm_Vertical" H 1750 2850 50  0001 C CNN
F 3 "~" H 1750 2850 50  0001 C CNN
	1    1750 2850
	-1   0    0    1   
$EndComp
Wire Wire Line
	1950 2750 2450 2750
Wire Wire Line
	1950 2850 2450 2850
Text Notes 1550 3000 0    50   ~ 0
From external RTD
$Sheet
S 7950 4500 1650 1150
U 5D8F6AE1
F0 "Laser" 50
F1 "laser.sch" 50
F2 "LD_POWER" I L 7950 5350 50 
F3 "PD_SIGNAL" I L 7950 5250 50 
F4 "SMI_SIGNAL_AC" I L 7950 4850 50 
F5 "SMI_SIGNAL_DC" I L 7950 4700 50 
$EndSheet
$Comp
L Connector:Conn_01x03_Female J4
U 1 1 5D905871
P 7000 5350
F 0 "J4" H 6894 5025 50  0000 C CNN
F 1 "Laser Diode Conn" H 6894 5116 50  0000 C CNN
F 2 "Connectors_Phoenix:PhoenixContact_MCV-G_03x3.50mm_Vertical" H 7000 5350 50  0001 C CNN
F 3 "~" H 7000 5350 50  0001 C CNN
	1    7000 5350
	-1   0    0    1   
$EndComp
Text Notes 6300 5400 0    50   ~ 0
to laser diode\n(offboard)
Wire Wire Line
	7200 5250 7950 5250
Wire Wire Line
	7200 5350 7950 5350
$Comp
L power:GNDREF #PWR02
U 1 1 5D90642C
P 7500 5750
F 0 "#PWR02" H 7500 5500 50  0001 C CNN
F 1 "GNDREF" H 7505 5577 50  0000 C CNN
F 2 "" H 7500 5750 50  0001 C CNN
F 3 "" H 7500 5750 50  0001 C CNN
	1    7500 5750
	1    0    0    -1  
$EndComp
Wire Wire Line
	7500 5750 7500 5450
Wire Wire Line
	7500 5450 7200 5450
Wire Wire Line
	3900 1600 8100 1600
Wire Wire Line
	3900 2800 5450 2800
Wire Wire Line
	5450 2800 5450 1700
Wire Wire Line
	5450 1700 8100 1700
Wire Wire Line
	5600 1800 8100 1800
Wire Wire Line
	3900 4700 5600 4700
Wire Wire Line
	5600 4700 5600 1800
Wire Wire Line
	5750 1900 8100 1900
$Comp
L power:GNDREF #PWR01
U 1 1 5D907722
P 7150 2400
F 0 "#PWR01" H 7150 2150 50  0001 C CNN
F 1 "GNDREF" H 7155 2227 50  0000 C CNN
F 2 "" H 7150 2400 50  0001 C CNN
F 3 "" H 7150 2400 50  0001 C CNN
	1    7150 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	7150 2400 7150 2100
Wire Wire Line
	7150 2100 8100 2100
Wire Wire Line
	7950 4850 5750 4850
Wire Wire Line
	5750 1900 5750 4850
$Comp
L Connector:Conn_01x06_Female J2
U 1 1 5DAC4DEB
P 8300 1800
F 0 "J2" H 8327 1776 50  0000 L CNN
F 1 "Conn_01x06_Female" H 8327 1685 50  0000 L CNN
F 2 "Connectors_Phoenix:PhoenixContact_MCV-G_06x3.50mm_Vertical" H 8300 1800 50  0001 C CNN
F 3 "~" H 8300 1800 50  0001 C CNN
	1    8300 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	7950 4700 5900 4700
Wire Wire Line
	5900 4700 5900 2000
Wire Wire Line
	5900 2000 8100 2000
Text Notes 6500 1500 0    50   ~ 0
outputs between +/- 0.75V
Text Notes 5100 900  0    100  ~ 20
High Level Connections
$EndSCHEMATC
