A simple webapp to predict the IRIS flower species.

The repository contains the files such as 

requirements.txt (all letter lowercase) in the root of the folder in order for heroku to start the build pack
runtime.txt (all letters lowercase) in the root folder to tell heroku that which python version to use
app.py contains the web app codes
model.pkl amd model.py are nothing but same but in two different formats. model.pkl is used in app.py.
Under the folder templates, there html file index.html which is actual web file
under the folder static, the style CSS file for the index.html


In the web page, once the web app deployed in heroku, after the inputs of the sepal length, sepal width, petal length and petal width, on clicking the 
predict button, the predicted species will be displayed.

