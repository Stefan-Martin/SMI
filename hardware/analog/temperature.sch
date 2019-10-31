EESchema Schematic File Version 4
LIBS:analog-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 4050 4150 2    50   Input ~ 0
RTD+
Text HLabel 4050 4300 2    50   Input ~ 0
RTD-
Text HLabel 7350 3400 2    50   Input ~ 0
RTD_AMP
$Comp
L smi:INA125P U6
U 1 1 5D8F05C2
P 5950 2950
AR Path="/5D8EE9F6/5D8F05C2" Ref="U6"  Part="1" 
AR Path="/5D8EEFE9/5D8F05C2" Ref="U10"  Part="1" 
F 0 "U10" H 6200 3100 50  0000 C CNN
F 1 "INA125P" H 6200 3000 50  0000 C CNN
F 2 "" H 7650 1450 50  0001 C CNN
F 3 "" H 7650 1450 50  0001 C CNN
	1    5950 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 3600 4900 3600
Wire Wire Line
	4900 3600 4900 3400
Wire Wire Line
	4900 3400 5350 3400
NoConn ~ 5350 3500
NoConn ~ 5350 3200
NoConn ~ 5350 3300
$Comp
L Device:R_US R5
U 1 1 5D8F06D7
P 3600 3650
AR Path="/5D8EE9F6/5D8F06D7" Ref="R5"  Part="1" 
AR Path="/5D8EEFE9/5D8F06D7" Ref="R12"  Part="1" 
F 0 "R12" H 3668 3696 50  0000 L CNN
F 1 "330K" H 3668 3605 50  0000 L CNN
F 2 "" V 3640 3640 50  0001 C CNN
F 3 "~" H 3600 3650 50  0001 C CNN
	1    3600 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R6
U 1 1 5D8F0741
P 4050 3650
AR Path="/5D8EE9F6/5D8F0741" Ref="R6"  Part="1" 
AR Path="/5D8EEFE9/5D8F0741" Ref="R13"  Part="1" 
F 0 "R13" H 4118 3696 50  0000 L CNN
F 1 "1K1" H 4118 3605 50  0000 L CNN
F 2 "" V 4090 3640 50  0001 C CNN
F 3 "~" H 4050 3650 50  0001 C CNN
	1    4050 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R8
U 1 1 5D8F07C5
P 3600 4250
AR Path="/5D8EE9F6/5D8F07C5" Ref="R8"  Part="1" 
AR Path="/5D8EEFE9/5D8F07C5" Ref="R15"  Part="1" 
F 0 "R15" H 3668 4296 50  0000 L CNN
F 1 "3K3" H 3668 4205 50  0000 L CNN
F 2 "" V 3640 4240 50  0001 C CNN
F 3 "~" H 3600 4250 50  0001 C CNN
	1    3600 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4050 4300 4050 4600
Wire Wire Line
	4050 4600 3850 4600
Wire Wire Line
	3600 4600 3600 4400
Wire Wire Line
	3600 4100 3600 3900
Wire Wire Line
	4050 4150 4050 3800
Wire Wire Line
	3850 4600 3850 4750
Connection ~ 3850 4600
Wire Wire Line
	3850 4600 3600 4600
Wire Wire Line
	3600 3500 3600 3400
Wire Wire Line
	3600 3400 4050 3400
Connection ~ 4900 3400
Wire Wire Line
	4050 3500 4050 3400
Connection ~ 4050 3400
Wire Wire Line
	4050 3400 4900 3400
Wire Wire Line
	5350 3800 4050 3800
Connection ~ 4050 3800
Wire Wire Line
	5350 4100 5350 3900
Wire Wire Line
	5350 3900 3600 3900
Wire Wire Line
	3600 3900 3600 3800
Connection ~ 3600 3900
Wire Wire Line
	5950 2450 5950 2650
$Comp
L Device:C_Small C8
U 1 1 5D8F47C5
P 5600 2650
AR Path="/5D8EE9F6/5D8F47C5" Ref="C8"  Part="1" 
AR Path="/5D8EEFE9/5D8F47C5" Ref="C10"  Part="1" 
F 0 "C10" V 5371 2650 50  0000 C CNN
F 1 "0.1uF" V 5462 2650 50  0000 C CNN
F 2 "" H 5600 2650 50  0001 C CNN
F 3 "~" H 5600 2650 50  0001 C CNN
	1    5600 2650
	0    1    1    0   
$EndComp
Wire Wire Line
	5700 2650 5950 2650
Connection ~ 5950 2650
Wire Wire Line
	5950 2650 5950 2750
Wire Wire Line
	6700 4450 6700 4200
Wire Wire Line
	6700 4100 6550 4100
Wire Wire Line
	6550 4200 6700 4200
Connection ~ 6700 4200
Wire Wire Line
	6700 4200 6700 4100
$Comp
L Device:R_US R7
U 1 1 5D8F4EAF
P 7150 3950
AR Path="/5D8EE9F6/5D8F4EAF" Ref="R7"  Part="1" 
AR Path="/5D8EEFE9/5D8F4EAF" Ref="R14"  Part="1" 
F 0 "R14" H 7218 3996 50  0000 L CNN
F 1 "2K" H 7218 3905 50  0000 L CNN
F 2 "" V 7190 3940 50  0001 C CNN
F 3 "~" H 7150 3950 50  0001 C CNN
	1    7150 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	7150 3800 6550 3800
Wire Wire Line
	6550 3900 6950 3900
Wire Wire Line
	6950 3900 6950 4100
Wire Wire Line
	6950 4100 7150 4100
Wire Wire Line
	7350 3400 6750 3400
Wire Wire Line
	6550 3500 6750 3500
Wire Wire Line
	6750 3500 6750 3400
Connection ~ 6750 3400
Wire Wire Line
	6750 3400 6550 3400
Wire Wire Line
	6550 2800 6550 3200
Wire Wire Line
	5200 2750 5200 2650
Wire Wire Line
	5200 2650 5500 2650
Text Notes 5600 5350 0    50   ~ 0
TODO: fix grounding
$Comp
L power:GNDREF #PWR012
U 1 1 5D9238FF
P 6700 4450
AR Path="/5D8EE9F6/5D9238FF" Ref="#PWR012"  Part="1" 
AR Path="/5D8EEFE9/5D9238FF" Ref="#PWR019"  Part="1" 
F 0 "#PWR019" H 6700 4200 50  0001 C CNN
F 1 "GNDREF" H 6705 4277 50  0000 C CNN
F 2 "" H 6700 4450 50  0001 C CNN
F 3 "" H 6700 4450 50  0001 C CNN
	1    6700 4450
	1    0    0    -1  
$EndComp
$Comp
L power:+9V #PWR?
U 1 1 5DBB1E67
P 5950 2450
AR Path="/5D8EE9F6/5DBB1E67" Ref="#PWR?"  Part="1" 
AR Path="/5D8EEFE9/5DBB1E67" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5950 2300 50  0001 C CNN
F 1 "+9V" H 5965 2623 50  0000 C CNN
F 2 "" H 5950 2450 50  0001 C CNN
F 3 "" H 5950 2450 50  0001 C CNN
	1    5950 2450
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR?
U 1 1 5DBB1FAF
P 5200 2750
AR Path="/5D8EE9F6/5DBB1FAF" Ref="#PWR?"  Part="1" 
AR Path="/5D8EEFE9/5DBB1FAF" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5200 2500 50  0001 C CNN
F 1 "GNDREF" H 5205 2577 50  0000 C CNN
F 2 "" H 5200 2750 50  0001 C CNN
F 3 "" H 5200 2750 50  0001 C CNN
	1    5200 2750
	1    0    0    -1  
$EndComp
$Comp
L power:GNDREF #PWR?
U 1 1 5DBB38AB
P 3850 4750
F 0 "#PWR?" H 3850 4500 50  0001 C CNN
F 1 "GNDREF" H 3855 4577 50  0000 C CNN
F 2 "" H 3850 4750 50  0001 C CNN
F 3 "" H 3850 4750 50  0001 C CNN
	1    3850 4750
	1    0    0    -1  
$EndComp
$Comp
L power:-9V #PWR?
U 1 1 5DBB39B6
P 5950 5000
F 0 "#PWR?" H 5950 4875 50  0001 C CNN
F 1 "-9V" H 5965 5173 50  0000 C CNN
F 2 "" H 5950 5000 50  0001 C CNN
F 3 "" H 5950 5000 50  0001 C CNN
	1    5950 5000
	-1   0    0    1   
$EndComp
$Comp
L Device:C_Small C?
U 1 1 5DBB3F53
P 5600 4800
AR Path="/5D8EE9F6/5DBB3F53" Ref="C?"  Part="1" 
AR Path="/5D8EEFE9/5DBB3F53" Ref="C?"  Part="1" 
F 0 "C?" V 5371 4800 50  0000 C CNN
F 1 "0.1uF" V 5462 4800 50  0000 C CNN
F 2 "" H 5600 4800 50  0001 C CNN
F 3 "~" H 5600 4800 50  0001 C CNN
	1    5600 4800
	0    1    1    0   
$EndComp
Wire Wire Line
	5700 4800 5950 4800
Wire Wire Line
	5950 4650 5950 4800
Connection ~ 5950 4800
Wire Wire Line
	5950 4800 5950 5000
$Comp
L power:GNDREF #PWR?
U 1 1 5DBB4BBC
P 5350 4950
F 0 "#PWR?" H 5350 4700 50  0001 C CNN
F 1 "GNDREF" H 5355 4777 50  0000 C CNN
F 2 "" H 5350 4950 50  0001 C CNN
F 3 "" H 5350 4950 50  0001 C CNN
	1    5350 4950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 4950 5350 4800
Wire Wire Line
	5350 4800 5500 4800
$Comp
L power:+9V #PWR?
U 1 1 5DBB54BC
P 6550 2800
F 0 "#PWR?" H 6550 2650 50  0001 C CNN
F 1 "+9V" H 6565 2973 50  0000 C CNN
F 2 "" H 6550 2800 50  0001 C CNN
F 3 "" H 6550 2800 50  0001 C CNN
	1    6550 2800
	1    0    0    -1  
$EndComp
$EndSCHEMATC
