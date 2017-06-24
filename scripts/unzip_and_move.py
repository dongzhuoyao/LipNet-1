
import os
import subprocess

target_dir = '/bdata/hut/lab/riz_LipNet/data/unzipped'

video_str = '/bdata/hut/lab/riz_LipNet/data/s{*}.mpg_vcd.zip'
align_str = '/bdata/hut/lab/riz_LipNet/data/s{*}.tar'


for k in range(1,35):
    if k == 21:
        continue

    video = video_str.replace("{*}", str(k))
    align = align_str.replace("{*}", str(k))

    cmd = ['unzip', video, '-d', target_dir]
    print('unzip ', video)
    subprocess.call(cmd)

    #mkdir -p 111 && tar -zxvf s1.tar -C 111
    #tar_target = os.path.join(target_dir, 's%d_align'.format(k))
    tar_target = target_dir
    cmd = ['tar','-zxvf',align,'-C',tar_target ]
    print('tar  ', align)
    subprocess.call(cmd)