# CS5830_A6
## Description
This repository contains the code for Assignment 6 of CS5830. The task was to build a `FastAPI` application for a digit-classification task. The descriptions of all files and directories in the repository can be found below. <br/>
1. `Build a FastAPI ... .pdf`	:	Task decription
2. `MNIST.ipynb`		:	Python Notebook to build an MLP for the MNIST digit classification task
3. `mnistmlp.keras`		:	Trained MLP used for digit classification
4. `mnistapi.py`		:	Python file to set up the `FastAPI` application. The image required for classification is uploaded in the Swagger UI and `mnistmlp.keras` classifies the image. This image must have a black background, with the digit in white. The user's own images can be used.
5. `sample_images/`		:	Directory with some custom images. These images are not part of the MNIST dataset. They have been drawn by the author, to test the `FastAPI` app.
6. `requirements.txt`		:	Text file with the Python libraries and dependencies for this project. Can be installed using `conda`.

## Installation
1. Clone the Git Repository: `git clone https://github.com/MelpakkamPradeep/CS5830_A6.git`
2. Navigate to the downloaded repository.
3. Install the dependencies: `conda create --name <env name>`. Then `conda install pip` and `pip install -r requirements.txt`.

## Usage
1. Navigate to the cloned repository, and begin the Uvicorn server using `uvicorn mnistapi:app --reload`.
2. Upload the required image in the `/predict` function in the Swagger UI of the server.
3. The output is displayed as `{'digit': _predn_}`
