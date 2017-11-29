# Animate the player movement
cmds.currentUnit(time="59.94fps")
cmds.playbackOptions(min = 0, max = 6700, by = 1)

# First keygrame
cmds.select(player)    # Just in case
cmds.currentTime(0)
cmds.move(0, 0, 0)
cmds.setKeyframe()

# Second keyframe
cmds.currentTime(200)
cmds.move(7, 0, 0)
cmds.setKeyframe()

# Third keyframe
cmds.currentTime(300)
cmds.rotate(0, 90, 0)
cmds.setKeyframe()

cmds.currentTime(400)
cmds.move(7, 0, -16)
cmds.setKeyframe()

cmds.currentTime(500)
cmds.rotate(0, 0, 0)
cmds.setKeyframe()

cmds.currentTime(600)
cmds.move(20, 0, -16)
cmds.setKeyframe()

cmds.currentTime(700)
cmds.rotate(0, 45, 0)
cmds.setKeyframe()

cmds.currentTime(800)
cmds.move(30, 0, -20)
cmds.setKeyframe()

cmds.currentTime(900)
cmds.rotate(0, 90, 0)
cmds.setKeyframe()

cmds.currentTime(1000)
cmds.move(30, 0, -29)
cmds.setKeyframe()

cmds.currentTime(1100)
cmds.rotate(0, 90, 90)
cmds.setKeyframe()

cmds.currentTime(1200)
cmds.move(30, 5, -29)
cmds.setKeyframe()

cmds.currentTime(1300)
cmds.rotate(0, 90, 0)
cmds.setKeyframe()

cmds.currentTime(1400)
cmds.move(30, 5, -39)
cmds.setKeyframe()

cmds.currentTime(1500)
cmds.rotate(0,90, -90)
cmds.setKeyframe()

cmds.currentTime(1600)
cmds.move(30, -5, -39)
cmds.setKeyframe()

cmds.currentTime(1700)
cmds.rotate(-90, 90, -90)
cmds.setKeyframe()

cmds.currentTime(1800)
cmds.move(30, -5, -29)
cmds.setKeyframe()

cmds.currentTime(1900)
cmds.rotate(0, 0, 0)
cmds.setKeyframe()

cmds.currentTime(2000)
cmds.move(46, -5, -29)
cmds.setKeyframe()

cmds.currentTime(2100)
cmds.rotate(0, 0, 90)
cmds.setKeyframe()

cmds.currentTime(2200)
cmds.move(46, 0, -29)
cmds.setKeyframe()

cmds.currentTime(2300)
cmds.rotate(90, 0, 90)
cmds.setKeyframe()

cmds.currentTime(2400)
cmds.move(46, 0, 0)
cmds.setKeyframe()

cmds.currentTime(2500)
cmds.rotate(0, -180, 0)
cmds.setKeyframe()

cmds.currentTime(2600)
cmds.move(30, 0, 0)
cmds.setKeyframe()

cmds.currentTime(2700)
cmds.rotate(0, -90, 0)
cmds.setKeyframe()

cmds.currentTime(2800)
cmds.move(30, 0, 10)
cmds.setKeyframe()

cmds.currentTime(2900)
cmds.rotate(0, -60, 0)
cmds.setKeyframe()

cmds.currentTime(3000)
cmds.move(38, 0, 34)
cmds.setKeyframe()

cmds.currentTime(3100)
cmds.rotate(0, -180, 0)
cmds.setKeyframe()

cmds.currentTime(3200)
cmds.move(32, 0, 34)
cmds.setKeyframe()

cmds.currentTime(3300)
cmds.rotate(0, -90, 0)
cmds.setKeyframe()

cmds.currentTime(3400)
cmds.move(32, 0, 47)
cmds.setKeyframe()

cmds.currentTime(3500)
cmds.rotate(0, 0, 0)
cmds.setKeyframe()

cmds.currentTime(3600)
cmds.move(53, 0, 47)
cmds.setKeyframe()

cmds.currentTime(3700)
cmds.rotate(0, 90, 0)
cmds.setKeyframe()

cmds.currentTime(3800)
cmds.move(53, 0, 34)
cmds.setKeyframe()

cmds.currentTime(3900)
cmds.rotate(0, 45, 0)
cmds.setKeyframe()

cmds.currentTime(4000)
cmds.move(65, 0, 30)
cmds.setKeyframe()

cmds.currentTime(4100)
cmds.rotate(0, -45, 0)
cmds.setKeyframe()

cmds.currentTime(4200)
cmds.move(70, 0, 43)
cmds.setKeyframe()

cmds.currentTime(4300)
cmds.rotate(0, 45, 0)
cmds.setKeyframe()

cmds.currentTime(4400)
cmds.move(90, 0, 25)
cmds.setKeyframe()

cmds.currentTime(4500)
cmds.rotate(0, 135, 0)
cmds.setKeyframe()

cmds.currentTime(4600)
cmds.move(84, 0, 19)
cmds.setKeyframe()

cmds.currentTime(4700)
cmds.rotate(0, 225, 0)
cmds.setKeyframe()

cmds.currentTime(4800)
cmds.move(76, 0, 22)
cmds.setKeyframe()

cmds.currentTime(4900)
cmds.rotate(0, 135, 0)
cmds.setKeyframe()

cmds.currentTime(5000)
cmds.move(60, 0, 12)
cmds.setKeyframe()

cmds.currentTime(5100)
cmds.rotate(0, 80, 0)
cmds.setKeyframe()

cmds.currentTime(5200)
cmds.move(65, 0, -11)
cmds.setKeyframe()

cmds.currentTime(5300)
cmds.rotate(0, 135, 0)
cmds.setKeyframe()

cmds.currentTime(5400)
cmds.move(57, 0, -15)
cmds.setKeyframe()

cmds.currentTime(5500)
cmds.rotate(0, 90, 0)
cmds.setKeyframe()

cmds.currentTime(5600)
cmds.move(57, 0, -39)
cmds.setKeyframe()

cmds.currentTime(5700)
cmds.rotate(0, 0, 0)
cmds.setKeyframe()

cmds.currentTime(5800)
cmds.move(78, 0, -39)
cmds.setKeyframe()

cmds.currentTime(5900)
cmds.rotate(0, -90, 0)
cmds.setKeyframe()

cmds.currentTime(6000)
cmds.move(78, 0, -17)
cmds.setKeyframe()

cmds.currentTime(6100)
cmds.rotate(0, -135, 0)
cmds.setKeyframe()

cmds.currentTime(6200)
cmds.move(74, 0, -10)
cmds.setKeyframe()

cmds.currentTime(6300)
cmds.rotate(0, -90, 0)
cmds.setKeyframe()

cmds.currentTime(6400)
cmds.move(75, 0, 0)
cmds.setKeyframe()

cmds.currentTime(6500)
cmds.rotate(0, 0, 0)
cmds.setKeyframe()

cmds.currentTime(6600)
cmds.move(100, 0, 0)
cmds.setKeyframe()
