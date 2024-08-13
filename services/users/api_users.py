import allure
import requests

from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from utils.helper import Helper
from config.headers import Headers
from services.users.models.user_model import UserModel


class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step('Create user')
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return response, model

    @allure.step('Get user by Id')
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic
        )
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return response, model

