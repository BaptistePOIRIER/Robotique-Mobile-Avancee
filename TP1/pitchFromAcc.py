# -*- coding: utf-8 -*-
"""
Pitch estimation from accelerometers' measurements

(c) S. Bertrand
"""


import math
import numpy as np
import matplotlib.pyplot as plt
import ImuData as imud



if __name__=='__main__':

    # sampling period (s)
    # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
    Te = 0.01
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # read data file
    fileName = 'donneesIMUAuRepos.txt'
    #fileName = 'donneesIMUPetitsAngles.txt'
    delimiter = '\t'
    imuMes = imud.ImuData(fileName, delimiter, Te)


    # init data structures for simulation
    computedPitchFromAcc = []
    pitchImu = []
    indicesK = [0]
    w0 = []


    # main loop to parse data from IMU
    for i in range(0, len(imuMes.time)):

        # compute pitch from acc measurements
        
        # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
        pitchAcc = np.arctan2(-imuMes.accX[i],np.sqrt(imuMes.accY[i]**2+imuMes.accZ[i]**2))
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
               
        # save to data structures used for simulation
        computedPitchFromAcc.append(pitchAcc)    
        indicesK.append(i+1)    
        pitchImu.append( math.radians(  imuMes.pitchDeg[i] ) )
        w0.append(math.radians(  pitchAcc - imuMes.pitchDeg[i]  ))
    
    
    # Variance
    print("Variance du bruit de mesure :",np.std(w0))
    
    # plots
    plt.figure(1)
    plt.plot(indicesK[1:len(indicesK)], computedPitchFromAcc, color='g')
    plt.plot(indicesK[1:len(indicesK)], pitchImu, color='b')
    plt.ylabel('Estimated pitch (rad)')  
    plt.xlabel('Iteration')
    plt.title('Green: computed from Acceleros, Blue: from IMU filter')
    plt.grid(True)
