import sys
with open(sys.argv[1],"r") as f:cmd=f.read().splitlines()


import nxbt
nx=nxbt.Nxbt()
procon=nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(procon)

nx.macro(procon,"A 0.1s 0.1s")

for i in range(len(cmd)//10000+1):nx.macro(procon,'\n'.join(cmd[i*10000:(i+1)*10000]))
