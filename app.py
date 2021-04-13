import os
from flask import Flask, render_template, request, flash, redirect
# import jinja2
# from jinja2 import Template
from werkzeug.utils import secure_filename
from src.recipe_api import get_recipes, picture_names

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	

#---------- URLS AND WEB PAGES -------------#
# Directory of images to predict from
image_path_dir = 'static/images/testData/'

# Initialize the app
app = Flask(__name__)
app.secret_key = "secret key"
app.jinja_env.filters['zip'] =zip 
app.config['UPLOAD_FOLDER'] = image_path_dir
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Remove image files in image_path_dir
files = [f for f in os.listdir(image_path_dir) if os.path.isfile(f)]
for f in files:
    if f.endswith(('.jpg','.png', '.jpeg', '.gif')):
        os.remove(f)

#------- >>>>> Main Homepage <<<<<< --------#
@app.route("/")
def readImages():
    """
    Homepage: serve our visualization page, index.html
    """
    return render_template('index.html')

#------- >>>>> Submit Files <<<<< ---------#
@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		num_files = 0
		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				flash(f'{file.filename} submitted')
				num_files += 1
		flash(f'\n{num_files} File(s) successfully uploaded')
		return redirect('/')

#------- >>>>> Recommend Page <<<<< --------#
# Get an example and return it's score from the predictor model
@app.route("/recommend", methods=["POST", "GET"])
def predict():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template)" (key): "string in the textbox" (value)
    # cmd = "/usr/bin/automator P2R_workflow.workflow/"
    # os.system(cmd)
    
    file_input,initial_img, preds,recoms_dict_Main,recoms_dict_Side,recoms_dict_Dessert,recoms_dict_Condiments,recoms_dict_Salad = get_recipes(request.args)
    return render_template('recommender2.html',
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
