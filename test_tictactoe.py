import unittest

from tictactoe import *


class TestFunctions(unittest.TestCase):

    def test_player(self):
        board = [[EMPTY, EMPTY, X],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, O]]
        self.assertTrue(player(board)==X)
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertTrue(player(board)==X)
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertTrue(player(board)==O)


    def test_actions(self):
        board = [[EMPTY, X, X],
                [O, O, O],
                [O, O, O]]
        self.assertTrue(actions(board)=={(0,0)})
        board = [[X, EMPTY, EMPTY],
                [O, O, O],
                [O, O, O]]
        self.assertTrue(actions(board)=={(0,1),(0,2)})
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertTrue(actions(board)=={(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)})


    def test_result(self):
        board = [[EMPTY, EMPTY, X],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, O]]
        action = (1,1)
        board2=[[EMPTY, EMPTY, X],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, O]]
        self.assertTrue(result(board, action)==board2)
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, O]]
        action = (0,2)
        board2=[[EMPTY, EMPTY, X],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, O]]
        self.assertTrue(result(board, action)==board2)
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, O]]
        action = (2,0)
        board2=[[EMPTY, EMPTY, EMPTY],
                [EMPTY, X, EMPTY],
                [X, EMPTY, O]]
        self.assertTrue(result(board, action)==board2)
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, O]]
        action = (1,1)
        self.assertRaises(Exception, result, board, action)


    def test_winner(self):
        board = [[X, X, X],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, O, O]]
        self.assertTrue(winner(board)==X)
        board = [[X, O, O],
                [X, EMPTY, EMPTY],
                [X, O, X]]
        self.assertTrue(winner(board)==X)
        board = [[X, O, O],
                [X, X, O],
                [O, X, X]]
        self.assertTrue(winner(board)==X)
        board = [[EMPTY, O, O],
                [X, X, O],
                [X, O, X]]
        self.assertTrue(winner(board)==None)


    def test_terminal(self):
        board = [[X, X, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, O, O]]
        self.assertFalse(terminal(board))
        board = [[X, O, O],
                [X, EMPTY, EMPTY],
                [X, O, X]]
        self.assertTrue(terminal(board))
        board = [[X, X, O],
                [O, O, X],
                [X, O, X]]
        self.assertTrue(terminal(board))
        board = [[EMPTY, O, O],
                [X, X, O],
                [X, O, X]]
        self.assertFalse(terminal(board))


if __name__ == '__main__':
    unittest.main()
