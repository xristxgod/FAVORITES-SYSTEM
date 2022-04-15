from src import *
from config import logger

class FavoritesUsers:

    def __init__(self):
        self.__favorites_users: typing.List = []

    def change_to_favorites(self, user_id: int) -> str:
        for index, user in enumerate(self.__favorites_users):
            if user == user_id:
                del self.__favorites_users[index]
                return "del"
        else:
            self.__favorites_users.append(user_id)
            return "add"

    async def select_all_users(self) -> bool:
        try:
            self.__favorites_users = await db.get_users_id()
            return True
        except Exception as error:
            logger.error(f"ERROR STEP 20: {error}")
            return False

    def is_in_favorites(self, user_id: int) -> bool:
        for user in self.__favorites_users:
            if user == user_id:
                return True
        else:
            return False

    @property
    def get_user_favorite(self) -> typing.List[int]:
        return self.__favorites_users

    def clear_favorites_users(self) -> None:
        self.__favorites_users = []