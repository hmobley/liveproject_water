# coding: utf-8
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/data/')
fs = ['aral_sea_s2cloudless-2016.jpg','aral_sea_s2cloudless-2018.jpg']
fs[0]
fs[1]
f = fs[0]
f
rawfile = f's2cloudless_imagery/data/{f}'
rawfile
maskfile = rawfile.replace('s2cloudless_imagery','s2cloudless_label_imagery')+'_mask.jpg'
maskfile
mask = Image.open(maskfile)
import Image
from PIL import Image
mask = Image.open(maskfile)
mask
mask = np.max(np.array(mask.resize(sz)),axis=2)
import numpy as np
mask = np.max(np.array(mask.resize(sz)),axis=2)
sz = (512, 512)
mask = np.max(np.array(mask.resize(sz)),axis=2)
mask = (mask>100).astype('int')
sum(mask)
mask
head(mask)
np.shape(mask)
mask[1,1,]
mask[100,100]
mask[200,200]
mask
tmp = np.array([[10,20],[1,2]])
tmp
sum(tmp)
sum(sum(tmp))
sum(sum(mask))
sum(mask)
len(sum(mask))
mask[29,]
mask[,29]
mask[:,29]
sum(mask[:,29])
sum(mask[:,28])
mask[:,28]
sum(sum(mask))
f = fs[1]
rawfile = f's2cloudless_imagery/data/{f}'
maskfile = rawfile.replace('s2cloudless_imagery','s2cloudless_label_imagery')+'_mask.jpg'
mask2 = Image.open(maskfile)
mask = np.max(np.array(mask.resize(sz)),axis=2)
mask2 = np.max(np.array(mask2.resize(sz)),axis=2)
mask2 = (mask2>100).astype('int')
sum(sum(mask))
sum(sum(mask2))
def loadmask(f):
    rawfile = rawfile = f's2cloudless_imagery/data/{f}'
    maskfile = maskfile = rawfile.replace('s2cloudless_imagery','s2cloudless_label_imagery')+'_mask.jpg'
    mask = Image.open(maskfile)
    mask = np.max(np.array(mask.resize(sz)),axis=2)
    mask = (mask>100).astype('int')
    return {mask,sum(sum(mask))}
    
fs
md = loadmask(fs[0])
fs[0]
sum(sum(mask))
def loadmask(f):
    rawfile = rawfile = f's2cloudless_imagery/data/{f}'
    maskfile = maskfile = rawfile.replace('s2cloudless_imagery','s2cloudless_label_imagery')+'_mask.jpg'
    mask = Image.open(maskfile)
    mask = np.max(np.array(mask.resize(sz)),axis=2)
    mask = (mask>100).astype('int')
    return (mask,sum(sum(mask)))
    
md = loadmask(fs[0])
md[0]
md[1]
sum(sum(mask))
sum(sum(mask2))
md2 = loadmask(fs[1])
md2
get_ipython().run_line_magic('ls', 's2cloudless_label_imagery')
get_ipython().run_line_magic('ls', 's2cloudless_label_imagery/data')
md2_1 = loadmask('balaton_s2cloudless-2016.jpg')
md2_2 = loadmask('balaton_s2cloudless-2018.jpg')
md3_1 = loadmask('burdur_s2cloudless-2016.jpg')
md3_2 = loadmask('burdur_s2cloudless-2018.jpg')
md4_1 = loadmask('copais_s2cloudless-2016.jpg')
md4_2 = loadmask('copais_s2cloudless-2018.jpg')
md2_1[1]
md2_2[1]
md3_1[1]
md3_2[1]
md4_1[1]
md4_2[1]
def calc_change(f1,f2):
    md1 = loadmask(f1)
    md2 = loadmask(f2)
    chg = md2[1] - md1[1]
    rt = chg/md1[1]
    return (chg,rt,md1,md2)
    
get_ipython().run_line_magic('ls', 's2cloudless_imagery')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/data')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/data/*2016')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/data/.*2016')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/data/*.2016')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/data/*2016')
get_ipython().run_line_magic('ls', 's2cloudless_imagery/data')
basenames = ['aral_sea','balaton','burdur','copais','elephant_butte','faguibine',
             'faguibine','koroneia','mead_mojave','mendocino','mono','poopo','qinghai',
             'ramganga','salda','salton_sea','urmia','walker']
len(basenames)
basenames = ['aral_sea','balaton','burdur','copais','elephant_butte','faguibine',
             'koroneia','mead_mojave','mendocino','mono','poopo','qinghai',
             'ramganga','salda','salton_sea','urmia','walker']
len(basenames)
for( bn in basenames):
    bn16 = "{bn}-2016.jpg"
for( bn in basenames)
    bn16 = "{bn}-2016.jpg"
for bn in basenames
    bn16 = "{bn}-2016.jpg"
basenames
for bn in basenames:
    bn16 = "{bn}-2016.jpg"
    bn18 = "{bn}-2018.jpb"
    print(bn16)
    print(bn18)
    
for bn in basenames:
    bn16 = f"{bn}-2016.jpg"
    bn18 = f"{bn}-2018.jpb"
    print(bn16)
    print(bn18)
    
def get_difs(basenames):
    for bn in basenames:
        bn16 = f"{bn}-2016.jpg"
        bn18 = f"{bn}-2018.jpb"
        chg = calc_change(bn16,bn18)
        print(f"{bn} change: {chg[1]*100.0}% ({chg[0]} pixels)")
        
len(basenames)
def get_diffs(basenames):
    for bn in basenames:
        bn16 = f"{bn}-2016.jpg"
        bn18 = f"{bn}-2018.jpb"
        chg = calc_change(bn16,bn18)
        print(f"{bn} change: {chg[1]*100.0}% ({chg[0]} pixels)")
        
get_diffs(basenames)
def get_diffs(basenames):
    for bn in basenames:
        bn16 = f"{bn}_s2cloudless-2016.jpg"
        bn18 = f"{bn}_s2cloudless-2018.jpb"
        chg = calc_change(bn16,bn18)
        print(f"{bn} change: {chg[1]*100.0}% ({chg[0]} pixels)")
        
get_diffs(basenames)
def get_diffs(basenames):
    for bn in basenames:
        bn16 = f"{bn}_s2cloudless-2016.jpg"
        bn18 = f"{bn}_s2cloudless-2018.jpg"
        chg = calc_change(bn16,bn18)
        print(f"{bn} change: {chg[1]*100.0}% ({chg[0]} pixels)")
        
get_diffs(basenames)
x = 0.385736368
print(f'{x}')
print(f'{x}.%0.2f')
print('{%0.2f}'.format(x))
print('{0.2f}'.format(x))
print('{.2f}'.format(x))
x.format('0.2f')
x.format(':0.2f'.format(x))
print('{:.2f}%'.format(x))
x
f'{x:.2f}'
def get_diffs(basenames):
    for bn in basenames:
        bn16 = f"{bn}_s2cloudless-2016.jpg"
        bn18 = f"{bn}_s2cloudless-2018.jpg"
        chg = calc_change(bn16,bn18)
        print(f"{bn} change: {chg[1]*100.0:.3f}% ({chg[0]} pixels)")
        
get_diffs(basenames)
def get_diffs(basenames):
    for bn in basenames:
        bn16 = f"{bn}_s2cloudless-2016.jpg"
        bn18 = f"{bn}_s2cloudless-2018.jpg"
        chg = calc_change(bn16,bn18)
        print(f"{bn} change: {chg[1]*100.0:.2f}% ({chg[0]} pixels)")
        
