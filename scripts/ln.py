import subprocess
for k in range(1,35):
    if k == 21:
        continue

    cmd = ['ln', '-s', '/bdata/hut/lab/riz_LipNet/data/unzipped/s%'.format(k), '/bdata/hut/lab/riz_LipNet/training/unseen_speakers/datasets/train/s%'.format(k)]
    print('ln ', cmd)
    subprocess.call(cmd)