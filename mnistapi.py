from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import Sequential, load_model
import numpy as np
from PIL import Image
from io import BytesIO

# Create a new FastAPI instance
app = FastAPI()

def load_model_from_path(path:str) -> Sequential:
	model = load_model(path)
	return model
	
path = 'mnistmlp.keras'
mnist_model = load_model_from_path(path)

def process_and_predict(model: Sequential, data: list) -> str:
	data = np.array(data)
	data = data.astype('float32')
	data /= 255
	print(data.shape)
	prediction = np.argmax(model.predict(data.reshape(1, 784) ), axis=-1)
	return str(prediction)
	
@app.post('/predict')
async def predict_digit(image: UploadFile = File(...)):
	contents = await image.read()
	img = Image.open(BytesIO(contents))
	img = img.resize((28, 28))
	img = img.convert("L")
	img_array = np.array(img).flatten().tolist()
	prediction = process_and_predict(mnist_model, img_array)
	print(prediction)
	return {"digit": prediction}
