from fastapi import APIRouter
from models.action import State_action
from services import predict_action


router = APIRouter()

@router.get('/', response_model=State_action)
def state_action_response_example():
    return State_action()

@router.get('/begin-match', response_model=State_action)
def match_begin():
    is_end, winner, board_map = predict_action.start_match()
    return State_action(end_game=is_end, winner=winner, hash_board=board_map)

@router.post('/predict-next-move', response_model=State_action)
def next_move_ai(row: int, col: int):
    is_end, winner, board_map = predict_action.predict_next_action((row, col))
    return State_action(end_game=is_end, winner=winner, hash_board=board_map)