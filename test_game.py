from unittest import TestCase
from game import *


class TestGame(TestCase):
    def test_world_has_live_cell_list(self):
        game = Game()
        self.assertTrue(isinstance(game.liveCells, dict), 'World contains no list of cells')

    # def test_cell_has_position_tuple(self):
    #     cell = Cell()
    #     self.assertTrue(isinstance(cell.pos, tuple), 'Cell contains no position tuple')
    #
    # def test_cell_has_neighbor_count(self):
    #     cell = Cell()
    #     self.assertTrue(isinstance(cell.numNeighbors, int), 'Cell has no neighbor count')

    def test_world_has_one_cell(self):
        game, pos = self.setup()
        game.addCell(pos)

        self.assertEqual(len(game.liveCells), 1)

    def test_world_has_two_cells(self):
        game, pos = self.setup()
        game.addCell(pos)
        game.addCell((1, 1))

        self.assertEqual(len(game.liveCells), 2)

    def test_world_doesnt_dupe_cell(self):
        game, pos = self.setup()
        game.addCell(pos)
        game.addCell(pos)

        self.assertEqual(len(game.liveCells), 1)

    def test_cell_has_1_neighbor(self):
        game, pos = self.setup()
        game.addCell((1, 1))
        game.liveCells[pos] = game.countNeighbors(pos)

        self.assertEqual(game.liveCells[(0, 0)], 1)

    def setup(self):
        game = Game()
        pos = (0, 0)
        game.addCell(pos)
        return game, pos

    def test_updateNeighborCounts(self):
        game, pos = self.setup()
        game.addCell(pos)
        game.addCell((0, 1))
        game.addCell((1, 1))
        game.updateNeighborCounts()

        self.assertEqual(game.liveCells[pos], 2)

    def test_determineNewCells(self):
        game, pos = self.setup()
        game.addCell(pos)
        game.addCell((0,1))
        game.addCell((1,0))
        newCells = game.determineNewCells()

        self.assertEqual(newCells, {(1,1) : 3})
        self.assertNotEqual(newCells, {(1,2) : 3})

    def test_findDyingCells(self):
        game, pos = self.setup()
        game.addCell(pos)

        self.assertEqual(game.findDyingCells(), [(0,0)])

    def test_nextCycle(self):
        game, pos = self.setup()
        game.addCell(pos)
        game.addCell((0, 1))
        game.addCell((1, 0))
        game.updateNeighborCounts()
        game.nextCycle()

        self.assertEqual(len(game.liveCells), 4)