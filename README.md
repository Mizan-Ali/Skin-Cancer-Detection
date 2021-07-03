# Skin Cancer Detection

### Website: https://skin-cancer-v1.herokuapp.com/

### Docker Image: https://hub.docker.com/r/conero007/skin-cancer-detection

---
## Table of Contents
* [Project Summary](#summary)
* [Development Process](#process)
* [Model Creation](#model)
* [Website](#website)
* [Deployment](#deploy)
* [Refernces](#refernces)

---

## Project Summary <a name="summary"></a>
This tool takes the image of a mole as an input and calculates the probability of that mole being malign (Cancerous).
Skin Cancer is a common disease these days.
* A total of 18.1 million new cases and 9.6 million deaths from skin cancer were estimated globally in 2018.
* A recent study on the epidemiology of skin cancer stated that in Europe, the incidence would increase to 40–50/100,000 inhabitants per year in the next decade. 
* Studies from India report clinicopathological evaluation and also focus on the current scenarios of NMSCs
* The estimated 5-year survival rate for patients whose melanoma is detected early is about 98 percent in the U.S. The survival rate falls to 62 percent when the disease reaches the lymph nodes, and 18 percent when the disease metastasizes to distant organs.
* Early detection is critical.

> 

## Development Process <a name="process"></a>
This principal component of this project is a CNN model that can predict the probability of a pole being malign.
Dataset: https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000

>



## Model Creation <a name="model"></a>
Built a CNN model from scratch, the key features implemented in the model are:
* **Conv2d** - All the convlutional layers have the same parameters except the input channel and output channel size.
* **MaxPool2d** - Downsamples the input along its spatial dimensions (height and width) by taking the maximum value over an input window (of size defined by pool_size) for each channel of the input.
* **BatchNormalization** - Used it to nullify the affect of an undesirable output from any specific layer by normalizing the values coming from the previous layer/
* **Dropout** - It is used for a better generalization of a model as it turns off a percentage of neurons randomly during training, which results in a more generalized model.
* **Flatten** - Used to turn the multi-dimensional output from the convolutional and max-pooling layers into a one dimentional tensor, to perform predictions.



> 


## Website <a name="website"></a>

flask api - backend
html + css + bootstrap



> 


## Deployment <a name="deploy"></a>

Docker image
deployed as container on heroku


> 


## References <a name="refernces"></a>
Docker doc
tf docs
flask doc
