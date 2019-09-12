from flask_restplus import Api
from backend.apis.UserManagement import api as login_api
from backend.apis.sensor import api as forest_data_api
from backend.apis.data_uploader import api as data_uploader_api

class BlackForestApi(Api):
    def update_doc(self, doc):
        self._doc = doc


api = BlackForestApi()
api.add_namespace(login_api)
api.add_namespace(forest_data_api)
api.add_namespace(data_uploader_api)

