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
server = app.get_server()


def get_load_data_from_env():
    project_id = sly_env.project_id(raise_not_found=False)
    dataset_id = sly_env.dataset_id(raise_not_found=False)
    items_data = {}
    if dataset_id:
        items_data = {"dataset_ids": [dataset_id]}
    elif project_id:
        items_data = {"project_id": project_id}
    train_task_id = os.environ.get("modal.state.trainTaskId", None)
    model_data = None
    if train_task_id:
        model_data = {
            "mode": "custom",
            "train_task_id": int(train_task_id),
        }
    data = {
        "items": items_data,
    }
    if model_data:
        data["model"] = model_data
    return data


predict_app.load_from_json(get_load_data_from_env())


@server.post("/run_preview")
async def preview(request):
    """
    Run a preview of the model prediction on sample images.

    Example data:
        data = {
            "model": {
                "mode": "connect",
                "session_id": <task_id>,
                "agent_id": <agent_id>,
            },
            "inference_settings": {
                "conf": 0.6,
            },
            "items": {
                # "project_id": ...,
                # "dataset_ids": [...],
                "image_ids": [1148679, 1148675],
            },
            "output": {"mode": "iou_merge", "iou_merge_threshold": 0.5},
        }
    """
    req = await request.json()
    try:
        state = req["state"]
        data = state["data"]
        if "items" not in data:
            raise ValueError("No items found in the request data.")
        image_ids = data["items"].get("image_ids", None)
        if not image_ids:
            raise ValueError("No image IDs ('image_ids') provided for preview.")
        predictions = predict_app.gui.model.model_api.predict(
            image_id=image_ids, **predict_app.gui.get_inference_settings()
        )
        anns = [pred.annotation.to_json() for pred in predictions]
        return {"data": anns}
    except Exception as e:
        sly.logger.error(f"Error during preview: {e}")
        return {"error": str(e)}


@server.post("/run_prediction")
async def run(request):
    """
    Run the model prediction.
    This endpoint processes the request data, runs the model prediction.

    Example data:
        data = {
            "model": {
                "mode": "connect",
                "session_id": <task_id>,
                "agent_id": <agent_id>,
            },
            "inference_settings": {
                "conf": 0.6,
            },
            "items": {
                # "project_id": ...,
                # "dataset_ids": [...],
                "image_ids": [1148679, 1148675],
            },
            "output": {"mode": "iou_merge", "iou_merge_threshold": 0.5},
        }
    """
    req = await request.json()
    try:
        state = req["state"]
        data = state["data"]
        predict_app.load_from_json(data)
        predictions = predict_app.gui.run()
        if not predictions:
            raise ValueError("No predictions were made. Check the model and input data.")
        return {
            "data": f"Prediction completed successfully: {len(predictions)} annotations created in the project (ID: {predictions[0].project_id})"
        }
    except Exception as e:
        sly.logger.error(f"Error during run: {e}")
        return {"error": str(e)}
