import os
import subprocess

data_url = ''
target_dir = '/bdata/hut/lab/riz_LipNet/data'

video_str = 'http://spandh.dcs.shef.ac.uk/gridcorpus/s{*}/video/s{*}.mpg_vcd.zip'
align_str = 'http://spandh.dcs.shef.ac.uk/gridcorpus/s{*}/align/s{*}.tar'


for k in range(1,35):
    if k == 21:
        continue

    video = video_str.replace("{*}",str(k))
    align = align_str.replace("{*}",str(k))

    cmd = ['wget', video,'-P',target_dir]
    print('Downloading ', video)
    subprocess.call(cmd)

    cmd = ['wget', align,'-P',target_dir]
    print('Downloading ', align)
    subprocess.call(cmd)