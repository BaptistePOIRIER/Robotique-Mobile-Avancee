# -*- coding: utf-8 -*-
"""
Class for IMU data manipulation

@author: baptiste.poirier
"""
import numpy as np
import matplotlib.pyplot as plt
from ImuData import ImuData

imuMes = ImuData('donneesIMUAuRepos.txt', '\t', 0.01)
#imuMes = ImuData('donneesIMUPetitsAngles.txt', '\t', 0.01)    

plt.close('all')    

imuMes.plotAcc()
imuMes.plotGyr()
imuMes.plotMag()
imuMes.plotEulerAngles()

def printMeanStdVar(attribute,name): 
    message = "| {:<8} | ".format(name)
    message += "{:<22} | ".format(np.mean(attribute))
    message += "{:<22} | ".format(np.std(attribute))
    message += "{:<22} |".format(np.std(attribute)**2)
    print(message)

print("{0:=^87}".format(""))
print("| {:<8} | {:<22} | {:<22} | {:<22} |".format("","Moyennes","Écarts types","Variances"))
print("{0:=^87}".format(""))

printMeanStdVar(imuMes.accX,"AccX")
printMeanStdVar(imuMes.accY,"AccY")
printMeanStdVar(imuMes.accZ,"AccZ")
printMeanStdVar(imuMes.gyrX,"GyrX")
printMeanStdVar(imuMes.gyrY,"GyrY")
printMeanStdVar(imuMes.gyrZ,"GyrZ")
printMeanStdVar(imuMes.magX,"MagX")
printMeanStdVar(imuMes.magY,"MagY")
printMeanStdVar(imuMes.magZ,"MagZ")
printMeanStdVar(imuMes.rollDeg,"RollDeg")
printMeanStdVar(imuMes.pitchDeg,"PitchDeg")
printMeanStdVar(imuMes.yawDeg,"YawDeg")
print("{0:=^87}".format(""))
plt.show()

'''
=======================================================================================
|          | Moyennes               | Écarts types           | Variances              |
=======================================================================================
| AccX     | 0.02720513346135382    | 0.008259275238694125   | 6.82156274685059e-05   |
| AccY     | -0.04046780220835334   | 0.008874554810482507   | 7.87577230842582e-05   |
| AccZ     | 9.803582018242919      | 0.010705230955272116   | 0.00011460196980571635 |
| GyrX     | 0.007823619299087854   | 0.007046515724562534   | 4.965338385650705e-05  |
| GyrY     | 0.005936829092654825   | 0.006583946301875518   | 4.3348348905980305e-05 |
| GyrZ     | -0.015032977436389823  | 0.007527571191760228   | 5.6664328047018496e-05 |
| MagX     | 0.2995023970235237     | 0.0007754784058107633  | 6.013667578788028e-07  |
| MagY     | 0.16180865434469513    | 0.0008042637163030449  | 6.468401253615848e-07  |
| MagZ     | -0.6333457085933749    | 0.0008468436956693662  | 7.171442448949501e-07  |
| RollDeg  | -0.24911970427268362   | 0.03622090958766189    | 0.001311954291357577   |
| PitchDeg | -0.149982578012482     | 0.0296206121704777     | 0.0008773806653538515  |
| YawDeg   | 0.03455128804608737    | 0.034416094810919035   | 0.001184467582034168   |
=======================================================================================
'''