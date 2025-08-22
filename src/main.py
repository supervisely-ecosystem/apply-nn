import os

import dotenv
import supervisely as sly
from supervisely._utils import sly_env
from supervisely.nn.inference.predict_app.predict_app import PredictApp

dotenv.load_dotenv(os.path.expanduser("~/supervisely(dev).env"))
dotenv.load_dotenv("local.env")

api = sly.Api()
predict_app = PredictApp(api)
app = predict_app.app

def get_load_data_from_env():
    project_id = sly_env.project_id(raise_not_found=False)
    dataset_id = sly_env.dataset_id(raise_not_found=False)
    input_data = {}
    if dataset_id:
        input_data = {"dataset_ids": [dataset_id]}
    elif project_id:
        input_data = {"project_id": project_id}
    train_task_id = os.environ.get("modal.state.trainTaskId", None)
    model_data = None
    if train_task_id:
        model_data = {
            "mode": "custom",
            "train_task_id": int(train_task_id),
        }
    data = {
        "input": input_data,
    }
    if model_data:
        data["model"] = model_data

    should_run = os.environ.get("modal.state.run", "false").lower() == "true"
    stop_after_run = os.environ.get("modal.state.stopAfterRun", "false").lower() == "true"

    data["run"] = should_run
    data["stop_after_run"] = stop_after_run
    return data

predict_app.load_from_json(get_load_data_from_env())
