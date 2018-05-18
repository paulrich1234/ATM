# -*- coding: UTF-8 -*-
from __future__ import division
import requests,sys,os
import pandas as pd
import numpy as np
s = os.sep

root = "/home/lily/Desktop" + s + "face_embedding"+s
'''for rt, dirs, filess in os.walk(root):
    for f in filess:
        file_path = rt + s + f
        filename=file_path
        #print(filename)
        key1 = str(os.path.basename(rt))
        #print(key1)
        data=pd.read_table(filename,header=None,sep=',')
        data['laber']=key1
        data.to_csv('/home/lily/Desktop/data.csv', sep=',', mode='a', header=False)
        print(data)
'''
for rt, dirs, filess in os.walk(root):
    for f in filess:
        file_path = rt + s + f
        filename=file_path
        person=os.path.basename(os.path.dirname(filename))
        with open(filename) as filetxt:
            for line in filetxt:
                b=line.split(',')
                b=pd.DataFrame(b)
                b=b.transpose()
                b['class']=person
                b.to_csv('/home/lily/Desktop/train_datafile1.csv', sep=',', mode='a', header=False)

