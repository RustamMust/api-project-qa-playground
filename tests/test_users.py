import allure
import pytest

from config.base_test import BaseTest


@allure.epic('Administration')
@allure.feature('Users')
class TestUsers(BaseTest):

    @pytest.mark.regression
    @allure.title('Create new user')
    def test_create_user(self):
        response, model = self.api_users.create_user()
        self.api_users.get_user_by_id(model.uuid)
        assert response.status_code == 200, response.json()
        assert len(model.email) > 0, 'Email is not valid'
        assert len(model.name) > 0, 'Name is not valid'
        assert len(model.nickname) > 0, 'Nickname is not valid'
        assert len(model.uuid) > 0, 'UUID is not valid'
