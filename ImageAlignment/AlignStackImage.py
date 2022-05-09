# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:42:00 2022

@author: Quan Qing
"""

from nd2reader import ND2Reader
from pystackreg import StackReg
from skimage.io import imsave

import tkinter as tk
from tkinter import filedialog
import os

def open_file_dlg():
    root = tk.Tk()
    root.withdraw()
    
    file_path = filedialog.askopenfilename()
    
    return file_path

if __name__ == '__main__':
    print('please select the image file first.')
    filename = open_file_dlg()
    chnlist = input('please list the channels '
                    'separated by camma for registration '
                    'with the first one as the reference '
                    'channel: ').split(',')
    chnlist=[int(x) for x in chnlist]
    (dirname, fname)=os.path.split(filename)
    
    if fname.split('.')[-1] == 'nd2' and len(chnlist):
        print('ok, we will work with file: '+filename)
        print('will now use color channel '+str(chnlist[0])+' to align all the other channels')
        print('will automatically use frame 0 as the reference frame')
            
        with ND2Reader(filename) as images:
            images.iter_axes = 't'
            images.bundle_axes = 'cyx'
            refchn = chnlist[0]
            refimg = images[0][refchn]
            
            # save frame 0 first for all channels
            for chnidx in chnlist:
                newpathname = os.path.join(dirname, 'aligned_'+fname.split('.')[0]+'_chn'+str(chnidx))
                if not os.path.exists(newpathname):
                    os.mkdir(newpathname)
                imgname = fname.split('.')[0]+'_chn'+str(chnidx)+'_0.tif'
                imsave(os.path.join(newpathname, imgname), images[0][chnidx])
                
            sr = StackReg(StackReg.RIGID_BODY)
            for t in range(1, len(images)):
                print('processing time frame '+str(t))
                imgset = images[t]
                
                transimg = imgset[refchn]
                sr.register(refimg, transimg)
                
                for chnidx in chnlist:
                    newpathname = os.path.join(dirname, 'aligned_'+fname.split('.')[0]+'_chn'+str(chnidx))
                    if not os.path.exists(newpathname):
                        os.mkdir(newpathname)
                    imgname = fname.split('.')[0]+'_chn'+str(chnidx)+'_'+str(t)+'.tif'
                    imsave(os.path.join(newpathname, imgname), sr.transform(imgset[chnidx]))
                    print(imgname+' registration done.')
                
            
        