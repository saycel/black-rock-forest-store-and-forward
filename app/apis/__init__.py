from flask_restplus import Api
from app.apis.login import api as login_api
from app.apis.sensor import api as forest_data_api


class BlackForestApi(Api):
    def update_doc(self, doc):
        self._doc = doc


api = BlackForestApi()
api.add_namespace(login_api)
api.add_namespace(forest_data_api)
