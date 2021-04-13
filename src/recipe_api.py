"""
Note this file contains _NO_ flask functionality.
Instead it makes a file that takes the input dictionary Flask gives us,
and returns the desired result.

This allows us to test if our modeling is working, without having to worry
about whether Flask is working. A short check is run at the bottom of the file.
"""

import pickle
import os
import numpy as np

from keras.models import load_model
from keras.applications import MobileNetV2
from recipeScripts import *

from keras import preprocessing
import tensorflow as tf 

# A hack for keras and tensorflow issues 
# From https://github.com/keras-team/keras/issues/6462
def get_extractor():
    global extractor
    extractor = load_model('models/extractor.hdf5')
    extractor._make_predict_function()
    print("Extractor Loaded")
def get_predictor():
    global predictor
    predictor = load_model('models/trained_model.hdf5')
    predictor._make_predict_function()
    print("Predictor Loaded")

#---------- MODEL IN MEMORY ----------------#
# Load Recipe dataframe
with open('models/df_epi_cleaner-5.pkl','rb') as fin:
    df = pickle.load(fin)

# Load Trained Model
# Calling Feature-Extractor and Predictor
get_extractor()
get_predictor()
class_dictionary = np.load('models/class_indices.npy').item()
inv_map = {v:k for k,v in class_dictionary.items()}

# List of images labels
picture_names =['Picture 1','Picture 2','Picture 3']

## Function to get recipes from input directory
def get_recipes(feature_dict):
# Feature_dict is collected from request.args in /recommend
# feature_dict is a dictionary {"name":"value"}

    # file_input contains fienames, stored as a list
    # file_input = [
    #     str(feature_dict.get(name,'1.jpg')) for name in picture_names
    # ]
    print('Here is whats in the directory', os.listdir('static/images/testData/'))
    list_inputfile = os.listdir('static/images/testData/')
    file_input = [str(filename) for filename in list_inputfile if filename !='.DS_Store']
    
    print("These are the input files >>>>>", file_input)
   
    # Iterate feature extraction & prediction from filenames(locations)
    initial_images =[]
    classify_result=[]
    global graph
    graph = tf.get_default_graph()

    for pic_file_loc in file_input:
        # process images
        if pic_file_loc =='.DS_Store':
            os.remove(pic_file_loc)
        else:
            fpath = os.path.join('static', 'images', 'testData', pic_file_loc)
            image = preprocessing.image.load_img(fpath, target_size=(224,224))
            image = preprocessing.image.img_to_array(image) / 255
            image = np.expand_dims(image, axis=0)
            # features extracted by extractor-object (called above) 
            features = extractor.predict(image)
            # make prediction on features
            class_predicted = predictor.predict_classes(features)
            # specify labels based on dictionary (called above)
            inID = class_predicted[0]
            label = inv_map[inID]
            classify_result.append(label)
        
        # collect initial images to display later
        initial_images.append(f'static/images/testData/{pic_file_loc}')
    classify_result = list(set(classify_result))
    predicted_img = classify_result
    print('Classify>>>>>>>>>>',classify_result)
    # Return dataframes with intersections
    d3, d2, d1, _ = intersect(df, classify_result)
    
    common_ingredients = ['3-Ingredient Recipes',
                            '2-Ingredient Recipes',
                             '1-Ingredient Recipes']

    out3_Main, links3_Main, imgpath3_Main = outputRecipes_Main(d3)
    out2_Main, links2_Main, imgpath2_Main = outputRecipes_Main(d2)
    out1_Main, links1_Main, imgpath1_Main = outputRecipes_Main(d1)

    title_list_Main = [out3_Main.title.values.tolist()[:3], out2_Main.title.values.tolist()[:3],
                    out1_Main.title.values.tolist()[:3]]
    link_list_Main = [links3_Main[:3], links2_Main[:3],links1_Main[:3]]
    image_list_Main = [imgpath3_Main[:3],imgpath2_Main[:3],imgpath1_Main[:3]]

    recs_Main = [{'name': cond, 'titles':title_list_Main[ind], 'links': link_list_Main[ind], 
             'images': image_list_Main[ind]} 
                for ind, cond in enumerate(common_ingredients) if 'titles' ]

    out3_Side, links3_Side, imgpath3_Side = outputRecipes_Side(d3)
    out2_Side, links2_Side, imgpath2_Side = outputRecipes_Side(d2)
    out1_Side, links1_Side, imgpath1_Side = outputRecipes_Side(d1)

    title_list_Side = [out3_Side.title.values.tolist()[:3], out2_Side.title.values.tolist()[:3],
                    out1_Side.title.values.tolist()[:3]]
    link_list_Side = [links3_Side[:3], links2_Side[:3],links1_Side[:3]]
    image_list_Side = [imgpath3_Side[:3],imgpath2_Side[:3],imgpath1_Side[:3]]

    recs_Side = [{'name': cond, 'titles':title_list_Side[ind], 'links': link_list_Side[ind], 
             'images': image_list_Side[ind]} 
                for ind, cond in enumerate(common_ingredients) if 'titles' ]

    out3_Condiments, links3_Condiments, imgpath3_Condiments = outputRecipes_Condiments(d3)
    out2_Condiments, links2_Condiments, imgpath2_Condiments = outputRecipes_Condiments(d2)
    out1_Condiments, links1_Condiments, imgpath1_Condiments = outputRecipes_Condiments(d1)

    title_list_Condiments = [out3_Condiments.title.values.tolist()[:3], out2_Condiments.title.values.tolist()[:3],
                    out1_Condiments.title.values.tolist()[:3]]
    link_list_Condiments = [links3_Condiments[:3], links2_Condiments[:3],links1_Condiments[:3]]
    image_list_Condiments = [imgpath3_Condiments[:3],imgpath2_Condiments[:3],imgpath1_Condiments[:3]]

    recs_Condiments = [{'name': cond, 'titles':title_list_Condiments[ind], 'links': link_list_Condiments[ind], 
            'images': image_list_Condiments[ind]} 
            for ind, cond in enumerate(common_ingredients) if 'titles' ]

    out3_Dessert, links3_Dessert, imgpath3_Dessert = outputRecipes_Dessert(d3)
    out2_Dessert, links2_Dessert, imgpath2_Dessert = outputRecipes_Dessert(d2)
    out1_Dessert, links1_Dessert, imgpath1_Dessert = outputRecipes_Dessert(d1)

    title_list_Dessert = [out3_Dessert.title.values.tolist()[:3], out2_Dessert.title.values.tolist()[:3],
                    out1_Dessert.title.values.tolist()[:3]]
    link_list_Dessert = [links3_Dessert[:3], links2_Dessert[:3],links1_Dessert[:3]]
    image_list_Dessert = [imgpath3_Dessert[:3],imgpath2_Dessert[:3],imgpath1_Dessert[:3]]

    recs_Dessert = [{'name': cond, 'titles':title_list_Dessert[ind], 'links': link_list_Dessert[ind], 
            'images': image_list_Dessert[ind]} 
            for ind, cond in enumerate(common_ingredients) if 'titles' ]

    out3_Salad, links3_Salad, imgpath3_Salad = outputRecipes_Salad(d3)
    out2_Salad, links2_Salad, imgpath2_Salad = outputRecipes_Salad(d2)
    out1_Salad, links1_Salad, imgpath1_Salad = outputRecipes_Salad(d1)

    title_list_Salad = [out3_Salad.title.values.tolist()[:3], out2_Salad.title.values.tolist()[:3],
                    out1_Salad.title.values.tolist()[:3]]
    link_list_Salad = [links3_Salad[:3], links2_Salad[:3],links1_Salad[:3]]
    image_list_Salad = [imgpath3_Salad[:3],imgpath2_Salad[:3],imgpath1_Salad[:3]]
    
    recs_Salad = [{'name': cond, 'titles':title_list_Salad[ind], 'links': link_list_Salad[ind], 
             'images': image_list_Salad[ind]} 
                for ind, cond in enumerate(common_ingredients) if 'titles' ]


    return (file_input, initial_images, predicted_img, recs_Main, recs_Side, recs_Condiments, recs_Dessert, recs_Salad)

# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal.
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
if __name__ == '__main__':
    from pprint import pprint
    import os
    print("Checking what files exist")
    list_dir_files = os.lisdir('static/images/testData')
    features = {p: f'static/images/testData/{p}' for p in list_dir_files}
    print('Images are of:')
    pprint(features)

    file_input, preds, recoms_dict = get_recipes(features)
    print(f'Input values: {file_input}')
    print('Output Image Classification')
    pprint(preds)
