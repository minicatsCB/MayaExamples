from maya import cmds
cmds.file(new=True, f=True)

player, _ = cmds.polyPyramid(w=1)
cmds.setAttr(player + ".scale", 3, 3, 3)
cmds.setAttr(player + ".rotate", 0, 0, -90)
cmds.setAttr(player + ".translate", 0, 0, 0)
cmds.select(player)
cmds.setAttr(player + ".rotateOrder", 5)    # Set rotate order to ZYX
cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)    # Put the local axis back to its original position

# Create bounds
cmds.curve(d=1, p=[(0,-10,-50), (100,-10,-50), (100,-10,50), (0,-10,50), (0,-10,-50)]) # Bottom face
cmds.curve(d=1, p=[(0,10,-50), (100,10,-50), (100,10,50), (0,10,50), (0,10,-50)])    # Upper face
cmds.curve(d=1, p=[(0,-10,-50),(0,10,-50)])    # Back-left edge
cmds.curve(d=1, p=[(100,-10,-50),(100,10,-50)])    # Front-left edge
cmds.curve(d=1, p=[(100,-10,50),(100,10,50)])    # Front-right edge
cmds.curve(d=1, p=[((0,-10,50)),(0,10,50)])    # Back-right edge

# Create obstacle circuit
cube1, _ = cmds.polyCube(w=12, h=2, d=5)
cmds.setAttr(cube1 + ".translate", 16, 0, 0)

cube2, _ = cmds.polyCube(w=5, h=5, d=5)
cmds.setAttr(cube2 + ".translate", 27, 0, -11)

cube3, _ = cmds.polyCube(w=10, h=10, d=10)
cmds.setAttr(cube3 + ".rotate", 0, 27, 0)
cmds.setAttr(cube3 + ".translate", 20, 0, -25)

cube4, _ = cmds.polyCube(w=10, h=3, d=3)
cmds.setAttr(cube4 + ".translate", 38, 0, -5)

cube5, _ = cmds.polyCube(w=5, h=3, d=35)
cmds.setAttr(cube5 + ".translate", 51, 0, -19)

cube6, _ = cmds.polyCube(w=13, h=3, d=4)
cmds.setAttr(cube6 + ".translate",72, 0, -44)

cube7, _ = cmds.polyCube(w=3, h=3, d=20)
cmds.setAttr(cube7 + ".rotate", 0, -50, 0)
cmds.setAttr(cube7 + ".translate", 77, 0, 30)

cube8, _ = cmds.polyCube(w=7, h=7, d=15)
cmds.setAttr(cube8 + ".translate", 95, 0, 12)

cube9, _ = cmds.polyCube(w=3, h=3, d=3)
cmds.setAttr(cube9 + ".translate", 27, 0, -4)

cube10, _ = cmds.polyCube(w=6, h=6, d=6)
cmds.setAttr(cube10 + ".rotate", 0, -25, 0)
cmds.setAttr(cube10 + ".translate", 70, 0, -17)

cube11, _ = cmds.polyCube(w=4, h=4, d=4)
cmds.setAttr(cube11 + ".translate", 83, 0, 40)

cube12, _ = cmds.polyCube(w=9, h=1, d=4)
cmds.setAttr(cube12 + ".translate", 24, 0, 42)

cube13, _ = cmds.polyCube(w=12, h=12, d=12)
cmds.setAttr(cube13 + ".translate", 8, 0, 33)

cube14, _ = cmds.polyCube(w=12, h=12, d=12)
cmds.setAttr(cube14 + ".translate", 48, 0, 25)

cube15, _ = cmds.polyCube(w=12, h=12, d=12)
cmds.setAttr(cube15 + ".translate", 88, 0, -27)

cube16, _ = cmds.polyCube(w=12, h=12, d=12)
cmds.setAttr(cube16 + ".translate", 9, 0, -41)

sphere1, _ = cmds.polySphere(r=3)
cmds.setAttr(sphere1 + ".translate", 15, 0, -10)

sphere2, _ = cmds.polySphere(r=5)
cmds.setAttr(sphere2 + ".translate", 39, 0, 8)

sphere3, _ = cmds.polySphere(r=4)
cmds.setAttr(sphere3 + ".translate", 81, 0, -9)

sphere4, _ = cmds.polySphere(r=4)
cmds.setAttr(sphere4 + ".translate", 9, 0, 14)

cylinder1, _ = cmds.polyCylinder(r=1, h=2)
cmds.setAttr(cylinder1 + ".scale", 6, 3, 11)
cmds.setAttr(cylinder1 + ".rotate", 0, 24, 0)
cmds.setAttr(cylinder1 + ".translate", 23, 0, 21)

cylinder2, _ = cmds.polyCylinder(r=1, h=2)
cmds.setAttr(cylinder2 + ".scale", 6, 6, 6)
cmds.setAttr(cylinder2 + ".translate", 69, 0, -30)

torus1, _ = cmds.polyTorus(r=1, sr=0.5)
cmds.setAttr(torus1 + ".scale", 5, 5, 5)
cmds.setAttr(torus1 + ".translate", 77, 0, 11)

torus2, _ = cmds.polyTorus(r=1, sr=0.5)
cmds.setAttr(torus2 + ".scale", 5, 5, 5)
cmds.setAttr(torus2 + ".translate", 30, 0, -39)

torus3, _ = cmds.polyTorus(r=1, sr=0.5)
cmds.setAttr(torus3 + ".scale", 3, 3, 3)
cmds.setAttr(torus3 + ".translate", 60, 0, 38)

cone1, _ = cmds.polyCone(r=1, h=2)
cmds.setAttr(cone1 + ".scale", 6, 6, 6)
cmds.setAttr(cone1 + ".translate", 39, 0, -22)

cone2, _ = cmds.polyCone(r=1, h=2)
cmds.setAttr(cone2 + ".scale", 4, 4, 4)
cmds.setAttr(cone2 + ".translate", 39, 0, 40)

cone3, _ = cmds.polyCone(r=1, h=2)
cmds.setAttr(cone3 + ".scale", 5, 5, 5)
cmds.setAttr(cone3 + ".translate", 62, 0, 24)

pyramid1, _ = cmds.polyPyramid(w=1)
cmds.setAttr(pyramid1 + ".scale", 7, 7, 7)
cmds.setAttr(pyramid1 + ".translate", 51, 0, 10)

pipe1, _ = cmds.polyPipe(r=2, h=2, t=0.5)
cmds.setAttr(pipe1 + ".scale", 3, 16, 3)
cmds.setAttr(pipe1 + ".rotate", -90, -10, 0)
cmds.setAttr(pipe1 + ".translate", 64, 0, 1)

helix1, _ = cmds.polyHelix(c=3, h=2, w=2, r=0.4)
cmds.setAttr(helix1 + ".scale", 6, 6, 6)
cmds.setAttr(helix1 + ".translate", 93, 0, 36)
