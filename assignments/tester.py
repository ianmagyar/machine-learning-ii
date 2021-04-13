from bots import RandomBot
from solution import StudentAgent
from tictactoe import TicTacToe


# TODO: add path to your saved model
STUDENT_SOLUTION_PATH = ''


def test_agents(p1_type, p2_type):
    board = TicTacToe()

    player_1 = p1_type(code=1)
    player_2 = p2_type(code=-1)

    if isinstance(player_1, StudentAgent):
        player_1.load_agent(STUDENT_SOLUTION_PATH)
    if isinstance(player_2, StudentAgent):
        player_2.load_agent(STUDENT_SOLUTION_PATH)

    one_wins, two_wins, ties = 0, 0, 0
    TESTS = 500

    for _ in range(TESTS):
        board.reset()
        while not board.isDone():
            state = board.get_state().copy()
            p1_action = player_1.act(state)

            new_state, reward, done, _ = board.step(
                p1_action, player_1.get_code())

            if board.isDone():
                break

            state = new_state.copy()
            p2_action = player_2.act(state)
            new_state, reward, done, _ = board.step(
                p2_action, player_2.get_code())

        result = board.has_won()
        if result == 1:
            one_wins += 1
        elif result == -1:
            two_wins += 1
        else:
            ties += 1

    return one_wins, two_wins, ties


def test_against_random():
    student_wins, random_wins, all_ties = 0, 0, 0

    p1_wins, p2_wins, ties = test_agents(StudentAgent, RandomBot)
    student_wins += p1_wins
    random_wins += p2_wins
    all_ties += ties

    p1_wins, p2_wins, ties = test_agents(RandomBot, StudentAgent)
    student_wins += p2_wins
    random_wins += p1_wins
    all_ties += ties

    print("Student agent wins {} times".format(student_wins))

    assert student_wins > 500


if __name__ == '__main__':
    test_against_random()
