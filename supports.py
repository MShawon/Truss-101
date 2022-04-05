"""
GPL-3.0 License

Copyright (C) 2020-2022 Monirul Shawon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import matplotlib
#import matplotlib.pyplot as plt
import numpy as np
"""
##############################################################
#                                                            #
#             Roller support marker using path               #
#            Pinned Support marker also using path           #
#              Our own custom arrow for rotating             #
#              Reaction arrow using path                     # 
#                                                            # 
#    ----------------- Monirul Shawon ------------------     #
##############################################################
"""
def rollerSupport():
    MAGIC = 0.2652031
    SQRTHALF = np.sqrt(0.5)
    MAGIC45 = SQRTHALF * MAGIC
    verts = np.array([[0.0, -1.0],
                    [MAGIC, -1.0], [SQRTHALF-MAGIC45, -SQRTHALF-MAGIC45], [SQRTHALF, -SQRTHALF],
                    [SQRTHALF+MAGIC45, -SQRTHALF+MAGIC45], [1.0, -MAGIC] ,[1.0, 0.0],
                    [1.0, MAGIC], [SQRTHALF+MAGIC45, SQRTHALF-MAGIC45], [SQRTHALF, SQRTHALF],
                    [SQRTHALF-MAGIC45, SQRTHALF+MAGIC45], [MAGIC, 1.0], [0.0, 1.0],
                    [-MAGIC, 1.0], [-SQRTHALF+MAGIC45, SQRTHALF+MAGIC45], [-SQRTHALF, SQRTHALF],
                    [-SQRTHALF-MAGIC45, SQRTHALF-MAGIC45], [-1.0, MAGIC], [-1.0, 0.0],
                    [-1.0, -MAGIC], [-SQRTHALF-MAGIC45, -SQRTHALF+MAGIC45], [-SQRTHALF, -SQRTHALF],
                    [-SQRTHALF+MAGIC45, -SQRTHALF-MAGIC45], [-MAGIC, -1.0], [0.0, -1.0],
                    [0.0, -1.0],
                    #line
                    [-1.0,-1.0], #index [26] 
                    [1.0,-1.0],
                    #Wall
                    [-1.0,-1.3], [-0.8,-1.0],[-0.8,-1.3],[-0.6,-1.0],
                    [-0.6,-1.3],[-0.4,-1.0],[-0.4,-1.3],[-0.2,-1.0],
                    [-0.2,-1.3],[0.0,-1.0],[0.0,-1.3],[0.2,-1.0],
                    [0.2,-1.3],[0.4,-1.0],[0.4,-1.3],[0.6,-1.0],
                    [0.6,-1.3],[0.8,-1.0],                   
                    ],dtype=float)

    codes = [matplotlib.path.Path.CURVE4] * 46
    codes[0] = matplotlib.path.Path.MOVETO
    codes[-21] = matplotlib.path.Path.CLOSEPOLY
    for i in range(26,46):
        if i%2==0:
            codes[i]=matplotlib.path.Path.MOVETO
        else:
            codes[i]=matplotlib.path.Path.LINETO

    path = matplotlib.path.Path(verts*1+(0,-1.5), codes)
    return path

def pinnedSupport():
    verts=np.array([[-1.0, -1.5], [0.0, 0.0], [1.0, -1.5], [-1.0, -1.5],
                    #Line Add + wall
                    [-1.2,-1.5],[1.2,-1.5],[-1.2,-1.8],[-1.0,-1.5],
                    #Wall
                    [-1.0,-1.8],[-0.8,-1.5],[-0.8,-1.8],[-0.6,-1.5],
                    [-0.6,-1.8],[-0.4,-1.5],[-0.4,-1.8],[-0.2,-1.5],
                    [-0.2,-1.8],[0.0,-1.5],[0.0,-1.8],[0.2,-1.5],
                    [0.2,-1.8],[0.4,-1.5],[0.4,-1.8],[0.6,-1.5],
                    [0.6,-1.8],[0.8,-1.5],[0.8,-1.8],[1,-1.5],
                    ],dtype=float)

    codes=[matplotlib.path.Path.LINETO]*28
    codes[0]=matplotlib.path.Path.MOVETO
    codes[3]=matplotlib.path.Path.CLOSEPOLY
    for i in range(4,28):
        if i%2==0:
            codes[i]=matplotlib.path.Path.MOVETO
        else:
            codes[i]=matplotlib.path.Path.LINETO

    path = matplotlib.path.Path(verts*1+(0,-0.5), codes)
    return path

def ownArrow():
    verts = np.array([[-0.2,0],[-0.45,0.1],[-0.35,0],[-1,0],
                    [-0.35,0],[-0.45,-0.1],[-0.2,0],[-0.2,0]],
            dtype=float)

    codes = [matplotlib.path.Path.LINETO] * 8
    codes[0] =matplotlib.path.Path.MOVETO
    codes[-1] = matplotlib.path.Path.CLOSEPOLY

    path = matplotlib.path.Path(verts, codes)
    return path

def reactionArrow():
    verts = np.array([[0,0],[0.8,0],[0.7,0.1],[1.0,0.0],
            [0.7,-0.1],[0.8,0],[0,0],[0,0]],
            dtype=float)


    codes = [matplotlib.path.Path.LINETO] * 8
    codes[0] = matplotlib.path.Path.MOVETO
    codes[-1] = matplotlib.path.Path.CLOSEPOLY

    path = matplotlib.path.Path(verts, codes)
    return path

# roller_support=reactionArrow()
# marker = roller_support.transformed(matplotlib.transforms.Affine2D().rotate_deg(0))

# t = np.arange(0.0,1.5,0.25)
# s = np.sin(2*np.pi*t)

# fig,ax = plt.subplots()
# ax.plot(t,s, marker=marker, color='k',markerfacecolor='#ff3300',markeredgecolor='#ff3300', markersize=50,alpha=0.8)
# ax.margins(.20)

# plt.show()