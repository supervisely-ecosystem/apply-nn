import os

import dotenv
import supervisely as sly
from supervisely.nn.inference.predict_app.predict_app import PredictApp

dotenv.load_dotenv(os.path.expanduser("~/supervisely(dev).env"))
dotenv.load_dotenv("local.env")

api = sly.Api()
predict_app = PredictApp(api)
app = predict_app.app
