<div align="center" markdown>
<img src="https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/app-poster.jpg"/>

# Predict App

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervisely.com/apps/supervisely-ecosystem/apply-nn)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/apply-nn)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/apply-nn.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/apply-nn.png)](https://supervisely.com)

</div>

# Overview

**Apply NN** is an all-in-one tool for deploying and using neural network models on the Supervisely platform.

With this app you can:

- Serve pretrained or custom models (trained inside Supervisely)
- Connect to already running serving sessions
- Perform inference on a **project** or a specific **dataset**
- Configure inference settings

When you select a model (e.g. `YOLO11n-det`), **Apply NN** will automatically launch the corresponding serving app (e.g. **[Serve YOLOv8 - v12](https://ecosystem.supervisely.com/apps/yolo/supervisely_integration/serve)**).

# How To Use

## Step 1. Select Data to Predict

Select images project or video to predict.

![Step 1](https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/step-1-predict-app.png)

## Step 2. Select Model

Connect to an already running serving session or select a model to deploy.

![Step 2.1](https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/step-2-2-predict-app.png)

Wait for the model to be deployed and press Select button.

![Step 2.2](https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/step-2-predict-app.png)

## Step 3. Select Classes

Select classes to predict.

![Step 3](https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/step-3-predict-app.png)

## Step 4. Configure Inference Settings

![Step 4](https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/step-4-predict-app.png)

## Step 5. Enter output project name and press Run button

![Step 5](https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/step-5-predict-app.png)

## Step 6. Wait for the process to finish

![Step 6](https://github.com/supervisely-ecosystem/apply-nn/releases/download/v0.0.1/step-6-predict-app.png)
