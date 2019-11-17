EESchema Schematic File Version 4
LIBS:analog-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 1700 2550 0    50   Input ~ 0
PWR+
Text HLabel 1700 4800 0    50   Input ~ 0
PWR-
$Comp
L Device:C C?
U 1 1 5D8E742A
P 4150 3700
AR Path="/5D8E742A" Ref="C?"  Part="1" 
AR Path="/5D8E6431/5D8E742A" Ref="C3"  Part="1" 
F 0 "C3" H 4265 3746 50  0000 L CNN
F 1 "220uF" H 4265 3655 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 4188 3550 50  0001 C CNN
F 3 "~" H 4150 3700 50  0001 C CNN
	1    4150 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 2550 4150 3550
$Comp
L Device:R_US R?
U 1 1 5D8E7436
P 6000 3100
AR Path="/5D8E7436" Ref="R?"  Part="1" 
AR Path="/5D8E6431/5D8E7436" Ref="R2"  Part="1" 
F 0 "R2" H 6068 3146 50  0000 L CNN
F 1 "220K, 1%" H 6068 3055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6040 3090 50  0001 C CNN
F 3 "~" H 6000 3100 50  0001 C CNN
	1    6000 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 5D8E743D
P 6000 4350
AR Path="/5D8E743D" Ref="R?"  Part="1" 
AR Path="/5D8E6431/5D8E743D" Ref="R4"  Part="1" 
F 0 "R4" H 6068 4396 50  0000 L CNN
F 1 "220K, 1%" H 6068 4305 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6040 4340 50  0001 C CNN
F 3 "~" H 6000 4350 50  0001 C CNN
	1    6000 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 2550 4800 2550
Wire Wire Line
	6000 2550 6000 2950
Text Notes 1800 2550 0    50   ~ 0
“dirty”
Text Notes 3150 2550 0    50   ~ 0
“clean”
Wire Wire Line
	4150 3850 4150 4800
Wire Wire Line
	6000 4500 6000 4800
Connection ~ 4150 4800
Wire Wire Line
	6000 4200 6000 3650
$Comp
L Amplifier_Operational:TL081 U?
U 1 1 5D8E745B
P 7300 3750
AR Path="/5D8E745B" Ref="U?"  Part="1" 
AR Path="/5D8E6431/5D8E745B" Ref="U3"  Part="1" 
F 0 "U3" H 7641 3796 50  0000 L CNN
F 1 "TL081" H 7641 3705 50  0000 L CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 7350 3800 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tl081.pdf" H 7450 3900 50  0001 C CNN
	1    7300 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 3650 6000 3650
Connection ~ 6000 3650
Wire Wire Line
	6000 3650 6000 3250
Wire Wire Line
	7200 3450 7200 3100
Wire Wire Line
	7200 4800 6000 4800
$Comp
L Device:R_US R?
U 1 1 5D8E7469
P 8200 3750
AR Path="/5D8E7469" Ref="R?"  Part="1" 
AR Path="/5D8E6431/5D8E7469" Ref="R3"  Part="1" 
F 0 "R3" V 7995 3750 50  0000 C CNN
F 1 "100" V 8086 3750 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8240 3740 50  0001 C CNN
F 3 "~" H 8200 3750 50  0001 C CNN
	1    8200 3750
	0    1    1    0   
$EndComp
$Comp
L Device:C C?
U 1 1 5D8E7470
P 7950 3950
AR Path="/5D8E7470" Ref="C?"  Part="1" 
AR Path="/5D8E6431/5D8E7470" Ref="C5"  Part="1" 
F 0 "C5" H 8065 3996 50  0000 L CNN
F 1 "10pF" H 8065 3905 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 7988 3800 50  0001 C CNN
F 3 "~" H 7950 3950 50  0001 C CNN
	1    7950 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6850 3850 7000 3850
$Comp
L smi:BUF634A U?
U 1 1 5D8E7478
P 9000 3700
AR Path="/5D8E7478" Ref="U?"  Part="1" 
AR Path="/5D8E6431/5D8E7478" Ref="U2"  Part="1" 
F 0 "U2" H 9541 3746 50  0000 L CNN
F 1 "BUF634A" H 9541 3655 50  0000 L CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 9000 3700 50  0001 C CNN
F 3 "" H 9000 3700 50  0001 C CNN
	1    9000 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	8650 3750 8350 3750
Wire Wire Line
	9050 4050 9050 4500
Wire Wire Line
	9050 4800 7200 4800
Connection ~ 7200 4800
NoConn ~ 7300 4050
NoConn ~ 7400 4050
Wire Wire Line
	7600 3750 7950 3750
Wire Wire Line
	7950 4100 7950 4200
Wire Wire Line
	7950 4200 6850 4200
Wire Wire Line
	6850 4200 6850 3850
Wire Wire Line
	7950 3800 7950 3750
Connection ~ 7950 3750
Wire Wire Line
	7950 3750 8050 3750
Wire Wire Line
	7200 4050 7200 4550
NoConn ~ 8650 3650
Wire Wire Line
	9050 2550 9050 3150
Wire Wire Line
	6000 2550 7200 2550
Connection ~ 7200 2550
Wire Wire Line
	7200 2550 9050 2550
Wire Wire Line
	7950 4200 9500 4200
Wire Wire Line
	9500 4200 9500 3700
Connection ~ 7950 4200
$Comp
L power:GNDREF #PWR?
U 1 1 5D8E7495
P 10200 3850
AR Path="/5D8E7495" Ref="#PWR?"  Part="1" 
AR Path="/5D8E6431/5D8E7495" Ref="#PWR06"  Part="1" 
F 0 "#PWR06" H 10200 3600 50  0001 C CNN
F 1 "GNDREF" H 10205 3677 50  0000 C CNN
F 2 "" H 10200 3850 50  0001 C CNN
F 3 "" H 10200 3850 50  0001 C CNN
	1    10200 3850
	1    0    0    -1  
$EndComp
Connection ~ 9500 3700
Wire Wire Line
	10200 3700 9500 3700
Wire Wire Line
	10200 3850 10200 3700
$Comp
L power:-9V #PWR?
U 1 1 5D8E74A1
P 9600 4950
AR Path="/5D8E74A1" Ref="#PWR?"  Part="1" 
AR Path="/5D8E6431/5D8E74A1" Ref="#PWR09"  Part="1" 
F 0 "#PWR09" H 9600 4825 50  0001 C CNN
F 1 "-9V" H 9615 5123 50  0000 C CNN
F 2 "" H 9600 4950 50  0001 C CNN
F 3 "" H 9600 4950 50  0001 C CNN
	1    9600 4950
	-1   0    0    1   
$EndComp
Wire Wire Line
	9600 4950 9600 4800
Wire Wire Line
	9600 4800 9050 4800
Connection ~ 9050 4800
Wire Wire Line
	9600 2550 9050 2550
Connection ~ 9050 2550
Wire Wire Line
	9600 2350 9600 2550
$Comp
L Device:C_Small C?
U 1 1 5D8E74B4
P 7400 4550
AR Path="/5D8E74B4" Ref="C?"  Part="1" 
AR Path="/5D8E6431/5D8E74B4" Ref="C7"  Part="1" 
F 0 "C7" V 7171 4550 50  0000 C CNN
F 1 "0.1uF" V 7262 4550 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 7400 4550 50  0001 C CNN
F 3 "~" H 7400 4550 50  0001 C CNN
	1    7400 4550
	0    1    1    0   
$EndComp
Wire Wire Line
	7300 4550 7200 4550
Connection ~ 7200 4550
Wire Wire Line
	7200 4550 7200 4800
$Comp
L power:GNDREF #PWR?
U 1 1 5D8E74BE
P 7500 4550
AR Path="/5D8E74BE" Ref="#PWR?"  Part="1" 
AR Path="/5D8E6431/5D8E74BE" Ref="#PWR08"  Part="1" 
F 0 "#PWR08" H 7500 4300 50  0001 C CNN
F 1 "GNDREF" V 7505 4422 50  0000 R CNN
F 2 "" H 7500 4550 50  0001 C CNN
F 3 "" H 7500 4550 50  0001 C CNN
	1    7500 4550
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5D8E74C4
P 7400 3100
AR Path="/5D8E74C4" Ref="C?"  Part="1" 
AR Path="/5D8E6431/5D8E74C4" Ref="C1"  Part="1" 
F 0 "C1" V 7171 3100 50  0000 C CNN
F 1 "0.1uF" V 7262 3100 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 7400 3100 50  0001 C CNN
F 3 "~" H 7400 3100 50  0001 C CNN
	1    7400 3100
	0    1    1    0   
$EndComp
Wire Wire Line
	7300 3100 7200 3100
Connection ~ 7200 3100
Wire Wire Line
	7200 3100 7200 2550
$Comp
L power:GNDREF #PWR?
U 1 1 5D8E74CE
P 7500 3100
AR Path="/5D8E74CE" Ref="#PWR?"  Part="1" 
AR Path="/5D8E6431/5D8E74CE" Ref="#PWR04"  Part="1" 
F 0 "#PWR04" H 7500 2850 50  0001 C CNN
F 1 "GNDREF" V 7505 2972 50  0000 R CNN
F 2 "" H 7500 3100 50  0001 C CNN
F 3 "" H 7500 3100 50  0001 C CNN
	1    7500 3100
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5D8E74D4
P 9250 3150
AR Path="/5D8E74D4" Ref="C?"  Part="1" 
AR Path="/5D8E6431/5D8E74D4" Ref="C2"  Part="1" 
F 0 "C2" V 9021 3150 50  0000 C CNN
F 1 "0.1uF" V 9112 3150 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 9250 3150 50  0001 C CNN
F 3 "~" H 9250 3150 50  0001 C CNN
	1    9250 3150
	0    1    1    0   
$EndComp
Wire Wire Line
	9150 3150 9050 3150
$Comp
L power:GNDREF #PWR?
U 1 1 5D8E74DC
P 9350 3150
AR Path="/5D8E74DC" Ref="#PWR?"  Part="1" 
AR Path="/5D8E6431/5D8E74DC" Ref="#PWR05"  Part="1" 
F 0 "#PWR05" H 9350 2900 50  0001 C CNN
F 1 "GNDREF" V 9355 3022 50  0000 R CNN
F 2 "" H 9350 3150 50  0001 C CNN
F 3 "" H 9350 3150 50  0001 C CNN
	1    9350 3150
	0    -1   -1   0   
$EndComp
Connection ~ 9050 3150
Wire Wire Line
	9050 3150 9050 3350
$Comp
L Device:C_Small C?
U 1 1 5D8E74E4
P 9250 4500
AR Path="/5D8E74E4" Ref="C?"  Part="1" 
AR Path="/5D8E6431/5D8E74E4" Ref="C6"  Part="1" 
F 0 "C6" V 9021 4500 50  0000 C CNN
F 1 "0.1uF" V 9112 4500 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder" H 9250 4500 50  0001 C CNN
F 3 "~" H 9250 4500 50  0001 C CNN
	1    9250 4500
	0    1    1    0   
$EndComp
Wire Wire Line
	9150 4500 9050 4500
$Comp
L power:GNDREF #PWR?
U 1 1 5D8E74EC
P 9350 4500
AR Path="/5D8E74EC" Ref="#PWR?"  Part="1" 
AR Path="/5D8E6431/5D8E74EC" Ref="#PWR07"  Part="1" 
F 0 "#PWR07" H 9350 4250 50  0001 C CNN
F 1 "GNDREF" V 9355 4372 50  0000 R CNN
F 2 "" H 9350 4500 50  0001 C CNN
F 3 "" H 9350 4500 50  0001 C CNN
	1    9350 4500
	0    -1   -1   0   
$EndComp
Connection ~ 9050 4500
Wire Wire Line
	9050 4500 9050 4800
$Comp
L power:GNDPWR #PWR010
U 1 1 5D8F0EE2
P 3950 5250
F 0 "#PWR010" H 3950 5050 50  0001 C CNN
F 1 "GNDPWR" H 3954 5096 50  0000 C CNN
F 2 "" H 3950 5200 50  0001 C CNN
F 3 "" H 3950 5200 50  0001 C CNN
	1    3950 5250
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 5250 3950 4800
Wire Wire Line
	3950 4800 4150 4800
$Comp
L smi:+18V #U01
U 1 1 5D8F2BC9
P 3950 2150
F 0 "#U01" H 3950 2150 50  0001 C CNN
F 1 "+18V" H 4008 2137 50  0000 L CNN
F 2 "" H 3950 2150 50  0001 C CNN
F 3 "" H 3950 2150 50  0001 C CNN
	1    3950 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 2200 3950 2550
Wire Wire Line
	3950 2550 4150 2550
$Comp
L power:+9V #PWR03
U 1 1 5D8F6D7D
P 9600 2350
F 0 "#PWR03" H 9600 2200 50  0001 C CNN
F 1 "+9V" H 9615 2523 50  0000 C CNN
F 2 "" H 9600 2350 50  0001 C CNN
F 3 "" H 9600 2350 50  0001 C CNN
	1    9600 2350
	1    0    0    -1  
$EndComp
Text Notes 6600 2500 0    50   ~ 0
+18V & +9V intentionally shorted
Text Notes 6600 4900 0    50   ~ 0
GNDPWR & -9V intentionally shorted
Connection ~ 3950 2550
Connection ~ 3950 4800
Connection ~ 4150 2550
$Comp
L Regulator_Linear:L7818 U13
U 1 1 5DA8422F
P 5100 2550
F 0 "U13" H 5100 2792 50  0000 C CNN
F 1 "L7818" H 5100 2701 50  0000 C CNN
F 2 "TO_SOT_Packages_THT:TO-220-3_Vertical" H 5125 2400 50  0001 L CIN
F 3 "http://www.st.com/content/ccc/resource/technical/document/datasheet/41/4f/b3/b0/12/d4/47/88/CD00000444.pdf/files/CD00000444.pdf/jcr:content/translations/en.CD00000444.pdf" H 5100 2500 50  0001 C CNN
	1    5100 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	5100 2850 5100 4800
Wire Wire Line
	5100 4800 6000 4800
Connection ~ 6000 4800
Wire Wire Line
	4150 4800 5100 4800
Connection ~ 5100 4800
Wire Wire Line
	5400 2550 6000 2550
Connection ~ 6000 2550
Text Notes 1800 5050 0    50   ~ 0
(capacitor multiplier: not \nimplemented, may remove)
Wire Wire Line
	1700 2550 2150 2550
Wire Wire Line
	2150 2550 2400 2550
Connection ~ 2150 2550
Wire Wire Line
	2150 2700 2150 2550
Wire Wire Line
	1700 4800 2150 4800
Connection ~ 2150 4800
Wire Wire Line
	2150 3950 2150 4800
Wire Wire Line
	2150 3350 2150 3650
Wire Wire Line
	2600 3050 2600 3350
Wire Wire Line
	2600 3350 2150 3350
Connection ~ 2150 3350
Wire Wire Line
	2150 3000 2150 3350
Wire Wire Line
	2150 4800 3000 4800
Wire Wire Line
	3000 4800 3950 4800
Connection ~ 3000 4800
Wire Wire Line
	3000 3850 3000 4800
Wire Wire Line
	3000 2550 3950 2550
Wire Wire Line
	3000 2550 2800 2550
Connection ~ 3000 2550
Wire Wire Line
	3000 3550 3000 2550
$Comp
L Diode:1N4001 D?
U 1 1 5D8E7421
P 3000 3700
AR Path="/5D8E7421" Ref="D?"  Part="1" 
AR Path="/5D8E6431/5D8E7421" Ref="D1"  Part="1" 
F 0 "D1" V 3046 3621 50  0000 R CNN
F 1 "1N4001" V 2955 3621 50  0000 R CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 3000 3525 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 3000 3700 50  0001 C CNN
	1    3000 3700
	0    -1   -1   0   
$EndComp
$Comp
L Device:C C?
U 1 1 5D8E7417
P 2150 3800
AR Path="/5D8E7417" Ref="C?"  Part="1" 
AR Path="/5D8E6431/5D8E7417" Ref="C4"  Part="1" 
F 0 "C4" H 2265 3846 50  0000 L CNN
F 1 "C" H 2265 3755 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.80mm" H 2188 3650 50  0001 C CNN
F 3 "~" H 2150 3800 50  0001 C CNN
	1    2150 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 5D8E7410
P 2150 2850
AR Path="/5D8E7410" Ref="R?"  Part="1" 
AR Path="/5D8E6431/5D8E7410" Ref="R1"  Part="1" 
F 0 "R1" H 2218 2896 50  0000 L CNN
F 1 "R_US" H 2218 2805 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 2190 2840 50  0001 C CNN
F 3 "~" H 2150 2850 50  0001 C CNN
	1    2150 2850
	1    0    0    -1  
$EndComp
$Comp
L Device:Ferrite_Bead_Small FB?
U 1 1 5D8E7409
P 2600 2950
AR Path="/5D8E7409" Ref="FB?"  Part="1" 
AR Path="/5D8E6431/5D8E7409" Ref="FB1"  Part="1" 
F 0 "FB1" H 2700 2950 50  0000 L CNN
F 1 "F" H 2700 2905 50  0001 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal" V 2530 2950 50  0001 C CNN
F 3 "~" H 2600 2950 50  0001 C CNN
	1    2600 2950
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_NPN_EBC Q?
U 1 1 5D8E7401
P 2600 2650
AR Path="/5D8E7401" Ref="Q?"  Part="1" 
AR Path="/5D8E6431/5D8E7401" Ref="Q1"  Part="1" 
F 0 "Q1" V 2928 2650 50  0000 C CNN
F 1 "Q_NPN_EBC" V 2837 2650 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 2800 2750 50  0001 C CNN
F 3 "~" H 2600 2650 50  0001 C CNN
	1    2600 2650
	0    -1   -1   0   
$EndComp
$EndSCHEMATC
