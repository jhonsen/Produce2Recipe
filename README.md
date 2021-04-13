# Produce2Recipe: a recipe-finder tool based on images of produce  
Project-5 at METIS data science bootcamp

**Focus**: Image  Classification (w/ CNN), Text Classification (w/ NLP), Data Engineering, and _Design-to-Product_ Pipeline

  

## Project Description

> **Problem Statement:** 
>
> - What dish can I cook tonight, using the ingredients I have in my refrigerator? 

  

### Project Description

I spend a lot time looking for recipes that would match the ingredients I have in my refrigerator.  Sometimes ~30 minutes is spent on google-searching and website-browsing, to get the one that's reasonable based on ingredients, prep time, nutritonal values, etc. I often feel that most cooking sites and mobile apps have too many functionalities to navigate through. So, I thought, *"Wouldn't it be nice to have a personalized recipe-finder that simply takes ingredient photos as the input ?"* I wanted to take a stab at this problem, i.e., building a recipe-finder that's personalized to my preferences. 

_Checkout the blog post [here](https://jhonsen.github.io/2019/04/22/Produce2Recipe/)_ 

- [x] **Objectives:**
  - [x] Collect recipes (text data) by webscraping _Epicurious_. Scraped info includes recipe title, -ingredients, -instructions, nutritional values, and photos  
  - [x] Collect images using Google API, for training a CNN model    
  - [x] Build a neural network-based image classifier of produce
  - [x] Perform topic modeling analysis for recipe-tagging, i.e., grouping them into different dish categories  
  - [x] Build a Flask app and a script that runs on a cellphone

![vidgif](./docs/images/P2R_action.gif)
  
_Publicly accessible app coming soon!_

**Code, notebooks, and documents**

- [Project_Report.md](./docs/Project5_Report.md), [Project_Presentation.pptx](./docs/Project_5_Presentation.pptx), or [PDF](./docs/Project_5_Presentation.pdf) - project report on markdown and powerpoint (or pdf) formats 
- [Step1_DataAcquisition.ipynb](./notebooks/Step1_DataAcquisition.ipynb) - collecting images and webscraping epicurious for recipes
- [Step2_Cleaning.ipynb](./notebooks/Step2_Cleaning.ipynb) - preliminary cleaning of the dataset 
- [Step3_TopicModeling.ipynb](./notebooks/Step3_TopicModeling.ipynb) - _topic modeling_ of recipe titles 
- [Step4_ImageClassification.ipynb](./notebooks/Step4_ImageClassification.ipynb) - image classification
- [Step5_End-to-end-pipeline.ipynb](./notebooks/Step5_End-to-end-pipeline.ipynb) - example script of how images are fed into the model > output as text > key-search of tagged recipes
- Other notebooks are labeled with a prefix: [Extra_](./notebooks/)  

**Instructions to run web_app prototype**
1. Download 2 files from [this gdrive](https://drive.google.com/drive/folders/1kz-_Euwk2G4AZf4htolcbwZhWg1wjtQl?usp=sharing) and place them in `./models/` folder
2. On terminal, run $>`python app.py`
3. Copy the URL shown (e.g., http://127.0.0.1:5000/) into a browser
4. Choose 1-3 images of produce from local machine
5. Click Submit
6. Click  *Find list of Recipes** link
