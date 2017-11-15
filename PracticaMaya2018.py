from maya import cmds
cmds.file(new=True, f=True)

player, _ = cmds.polyCube(w=4, h=2, d=2)
cmds.setAttr(player + ".translate", 0, 0, 0)

# Create bounds
cmds.curve(d=1, p=[(0,-10,-50), (100,-10,-50), (100,-10,50), (0,-10,50), (0,-10,-50)]) # Bottom face
cmds.curve(d=1, p=[(0,10,-50), (100,10,-50), (100,10,50), (0,10,50), (0,10,-50)])    # Upper face
cmds.curve(d=1, p=[(0,-10,-50),(0,10,-50)])    # Back-left edge
cmds.curve(d=1, p=[(100,-10,-50),(100,10,-50)])    # Front-left edge
cmds.curve(d=1, p=[(100,-10,50),(100,10,50)])    # Front-right edge
cmds.curve(d=1, p=[((0,-10,50)),(0,10,50)])    # Back-right edge

# Create obstacle circuit
cube1, _ = cmds.polyCube(w=2, h=2, d=2)
cmds.setAttr(cube1 + ".translate", 5, 0, 0)