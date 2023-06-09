import numpy as np
from PIL import Image
import tensorflow as tf
import os
from flask import current_app as app
from skimage.transform import resize
from skimage.io import imread, imshow

IMG_WIDTH = 256
IMG_HEIGHT = 256
IMG_CHANNELS = 3

import tensorflow as tf
from keras import backend as K

def jaccard_iou(y_true, y_pred):
  y_true_f = K.flatten(y_true)
  y_pred_f = K.flatten(y_pred)
  intersection = K.sum(y_true_f*y_pred_f)

  return (intersection)/(K.sum(y_true_f)+K.sum(y_pred_f)-intersection)


custom_objects = {'jaccard_iou': jaccard_iou}
linknet_model = tf.keras.models.load_model('app/seg_models/Unet/models/unet_model.h5', custom_objects=custom_objects)


def segment_image(filename):
    filepath = os.path.join('app', app.config['UPLOAD_FOLDER'], filename)

    input_image = imread(filepath)[:, :, :IMG_CHANNELS]
    input_image = resize(input_image, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)

    prediction = linknet_model.predict(input_image[tf.newaxis, ...])[0]

    predicted_mask = (prediction > 0.5).astype(np.uint8)
    output_image = tf.keras.utils.array_to_img(predicted_mask)

    output_image_path = os.path.join('app', app.config['UPLOAD_FOLDER'], 'seg_' + filename)
    output_image.save(output_image_path)


