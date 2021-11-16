# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:49:18 2021

@author: yuhao
"""
import bagpy
import shutil
import os
from pathlib import Path


optitrack_topic = '/mocap_node/Robot_1/pose'
force_topic = '/ni_daq_data'
source_dir = 'PATH TO SOURCE DIRECTORY'
aim_dir = 'PATH TO DESTINATION DIRECTORY'
i = 1

if os.path.isdir(source_dir):
    print('Source directory found')
else:
    print('Error: source directory not found.')
    exit()

if os.path.isdir(aim_dir):
    print('Aim directory found.')
else:
    print('Aim directory not found.')
    os.mkdir(aim_dir)
    print('Successfully created Aim directory')
    
for file in os.listdir(source_dir):
    if file.endswith(".bag"): 
        filename = Path(file).stem
        b = bagpy.bagreader('{}/{}'.format(source_dir,file))
        optitrack_data = b.message_by_topic(optitrack_topic)
        force_data = b.message_by_topic(force_topic)
        shutil.copy(optitrack_data, '{}/optitrack_{}.csv'.format(aim_dir,str(i).zfill(2)))
        shutil.copy(force_data, '{}/force_{}.csv'.format(aim_dir,str(i).zfill(2)))
        i+=1
    else:
        continue
        