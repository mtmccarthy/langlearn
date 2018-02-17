from typing import List, Dict, Tuple
from common import get_file_lines
from copy import copy

Player = str  # Name of player

# Striker, otherBatsman, Dict[Player, Runs], ExtraRuns, Number of balls, list of available players, struck out players
GameState = Tuple[Player, Player, Dict[Player, int], int, int, List[Player], List[Player]]


def make_game_state(num_players: int) -> GameState:
    striker = "P1"
    other_batsman = "P2"

    score_map = {}
    for i in range(0, num_players + 1):
        score_map["P" + str(i+1)] = 0

    return (striker,
            other_batsman,
            score_map,
            0,
            0,
            ["P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11"],
            []
            )


def get_player_index(index: str) -> int:
    return int(index[1:])


def add_runs_to_striker(gs: GameState, num_runs: int) -> GameState:
    striker = gs[0]

    prev_runs = gs[2][striker]
    new_runs = prev_runs + num_runs
    new_score_map = copy(gs[2])
    new_score_map[striker] = new_runs

    if num_runs % 2 == 0:
        return striker, gs[1], new_score_map, gs[3], gs[4], gs[5], gs[6]
    else:
        return gs[1], striker, new_score_map, gs[3], gs[4], gs[5], gs[6]


def add_extra_run(gs: GameState, num_extras: int) -> GameState:
    return gs[0], gs[1], gs[2], gs[3] + num_extras, gs[4], gs[5], gs[6]


def add_ball(gs: GameState) -> GameState:
    if gs[4] + 1 == 6:
        return swap_striker((gs[0], gs[1], gs[2], gs[3], 0, gs[5], gs[6]))
    else:
        return gs[0], gs[1], gs[2], gs[3], gs[4] + 1, gs[5], gs[6]


def swap_striker(gs: GameState) -> GameState:
    available_new_strikers = copy(gs[5])

    if len(available_new_strikers) == 0:
        return None

    next_striker = available_new_strikers.pop(0)  # deque the queue

    return next_striker, gs[1], gs[2], gs[3], gs[4], available_new_strikers, gs[6] + [gs[0]]


def parse_token(current_game_state: GameState, token: str) -> GameState:

    try:
        num_runs = int(token)
        return add_runs_to_striker(add_ball(current_game_state), num_runs)
    except ValueError:
        # Check for remaining possible input characters
        if token == '.':
            return add_ball(current_game_state)
        elif token == 'b':
            return add_extra_run(add_ball(current_game_state), 1)
        elif token == 'w':
            return add_extra_run(current_game_state, 1)
        elif token == 'W':
            return swap_striker(current_game_state)
        else:
            return None


def generate_game_state(score: str) -> GameState:
    tokens = list(score)
    current_game_state = make_game_state(10)

    for token in tokens:
        next_game_state = parse_token(current_game_state, token)
        if next_game_state is None:
            print("Game ended before final input could be read")
            return current_game_state
        else:
            current_game_state = next_game_state

    return current_game_state


def game_state_str(game_state: GameState) -> str:
    game_str = ""
    for player, personal_score in game_state[2].items():
        game_str += player + ": " + str(personal_score) + "\n"

    game_str += "Extras: " + str(game_state[3])

    return game_str


def main(path: str) -> ():
    lines = get_file_lines(path)

    for line in lines:
        game_state = generate_game_state(line)
        print(game_state_str(game_state))


if __name__ == '__main__':
    main('easytests/cricket_351_challenge_input.txt')

