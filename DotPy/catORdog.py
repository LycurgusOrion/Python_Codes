# Importing Keras library and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import model_from_json

import numpy as np
import config



def Main():

	# Load the Model
	json_file = open("classifier.json", "r")
	loaded_model_json = json_file.read()
	json_file.close()

	classifier = model_from_json(loaded_model_json)
	classifier.load_weights("classifier.h5")
	print("Loaded Models")

	classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

	# Part - 3 - Predicting New Image
	test_image = image.load_img(config.TEST_IMAGE,
								target_size=(64, 64))

	test_image = image.img_to_array(test_image)

	test_image = np.expand_dims(test_image, axis=0)

	result = classifier.predict(test_image)

	# training_set.class_indices

	if result[0][0] == 1:
		prediction = "dog"
	else:
		prediction = "cat"

	print(prediction)


if __name__ == "__main__":
	Main()
