import pygame

class Game:
    def __init__(self):
        self.liveCells = dict()
        self.white = pygame.Color(255,255,255)

    def addCell(self, pos):
        self.liveCells[pos] = 0

    def countNeighbors(self, pos):
        neighboringCells = self.getNeighborPositions(pos)
        neighborCount = 0
        for cell in neighboringCells:
            if cell in self.liveCells:
                neighborCount += 1
        return neighborCount

    def getNeighborPositions(self, pos):
        (x,y) = pos
        return ((x-1, y-1),
                (x, y-1),
                (x+1, y-1),
                (x-1, y),
                (x+1,y),
                (x-1, y+1),
                (x, y+1),
                (x+1, y+1))

    def updateNeighborCounts(self):
        pass
        for cell in self.liveCells:
            self.liveCells[cell] = self.countNeighbors(cell)

    def determineNewCells(self):
        newCells = dict()
        for cell in self.liveCells:
            for adjacentCell in self.getNeighborPositions(cell):
                if adjacentCell not in self.liveCells and self.countNeighbors(adjacentCell) == 3:
                    newCells[adjacentCell] = 3
        return newCells

    def findDyingCells(self):
        dyingCells = list()
        for cell, neighbors in self.liveCells.items():
            if neighbors < 2 or neighbors > 3:
                dyingCells.append(cell)
        return dyingCells

    def nextCycle(self):
        cellsBeingBorn = self.determineNewCells()
        for cell in self.findDyingCells():
            del self.liveCells[cell]
        self.liveCells.update(cellsBeingBorn)
        self.updateNeighborCounts()

    def draw(self, screen, offset = (0,0), cellSize = (4,4), color = 'white'):
        if color == 'white':
            color = self.white
        for cell in self.liveCells:
            self.drawCell(cell, screen, offset, cellSize, color)

    def drawCell(self, cell, screen, offset, cellSize, color):
        cellRect = self.locateCell(cell, cellSize, offset)
        screen.fill(color, cellRect)

    def locateCell(self, cell, cellSize, offset):
        x, y = cell
        xscale, yscale = cellSize
        xoffset, yoffset = offset
        x = x * xscale + xoffset
        y = y * yscale + yoffset
        cellRect = pygame.Rect((x, y), cellSize)
        return cellRect
