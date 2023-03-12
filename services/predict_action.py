from core.config import settings

def start_match():
    settings.st.reset()
    positions = settings.st.availablePositions()
    p1_action = settings.st.p1.chooseAction(positions, settings.st.board, settings.st.playerSymbol)
    settings.st.updateState(p1_action)
    board_hash = settings.st.getHash()
    settings.st.p1.addState(board_hash)
    return settings.st.isEnd, -2, board_hash

# action_human : (row, col) (int, int)
def predict_next_action(action_human):
    win = 0
    end = False
    settings.st.updateState(action_human)
    board_map = settings.st.getHash()
    win = settings.st.winner()

    if win is not None:
        end = settings.st.isEnd
        settings.st.giveReward()
        settings.st.p1.reset()
        settings.st.reset()
        
        return end, win, board_map

    positions = settings.st.availablePositions()
    p1_action = settings.st.p1.chooseAction(positions, settings.st.board, settings.st.playerSymbol)
    settings.st.updateState(p1_action)
    board_hash = settings.st.getHash()
    settings.st.p1.addState(board_hash)

    win = settings.st.winner()
    if win is not None:
        end = settings.st.isEnd
        settings.st.giveReward()
        settings.st.p1.reset()
        settings.st.reset()
    
    win = -2 if win is None else win
    return end, win, board_hash