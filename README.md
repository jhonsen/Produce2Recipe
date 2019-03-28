# Produce2Recipe: a recipe-finder tool based on images of produce  
Project-5 at METIS data science bootcamp

**Focus**: Image  Classification (w/ CNN), Text Classification (w/ NLP), Data Engineering, and _Design-to-Product_ Pipeline

  

## Project Description

> **Problem Statement:** 
>
> - What dish can I cook tonight, using the ingredients I have in my refrigerator? 

  

### Project Description

I spend a lot time looking for recipes that would match the ingredients I have in my refrigerator.  Sometimes ~30 minutes is spent on google-searching and website-browsing, to get the one that's reasonable based on ingredients, prep time, nutritonal values, etc. I often feel that most cooking sites and mobile apps have too many functionalities to navigate through. So, I thought, *"Wouldn't it be nice to have a personalized recipe-finder that simply takes ingredient photos as the input ?"* I wanted to take a stab at this problem, i.e., building a recipe-finder that's personalized to my preferences. 

- [x] **Objectives:**
  - [x] Collect recipes (text data) by webscraping _Epicurious_. Scraped info includes recipe title, -ingredients, -instructions, nutritional values, and photos  
  - [x] Collect images using Google API, for training a CNN model    
  - [x] Build a neural network-based image classifier of produce
  - [x] Perform topic modeling analysis for recipe-tagging, i.e., grouping them into different dish categories  
  - [x] Build a Flask app and a script that runs on a cellphone



**Code, notebooks, and documents**

- [Project_Report.md](./docs/Project5_Report.md), [Project_Presentation.pptx](./docs/Project_5_Presentation.pptx), or [PDF](./docs/Project_5_Presentation.pdf) - project report on markdown and powerpoint (or pdf) formats 
- Step1_DataAcquisition.ipynb](./notebooks/) - collecting images using google-API and webscraping epicurious for recipes (_coming soon_)
- Step2_Cleaning.ipynb](./notebooks/) - preliminary cleaning of the dataset (_coming soon_)
- Step3_TopicModeling.ipynb](./notebooks/) - _topic modeling_ of recipe titles (_coming soon_) 
- Step4_ImageClassification.ipynb](./notebooks/) - image classification (*coming soon*)
- Step5_End-to-end-pipeline.ipynb(./notebooks/) - (*coming soon*)