from pydantic import BaseSettings
from models.player import Player, HumanPlayer
from models.state import State


class Settings(BaseSettings):
    API_V1_STR: str = "/API/V1"
    PROJECT_NAME: str = "TICTACTOE"
    FILES_PATH = 'files'
    TOKENS: object = None
    TICTACTOE_RULES: object = None
    p1: Player = Player("p1", exp_rate=-1)
    h1: HumanPlayer = HumanPlayer('human')
    st: State = State(p1, h1)
    p1.loadPolicy(f"{FILES_PATH}/policy_p1")

    class Config:
        env_file = ".env"

settings = Settings()