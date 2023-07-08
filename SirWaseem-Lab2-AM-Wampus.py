import numpy as np
from numpy import random as r

# def wampus(col,row,nwam,npit,sp):
#
#     grid=[[[0]]* col for _ in range(row)]
#     print(grid)
#     # grid[1][1].append(3)
#     # print(grid)
#     while npit>0:
#         x=r.randint(row)
#         y=r.randint(col)
#         print("(",x,",",y,")")
#         if grid[x][y]!=3:
#          grid[x][y]=3
#          continue
#         print(grid)
# wampus(4,4,1,1,1)


def Placement(placementConstant, SP, GW):
    x = np.random.randint(NRows)
    y = np.random.randint(NCols)
    if (x, y) == SP:
        return False, GW
    else:
        if GW[x][y] == 2 | GW[x][y] == 3 | GW[x][y] == 4:
            return False, GW
        else:
            GW[x][y] = placementConstant
            if x+1<NRows:
                GW[x+1][y]="E"

                return True, GW



def WampusWorld(NCols,NRows, NPits,NWampus, NGold, SP):
 GW=[[0]*NCols for _ in range(NRows)]

 while NPits>0:
     checkFlag, GW=Placement(2, SP, GW)
     if checkFlag:
      NPits = NPits - 1
     else:
        continue

 while NWampus>0:
     checkFlag, GW=Placement(3, SP, GW)
     if checkFlag:
      NWampus = NWampus - 1
     else:
        continue

 while NGold>0:
     checkFlag, GW=Placement(4, SP, GW)
     if checkFlag:
      NGold = NGold - 1
     else:
        continue
 print(GW)







NCols=4
NRows=4
NPits=2
SP=(0,0)
NWampus=1
NGold=1
WampusWorld(NCols,NRows, NPits,NWampus,NGold, SP)