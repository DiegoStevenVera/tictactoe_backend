from pydantic import BaseModel


class State_action(BaseModel):
    end_game: bool = False
    winner: int = -2
    hash_board: str = '[0. 0. 0. 0. 0. 0. 0. 0. 0.]'