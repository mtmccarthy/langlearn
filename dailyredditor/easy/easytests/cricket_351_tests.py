import unittest
from easy.cricket_351 import *
from common import *


class TestGenerateGameState(unittest.TestCase):

    def setUp(self):
        self.path = "./cricket_351_simple_input.txt"
        self.challenge_path = "./cricket_351_challenge_input.txt"
        self.test_game_state = ("P1",
                                "P2",
                                {"P1": 7, "P2": 2, "P3": 9},
                                2,
                                4,
                                ["P3"],
                                []
                                )

    def test_generate_game_state(self):
        game_state = None
        score = get_file_lines(self.challenge_path)[0]  # 'WWWWWWWWWWW...'
        self.assertEquals(game_state, generate_game_state(score))
        next_score = get_file_lines(self.challenge_path)[1]
        expected_game_state = ("P3",
                               "P1",
                               {"P1": 1, "P2": 6, "P3": 6, "P4": 0, "P5": 0, "P6": 0, "P7": 0, "P8": 0, "P9": 0, "P10": 0, "P11": 0},
                               1,
                               1,
                               ["P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11"],
                               ["P2"])
        self.assertEquals(expected_game_state, generate_game_state(next_score))

    def test_make_game_state(self):
        expected_gs = ("P1",
                       "P2",
                       {"P1": 0, "P2": 0, "P3": 0, "P4": 0, "P5": 0, "P6": 0, "P7": 0, "P8": 0, "P9": 0, "P10": 0, "P11": 0},
                       0,
                       0,
                       ["P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11"],
                       []
                       )
        self.assertEquals(expected_gs, make_game_state(10))

    def test_add_runs_to_striker(self):
        game_state = self.test_game_state

        new_game_state = add_runs_to_striker(game_state, 4)

        striker = new_game_state[0]

        self.assertEquals(11, new_game_state[2][striker])
        self.assertEquals(striker, game_state[0])

    def test_add_extra_run(self):
        expected_gs = ("P1", "P2", {"P1": 7, "P2": 2, "P3": 9}, 4, 4, ['P3'], [])
        self.assertEquals(expected_gs, add_extra_run(self.test_game_state, 2))

    def test_add_ball(self):
        expected_game = ("P1",
                         "P2",
                         {"P1": 7, "P2": 2, "P3": 9},
                         2,
                         5,
                         ["P3"],
                         []
                         )
        self.assertEquals(expected_game, add_ball(self.test_game_state))

        example_over_out = ("P3",
                            "P2",
                            {"P1": 7, "P2": 2, "P3": 9},
                            2,
                            0,
                            [],
                            ["P1"]
                            )

        self.assertEquals(example_over_out,
                          add_ball(add_ball(self.test_game_state)))

    def test_swap_striker(self):
        expected_game_state = ("P3",
                               "P2",
                               {"P1": 7, "P2": 2, "P3": 9},
                               2,
                               4,
                               [],
                               ["P1"]
                               )
        self.assertEquals(expected_game_state, swap_striker(self.test_game_state))


class TestGameStateStr(unittest.TestCase):

    def setUp(self):
        pass

    def test_game_state_str(self):
        game_state = ("P1", "P2", {"P1": 7, "P2": 2, "P3": 9}, 2)
        self.assertEquals("P1: 7\nP2: 2\nP3: 9\nExtras: 2", game_state_str(game_state))



