import numpy as np
import time as time

starttime = time.time()

PI = np.pi

esizeksk = 0.15
esize2 = 0.30
esizedefault = 10


r1 = 1
r2 = r1 + 3 * esizeksk
r3 = r2 + 2 * esize2
r4 = esizedefault/2

# BLECHSTÄRKE [mm]
T1 = 40
# T1 = Bereich_T1[index]
T2 = 40
# T2 = Bereich_T2[index]
T3 = 12  # Mittelblech
# T3 = Bereich_T3[index]

# LÄNGE [mm]
L1 = 200
# L1 = Bereich_L1[index]
LEIN = 150
# LEIN = Bereich_LEIN[index]
L2 = 136
# L2 = Bereich_L2[index]
L3 = 150
# L3 = Bereich_L3[index]
L4 = T3
L5 = L3
L6 = L2
L7 = L1

# BREITE [mm]
W1 = 25
# W1 = Bereich_W1[index]
W2 = 100
# W2 = Bereich_W2[index]

# HOEHE [mm]
H = 200
# H = Bereich_´H[index]

# RADIUS [mm]
R = 400
# R = Bereich_R[index]

# SCHWEISSNAHTDICKE der Kehlnaht (senkrecht zur Naht definiert) [mm]
A = 14

M1x = r1*np.sin(PI/4) - r1*(1 - np.cos(PI/4))

Winkel1 = 0
Winkel2 = 0

E1 = 0
E2 = 0

THETA1 = Winkel1 * (PI/180)
THETA2 = Winkel2 * (PI/180)

kdictN_TM1 = {}
kdictN_TM2 = {}
kdictG = {}
kdictD = {}
kdictWeldLeft = {}
kdictWeldRight = {}
kdictWeld = {}

K1N = np.array([-L1-L2-L3, -W2/2-W1, T1/2, 1])
kdictN_TM1[1] = K1N
K2N = np.array([-L1-L2-L3, -W2/2-W1, -T1/2, 1])
kdictN_TM1[2] = K2N
K3N = np.array([-L2-L3, -W2/2-W1, T1/2, 1])
kdictN_TM1[3] = K3N
K4N = np.array([-L2-L3, -W2/2-W1, -T1/2, 1])
kdictN_TM1[4] = K4N
K5N = np.array([-L3, -W2/2, +T1/2, 1])
kdictN_TM1[5] = K5N
K6N = np.array([-L3, -W2/2, -T1/2, 1])
kdictN_TM1[6] = K6N

K15N = np.array([L5, -W2/2, T1/2, 1])
kdictN_TM2[15] = K15N
K16N = np.array([L5, -W2/2, -T1/2, 1])
kdictN_TM2[16] = K16N
K17N = np.array([L6+L5, -W2/2-W1, T1/2, 1])
kdictN_TM2[17] = K17N
K18N = np.array([L6+L5, -W2/2-W1, -T1/2, 1])
kdictN_TM2[18] = K18N
K19N = np.array([L7+L6+L5, -W2/2-W1, +T1/2, 1])
kdictN_TM2[19] = K19N
K20N = np.array([L7+L6+L5, -W2/2-W1, -T1/2, 1])
kdictN_TM2[20] = K20N
K21N = np.array([L7+L6+L5, +W2/2+W1, +T1/2, 1])
kdictN_TM2[21] = K21N
K22N = np.array([L7+L6+L5, +W2/2+W1, -T1/2, 1])
kdictN_TM2[22] = K22N
K23N = np.array([L6+L5, +W2/2+W1, +T1/2, 1])
kdictN_TM2[23] = K23N
K24N = np.array([L6+L5, +W2/2+W1, -T1/2, 1])
kdictN_TM2[24] = K24N
K25N = np.array([L5, +W2/2, +T1/2, 1])
kdictN_TM2[25] = K25N
K26N = np.array([L5, +W2/2, -T1/2, 1])
kdictN_TM2[26] = K26N

K35N = np.array([-L3, +W2/2, +T1/2, 1])
kdictN_TM1[35] = K35N
K36N = np.array([-L3, +W2/2, -T1/2, 1])
kdictN_TM1[36] = K36N
K37N = np.array([-L3-L2, +W2/2+W1, T1/2, 1])
kdictN_TM1[37] = K37N
K38N = np.array([-L3-L2, +W2/2+W1, -T1/2, 1])
kdictN_TM1[38] = K38N
K39N = np.array([-L1-L3-L2, +W2/2+W1, T1/2, 1])
kdictN_TM1[39] = K39N
K40N = np.array([-L1-L3-L2, +W2/2+W1, -T1/2, 1])
kdictN_TM1[40] = K40N

K81N = np.array([LEIN-L1-L2-L3, -W2/2-W1, T1/2, 1])
kdictN_TM1[81] = K81N
K82N = np.array([LEIN-L1-L2-L3, -W2/2-W1, -T1/2, 1])
kdictN_TM1[82] = K82N
K83N = np.array([-LEIN+L5+L6+L7, -W2/2-W1, +T2/2, 1])
kdictN_TM2[83] = K83N
K84N = np.array([-LEIN+L5+L6+L7, -W2/2-W1, -T2/2, 1])
kdictN_TM2[84] = K84N
K85N = np.array([-LEIN+L5+L6+L7, +W2/2+W1, +T2/2, 1])
kdictN_TM2[85] = K85N
K86N = np.array([-LEIN+L5+L6+L7, +W2/2+W1, -T2/2, 1])
kdictN_TM2[86] = K86N
K87N = np.array([LEIN-L1-L2-L3, +W2/2+W1, +T1/2, 1])
kdictN_TM1[87] = K87N
K88N = np.array([LEIN-L1-L2-L3, +W2/2+W1, -T1/2, 1])
kdictN_TM1[88] = K88N

ALPHA1 = np.arctan((K36N[1]-K38N[1]) / (K38N[0]-K36N[0]))
SL1 = np.sqrt((K36N[1]-K38N[1])**2 + (K38N[1]-K36N[1])**2)
LM1 = (1/2) * np.sqrt(4*R**2 - SL1**2)

ALPHA2 = np.arctan((K24N[1]-K26N[1]) / (K24N[0]-K26N[0]))
SL2 = np.sqrt((K24N[1]-K26N[1])**2 + (K24N[0]-K26N[0])**2)
LM2 = (1/2) * np.sqrt(4*R**2 - SL2**2)

# Kreissegmentmittelpunkt - Lokales Koordinatensystem
K41N = np.array([-L3-np.cos(ALPHA1)*(SL1/2)+np.sin(ALPHA1)*LM1, -W2/2-W1-np.sin(ALPHA1)*(SL1/2)-np.cos(ALPHA1)*LM1, +T1/2, 1])
kdictN_TM1[41] = K41N
K42N = np.array([-L3-np.cos(ALPHA1)*(SL1/2)+np.sin(ALPHA1)*LM1, -W2/2-W1-np.sin(ALPHA1)*(SL1/2)-np.cos(ALPHA1)*LM1, -T1/2, 1])
kdictN_TM1[42] = K42N
K43N = np.array([+L5+np.cos(ALPHA2)*(SL2/2)-np.sin(ALPHA2)*LM2, -W2/2-W1-np.sin(ALPHA2)*(SL2/2)-np.cos(ALPHA2)*LM2, +T1/2, 1])
kdictN_TM2[43] = K43N
K44N = np.array([+L5+np.cos(ALPHA2)*(SL2/2)-np.sin(ALPHA2)*LM2, -W2/2-W1-np.sin(ALPHA2)*(SL2/2)-np.cos(ALPHA2)*LM2, -T1/2, 1])
kdictN_TM2[44] = K44N
K45N = np.array([+L5+np.cos(ALPHA2)*(SL2/2)-np.sin(ALPHA2)*LM2, W2/2+W1+np.sin(ALPHA2)*(SL2/2)+np.cos(ALPHA2)*LM2, +T1/2, 1])
kdictN_TM2[45] = K45N
K46N = np.array([+L5+np.cos(ALPHA2)*(SL2/2)-np.sin(ALPHA2)*LM2, +W2/2+W1+np.sin(ALPHA2)*(SL2/2)+np.cos(ALPHA2)*LM2, -T1/2, 1])
kdictN_TM2[46] = K46N
K47N = np.array([-L3-np.cos(ALPHA1)*(SL1/2)+np.sin(ALPHA1)*LM1, W2/2+W1+np.sin(ALPHA1)*(SL1/2)+np.cos(ALPHA1)*LM1, +T1/2, 1])
kdictN_TM1[47] = K47N
K48N = np.array([-L3-np.cos(ALPHA1)*(SL1/2)+np.sin(ALPHA1)*LM1, W2/2+W1+np.sin(ALPHA1)*(SL1/2)+np.cos(ALPHA1)*LM1, -T1/2, 1])
kdictN_TM1[48] = K48N

K50N = np.array([-A/np.cos((PI)/4), -W2/2, +T1/2, 1])
kdictN_TM1[50] = K50N
K51N = np.array([-A/np.cos((PI)/4), -W2/2, -T1/2, 1])
kdictN_TM1[51] = K51N
K62N = np.array([-A/np.cos((PI)/4), +W2/2, +T1/2, 1])
kdictN_TM1[62] = K62N
K63N = np.array([-A/np.cos((PI)/4), +W2/2, -T1/2, 1])
kdictN_TM1[63] = K63N
K54N = np.array([+A/np.cos((PI)/4), -W2/2, +T2/2, 1])
kdictN_TM2[54] = K54N
K55N = np.array([+A/np.cos((PI)/4), -W2/2, -T2/2, 1])
kdictN_TM2[55] = K55N
K58N = np.array([+A/np.cos((PI)/4), +W2/2, +T2/2, 1])
kdictN_TM2[58] = K58N
K59N = np.array([+A/np.cos((PI)/4), +W2/2, -T2/2, 1])
kdictN_TM2[59] = K59N

K65N = np.array([-1.0*T1-A/np.cos((PI)/4), -W2/2, +T1/2, 1])
kdictN_TM1[65] = K65N
K66N = np.array([-1.0*T1-A/np.cos((PI)/4), -W2/2, -T1/2, 1])
kdictN_TM1[66] = K66N
K67N = np.array([-0.4*T1-A/np.cos((PI)/4), -W2/2, +T1/2, 1])
kdictN_TM1[67] = K67N
K68N = np.array([-0.4*T1-A/np.cos((PI)/4), -W2/2, -T1/2, 1])
kdictN_TM1[68] = K68N
K69N = np.array([+0.4*T2+A/np.cos((PI)/4), -W2/2, +T2/2, 1])
kdictN_TM2[69] = K69N
K70N = np.array([+0.4*T2+A/np.cos((PI)/4), -W2/2, -T2/2, 1])
kdictN_TM2[70] = K70N
K71N = np.array([+1.0*T2+A/np.cos((PI)/4), -W2/2, +T2/2, 1])
kdictN_TM2[71] = K71N
K72N = np.array([+1.0*T2+A/np.cos((PI)/4), -W2/2, -T2/2, 1])
kdictN_TM2[72] = K72N
K73N = np.array([+1.0*T2+A/np.cos((PI)/4), +W2/2, +T2/2, 1])
kdictN_TM2[73] = K73N
K74N = np.array([+1.0*T2+A/np.cos((PI)/4), +W2/2, -T2/2, 1])
kdictN_TM2[74] = K74N
K75N = np.array([+0.4*T2+A/np.cos((PI)/4), +W2/2, +T2/2, 1])
kdictN_TM2[75] = K75N
K76N = np.array([+0.4*T2+A/np.cos((PI)/4), +W2/2, -T2/2, 1])
kdictN_TM2[76] = K76N
K77N = np.array([-0.4*T1-A/np.cos((PI)/4), +W2/2, +T1/2, 1])
kdictN_TM1[77] = K77N
K78N = np.array([-0.4*T1-A/np.cos((PI)/4), +W2/2, -T1/2, 1])
kdictN_TM1[78] = K78N
K79N = np.array([-1.0*T1-A/np.cos((PI)/4), +W2/2, +T1/2, 1])
kdictN_TM1[79] = K79N
K80N = np.array([-1.0*T1-A/np.cos((PI)/4), +W2/2, -T1/2, 1])
kdictN_TM1[80] = K80N

K100N = np.array([-LEIN/2+L5+L6+L7, 0, 0, 1])
kdictN_TM2[100] = K100N

# Keypoints fuer Kerbspannung - Mittelpunkte Ausrundung
# Schweissnaht 1 - links unten
K91N = np.array([-(A/np.cos(PI/4) + M1x), +W2/2, +(T1/2 + r1), 1])
kdictN_TM1[91] = K91N

# Schweissnaht 2 - links oben
K92N = np.array([-(A/np.cos(PI/4) + M1x), +W2/2, -(T1/2 + r1), 1])
kdictN_TM1[92] = K92N

# Schweissnaht 3 - rechts unten
K93N = np.array([+(A/np.cos(PI/4) + M1x), +W2/2, +(T1/2 + r1), 1])
kdictN_TM2[93] = K93N

# Schweissnaht 4 - rechts oben
K94N = np.array([+(A/np.cos(PI/4) + M1x), +W2/2, -(T1/2 + r1), 1])
kdictN_TM2[94] = K94N

# Mittelpunkte fuer 1mm Radius am Querblech
# links unten
K95N = np.array([-r1, +W2/2, +(T1/2 + A/np.cos(PI/4) + M1x), 1])
kdictN_TM1[95] = K95N

# links oben
K96N = np.array([-r1, +W2/2, -(T1/2 + A/np.cos(PI/4) + M1x), 1])
kdictN_TM1[96] = K96N

# rechts unten
K97N = np.array([r1, +W2/2, +(T2/2 + A/np.cos(PI/4) + M1x), 1])
kdictN_TM2[97] = K97N

# rechts oben
K98N = np.array([r1, +W2/2, -(T2/2 + A/np.cos(PI/4) + M1x), 1])
kdictN_TM2[98] = K98N

#######################################################################
# Transformationsmatrix für Imperfektionen von Blech1 und Blech2
#######################################################################

# Transformationsmatrix TM1 - Transformation linke Seite
TM1 = np.array([[np.cos(THETA1), 0, np.sin(THETA1), -T3/2],
                [0, 1, 0, 0],
                [-np.sin(THETA1), 0, np.cos(THETA1), E1],
                [0, 0, 0, 1]
                ])

# Transformationsmatrix TM1 - Transformation rechte Seite
TM2 = np.array([[np.cos(THETA2), 0, np.sin(THETA2), T3/2],
                [0, 1, 0, 0],
                [-np.sin(THETA2), 0, np.cos(THETA2), E2],
                [0, 0, 0, 1]
                ])

# Translationsmatrix U - Gesamttranslation
TM3 = np.array([[1, 0, 0, T3/2],
                [0, 1, 0, 0],
                [0, 0, 1, -E1],
                [0, 0, 0, 1]
                ])

# Rotationsmatrix R - Gesamtrotation
RM = np.array([[np.cos(-THETA1), 0, np.sin(-THETA1), -(T3/2)/np.cos(-THETA1)],
               [0, 1, 0, 0],
               [-np.sin(-THETA1), 0, np.cos(-THETA1), 0],
               [0, 0, 0, 1]
               ])

TM1 = np.transpose(TM1)
TM2 = np.transpose(TM2)
TM3 = np.transpose(TM3)
RM = np.transpose(RM)

#######################################################################
# Translations- und Rotationsmatrixen für Ausrichtung
# von der Mittelebene von Blech1 in Z=0
#######################################################################

# Berechnung der Punkte im globalen Koordinatensystem

for key, value in kdictN_TM1.items():
    transformation = kdictN_TM1[key].dot(TM1)
    kdictG[key] = transformation

for key, value in kdictN_TM2.items():
    transformation = kdictN_TM2[key].dot(TM2)
    kdictG[key] = transformation

# Globale Stoßpunkte - linke Seite
K8G = np.array([-T3/2, -W2/2, (T1/2)/np.cos(-THETA1)+E1, 1])
kdictG[8] = K8G
K9G = np.array([-T3/2, -W2/2, -(T1/2)/np.cos(-THETA1)+E1, 1])
kdictG[9] = K9G
K32G = np.array([-T3/2, W2/2, (T1/2)/np.cos(-THETA1)+E1, 1])
kdictG[32] = K32G
K33G = np.array([-T3/2, W2/2, -(T1/2)/np.cos(-THETA1)+E1, 1])
kdictG[33] = K33G

# Globale Stoßpunkte - rechte Seite
K12G = np.array([+T3/2, -W2/2, (T2/2)/np.cos(THETA2)+E2, 1])
kdictG[12] = K12G
K13G = np.array([+T3/2, -W2/2, -(T2/2)/np.cos(THETA2)+E2, 1])
kdictG[13] = K13G
K28G = np.array([+T3/2, W2/2, (T2/2)/np.cos(THETA2)+E2, 1])
kdictG[28] = K28G
K29G = np.array([+T3/2, W2/2, -(T2/2)/np.cos(THETA2)+E2, 1])
kdictG[29] = K29G

# Globale Punkte - Mittelsteg
K7G = np.array([-L4/2, -W2/2,  H/2, 1])
kdictG[7] = K7G
K10G = np.array([-L4/2, -W2/2, -H/2, 1])
kdictG[10] = K10G
K11G = np.array([L4/2, -W2/2,  H/2, 1])
kdictG[11] = K11G
K14G = np.array([L4/2, -W2/2, -H/2, 1])
kdictG[14] = K14G
K27G = np.array([L4/2, W2/2,  H/2, 1])
kdictG[27] = K27G
K30G = np.array([L4/2, W2/2, -H/2, 1])
kdictG[30] = K30G
K31G = np.array([-L4/2, W2/2,  H/2, 1])
kdictG[31] = K31G
K34G = np.array([-L4/2, W2/2, -H/2, 1])
kdictG[34] = K34G

# Schweißpunkte globales Koordinatensystem
K52G = np.array([-L4/2, -W2/2, E1-((T1/2)/np.cos(-THETA1))-(np.sin(PI/4)*(A/np.cos(PI/4)+T1/2*np.tan(THETA1)))/np.sin(PI/4-THETA1), 1])
kdictG[52] = K52G
K49G = np.array([-L4/2, -W2/2, E1+((T1/2)/np.cos(-THETA1))+(np.sin(PI/4)*(A/np.cos(PI/4)+T1/2*np.tan(-THETA1)))/np.sin(PI/4+THETA1), 1])
kdictG[49] = K49G
K64G = np.array([-L4/2, +W2/2, E1-((T1/2)/np.cos(-THETA1))-(np.sin(PI/4)*(A/np.cos(PI/4)+T1/2*np.tan(THETA1)))/np.sin(PI/4-THETA1), 1])
kdictG[64] = K64G
K61G = np.array([-L4/2, +W2/2, E1+((T1/2)/np.cos(-THETA1))+(np.sin(PI/4)*(A/np.cos(PI/4)+T1/2*np.tan(-THETA1)))/np.sin(PI/4+THETA1), 1])
kdictG[61] = K61G
K56G = np.array([+L4/2, -W2/2, E2-(T2/2)/np.cos(THETA2)-(np.sin(PI/4)*(A/np.cos(PI/4)+T2/2*np.tan(-THETA2)))/np.sin(PI/4+THETA2), 1])
kdictG[56] = K56G
K53G = np.array([+L4/2, -W2/2, E2+(T2/2)/np.cos(THETA2)+(np.sin(PI/4)*(A/np.cos(PI/4)+T2/2*np.tan(+THETA2)))/np.sin(PI/4-THETA2), 1])
kdictG[53] = K53G
K60G = np.array([+L4/2, +W2/2, E2-(T2/2)/np.cos(THETA2)-(np.sin(PI/4)*(A/np.cos(PI/4)+T2/2*np.tan(-THETA2)))/np.sin(PI/4+THETA2), 1])
kdictG[60] = K60G
K57G = np.array([+L4/2, +W2/2, E2+(T2/2)/np.cos(THETA2)+(np.sin(PI/4)*(A/np.cos(PI/4)+T2/2*np.tan(THETA2)))/np.sin(PI/4-THETA2), 1])
kdictG[57] = K57G

#######################################################################
# Translation aller Koordinaten
#######################################################################
for key, value in kdictG.items():
    transformation = kdictG[key].dot(TM3)
    kdictD[key] = transformation

#######################################################################
# Rotation aller Koordinaten
#######################################################################

for key, value in kdictD.items():
    transformation = kdictD[key].dot(RM)
    kdictD[key] = transformation

# print(f"Time passed: {time.time() - starttime}")
