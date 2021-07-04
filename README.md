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
* The estimated 5-year survival rate for patients whose melanoma is detected early is about 98 percent in the U.S. The survival rate falls to 62 percent when the disease reaches the lymph nodes and 18 percent when the disease metastasizes to distant organs.
* Early detection is critical.


## Development Process <a name="process"></a>
This principle component of this project is a CNN model that can predict the probability of a pole being malign. 

Dataset: https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000



## Model Creation <a name="model"></a>
Built the CNN model from scratch, the key features implemented in the model are:
* **Conv2d** - All the convolutional layers have the same parameters except the input channel and output channel size.
* **MaxPool2d** - Downsamples the input along its spatial dimensions (height and width) by taking the maximum value over an input window (of size defined by pool_size) for each channel of the input.
* **BatchNormalization** - Used it to nullify the effect of an undesirable output from any specific layer by normalizing the values coming from the previous layer.
* **Dropout** - It is used for a better generalization of a model as it turns off a percentage of neurons randomly during training, which results in a more generalized model.
* **Flatten** - Used to turn the multi-dimensional output from the convolutional and max-pooling layers into one-dimensional tensor, to perform predictions.



## Website & Docker Image <a name="website"></a>
Used the Flask framework in python for creating the backend of the website, and used HTML, CSS, and Bootstrap for the structure and designing of each page. The input is taken in as a file and is checked whether it is an image or not using the extension of the file. The image is firstly stored in the static folder which, after each refresh, empties itself, so any image uploaded will be lost after a refresh. After the image has been uploaded and stored, it will be processed so that it is compatible with our model, and then passed to the model for classification. The result from the model is then displayed on the same page using jinja2. As for any type of error, we have used Flask framework's Flash messages module for displaying that error to the user in a readable format.

After the website was created, we added the Dockerfile file to our directory for the purpose of creating a docker image of our project, we also had to modify our Flask code for it to run in a docker container. Since ports are dynamically allocated each time in a docker container we had to fetch the port, for our website to run on, at runtime. All that was left now was to build the docker image, test it for bugs and finally push the docker image on DockerHub.



## Deployment <a name="deploy"></a>

For the deployment of our project, we chose Heroku for its free tier option and easy-to-understand procedure. Since we already had created the docker image of our project, we just needed to add one more file called heroku.yml which will tell our Heroku server which Dockerfile to build (Though we only have one Docker container here, this feature is useful when we have multiple Docker container and a docker-compose.yml) and now our project has all the files needed to be deployed on Heroku. Before pushing our website on Heroku, for it to be deployed as a container we first have to set the stack of our Heroku app to container mode. After that's done, all we need to do is push our application on Heroku and release it.



## References <a name="refernces"></a>
* https://docs.python.org/3.9/
* https://docs.docker.com/language/python/
* https://flask.palletsprojects.com/en/2.0.x/
* https://www.tensorflow.org/api_docs/python/tf/all_symbols
* https://devcenter.heroku.com/categories/python-support

