from math import *
import numpy as np
import copy

N = 1000 # N为采集的数据包数量

def complexDecoding(raw_data):
    """    
    将原始数据转化为Python可识别的复数
    这里使用了第一个天线的数据raw_data[0]
    第二根第三根天线数据下标分别为1, 2
    原始数据为a + bi, python为a + bj
    返回处理后的数据
    """
    for n in range(N):
        for i in range(30): # 30 代表子载波数量，固定为30
            if raw_data[0][-1] == 'i':
                data.append(complex(raw_data[0][:-1]+'j'))
            else:
                data.append(complex(raw_data[0]))
    return data

def getAP(data):
    """
    根据复数计算振幅和相位
    """
    amplitudes = [([] * 30) for i in range(N)]
    phases = [([] * 30) for i in range(N)]
    for m in range(N):
        for i in range(30):
            r = sqrt((data[i + m * 30].real) ** 2 + (data[i + m * 30].imag) ** 2)
            amplitudes[m].append(r)
            phases[m].append(np.angle(data[i + m * 30]))
    return (amplitudes, phases)

def preprocessingPhase(phases):
    """
    将相位进行线性变换
    index是 -28 到 28 根据 IEEE 802.11n 协议
    返回变换后的相位
    """
    index = range(-28,0,2) + [-1, 1] + range(3,28, 2) + [28]
    for m in range(N):
        for l in range(10):
            clear = True
            base = 0
            tphases[m][0] = phases[m][0]

            for i in range(1, 30):
                if phases[m][i] - phases[m][i-1] > pi:
                    base += 1
                    clear = False
                elif phases[m][i] - phases[m][i-1] < -pi:
                    base -= 1
                    clear = False
                tphases[m][i] = phases[m][i] - 2 * pi * base

            if clear == True:
                break
            else:
                for i in range(30):
                    phases[m][i] = tphases[m][i] - (tphases[m][29] - tphases[m][0]) 
                                    * 1.0 /(28 - (-28)) * (index[i]) 
                                    - 1.0 / 30 * sum([tphases[m][j] for j in range(30)])
    return phases