# UNet-with-EfficientNet-Encoder
The UNet model used for segmentation takes in different encoders. From in-built and pretrained models on Keras to custom encoders with custom weights, the choices are plenty. In this repository I share my compilation of UNet models with EfficientNetB0 to EfficientNetB7 encoder.

- EfficientNet_B0
- EfficientNet_B1
- EfficientNet_B2
- EfficientNet_B3
- EfficientNet_B4
- EfficientNet_B5
- EfficientNet_B6
- EfficientNet_B7

The EfficientNet family of networks (B0, B1, ..., B7), introduced by Mingxing Tan and Quoc V. Le dominated the ImageNet charts achieving higher accuracy with lesser number of parameter through efficient depth, width and resolution scaling/ compound scaling of models.

![image](https://user-images.githubusercontent.com/47257557/144846483-32cd13b5-7b73-40d0-9bbf-51db19f0a1ab.png)

Link to paper: https://arxiv.org/pdf/1905.11946.pdf

## Libraries and Version

- Python (3.9)
- Tensorflow (2.5.1)
- Keras (2.5.0)
- Tensorflow add-ons (0.14.0)

You can install these libraries using pip

 - pip install tensorflow==2.5.1 for CPU-only
 - pip install tensorflow-gpu==2.5.1 for systems with GPU support (Ubuntu and Windows)
 - pip install keras
 - pip install tensorflow-addons
  
  To use addons:
  
    import tensorflow as tf
    
    import tensorflow_addons as tfa
