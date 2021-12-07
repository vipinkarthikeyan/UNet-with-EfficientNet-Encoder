# Import the necessary libraries

import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import load_model

# This loads the EfficientNetB7 model from the Keras library
# Input Shape is the shape of the image that is input to the first layer. For example, consider an image with shape (width, height , number of channels)
# 'include_top' is set to 'False' to load the model with out the classification or dense layers. Top layers are not required as this is a segmentation problem.
# 'weights' is set to imagenet, that is, it uses the weight it learnt while training on the imagenet dataset. You can set it to None or your custom_weights.

model = tf.keras.applications.EfficientNetB7(input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, CHANNELS), include_top=False, weights="imagenet")

#To see the list of layers and parameters

model.summary()
