import os
import flask
from flask import Flask, render_template, request
from src.recipe_api import get_recipes, picture_names
import jinja2
from jinja2 import Template

#---------- URLS AND WEB PAGES -------------#
# Directory of images to predict from
image_path_dir = 'static/images/testData/'

# Initialize the app
app = flask.Flask(__name__)
app.jinja_env.filters['zip'] =zip 

#------- >>>>> Main Homepage <<<<<< --------#
@app.route("/")
def readImages():
    """
    Homepage: serve our visualization page, index.html
    """
    return flask.render_template('index.html')

#------- >>>>> Recommend Page <<<<< --------#
# Get an example and return it's score from the predictor model
@app.route("/recommend", methods=["POST", "GET"])
def predict():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template)" (key): "string in the textbox" (value)
    cmd = "/usr/bin/automator P2R_workflow.workflow/"
    os.system(cmd)
    
    file_input,initial_img, preds,recoms_dict_Main,recoms_dict_Side,recoms_dict_Dessert,recoms_dict_Condiments,recoms_dict_Salad = get_recipes(request.args)
    return flask.render_template('recommender2.html',
                                    x_input=file_input,
                                    picture_names=picture_names,
                                    picture_inputs= initial_img,
                                    prediction=preds,
                                    recommended_list_Main=recoms_dict_Main,
                                    recommended_list_Side=recoms_dict_Side,
                                    recommended_list_Dessert=recoms_dict_Dessert,
                                    recommended_list_Condiments=recoms_dict_Condiments,
                                    recommended_list_Salad=recoms_dict_Salad,
                                    )


#--------- RUN WEB APP SERVER ------------#
# Start the app server on port 80
# (The default website port)
if __name__ == '__main__':

    app.run(debug=True)
