import cv2
import sys
import numpy as np

img=~cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)>>7
assert img.shape==(120,320)

result=""
cur=0
for i in range(img.shape[0]):
	if not np.all(img[i]==0):
		sparse=np.where(img[i])[0]
		start,stop=sparse[0],sparse[-1]
		step=-1 if cur>(start+stop)//2 else 1
		if step==-1:
			stop,start=start,stop
			btn='DPAD_LEFT'
		else:
			btn='DPAD_RIGHT'
		if cur>start:
			result+='DPAD_LEFT 0.1s\n0.1s\n'*(cur-start)
		else:
			result+='DPAD_RIGHT 0.1s\n0.1s\n'*(start-cur)
		for j in range(start,stop+step,step):
			if img[i,j]:
				result+='A 0.1s\n'
			result+=f'{btn} 0.1s\n0.1s\n'
		result+='A 0.1s\nDPAD_DOWN 0.1s\n0.1s\n'
		cur=max(min(stop+step,320),0)
	else:
		result+='DPAD_DOWN 0.1s\n0.1s\n'

# with open(f'{sys.argv[1][:sys.argv[1].rfind(".")]}.txt','w') as f:
#     f.write(result)

print(result)
