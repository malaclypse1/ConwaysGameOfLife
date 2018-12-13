def addBlinker(gameInstance, pos):
    x, y = pos
    gameInstance.addCell((x, y + 1))
    gameInstance.addCell((x + 1, y + 1))
    gameInstance.addCell((x + 2, y + 1))


def addToad(gameInstance, pos):
    x, y = pos
    gameInstance.addCell((x + 1, y + 1))
    gameInstance.addCell((x + 2, y + 1))
    gameInstance.addCell((x + 3, y + 1))
    gameInstance.addCell((x, y + 2))
    gameInstance.addCell((x + 1, y + 2))
    gameInstance.addCell((x + 2, y + 2))


def addGlider(gameInstance, pos):
    x, y = pos
    gameInstance.addCell((x + 2, y))
    gameInstance.addCell((x + 2, y + 1))
    gameInstance.addCell((x, y + 1))
    gameInstance.addCell((x + 1, y + 2))
    gameInstance.addCell((x + 2, y + 2))
