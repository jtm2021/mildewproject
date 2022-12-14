## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.

* The dataset contains more than 4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.


## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.

* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* We suspect affected cherry leaves to have clear marks/signs, that are powdery looking patches, that can differentiate from a healthy leaf. An Image Montage, shows that typically an infected leaf has fungal infection across. It is evidenced by an opaqueness characteristic along the venules of the leaves.
    * A machine learning model was used in investigating it. The hypothesis classifies a sample as a healthy leaf or a leaf that is affected with powdery mildew. The algorithm achieves the recognition of pattern with training, validation and test ratio of 0.70, 0.10 and 0.20 respectively.


## Rationale to map the business requirements to the Data Visualizations and ML tasks

* **Business Requirement 1**: The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
    - We will display the "mean" and "standard deviation" images for healthy and infected leaves.
    - We will display the difference between an average leaf with powdery mildew and an average healthy cherry leaf.
    - We will display a image montage for either healthy or diseased leaves.

* **Business Requirement 2**: The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.
    - We want to predict if a given sample is diseased with powdery mildew or not. 
	- We want to build a binary classifier and generate reports.

## ML Business Case
* The idea of the business is to create a study to visually differentiate cherry leaves between healthy and diseased with powdery mildew to a degree of 97% accuracy. 
* The ideal outcome is to provide the business a reliable and high accuracy in predicting healthy or diseased cherry crop by using sample leaves.
* The output is reflected in a dashboard using streamlit and the team working in the business can easily upload images of a sample cherry leaf. It reduces the manual processes around predicting powdery mildew in the plantation.
* Heuristics: The current diagnostic needs a well-experienced staff to perform a quality inspection to identify whether a sample cherry leaf is healthy or not. There is a possibility of human error in this part due because a new infection of powdery mildew in leaves cannot be detected by the human eye.


## Dashboard Design
Streamlit was used for the project dashboard. It has a responsive design with a menu located on the left part of the page. These are the following:

    1. Quick Project Summary
    2. Cherry Leaves Visualizer
    3. Mildew Detection
    4. Project Hypothesis
    5. ML Performance Metrics

![Dashboard Menu](/media/menu.PNG)

### QUICK PROJECT SUMMARY
The summary provides general information about powdery mildew in cherry leaves. It has information about the dataset used for the project. A link is also provided if the user wants to know more information about the project. The business requirements are stated on the same page.

![Summary](/media/summary.PNG)

### CHERRY LEAVES VISUALIZER
This section will answer the first business requirement. It has three checkboxes as seen on the following image that provide more information when ticked.

![Visualizer](/media/visualizer.PNG)
![Variability](/media/visualizer1.PNG)
![Average](/media/visualizer2.PNG)
![Image Montage Healthy](/media/visualizerhealthy.PNG)
![Image Montage Diseased](/media/visualizerdiseased.PNG)

### MILDEW DETECTION
This part evaluates an uploaded image whether it's healthy or affected by powdery mildew. A widget (file uploader) is displayed. With this, the user can upload an image or a batch of images. After succesfully uploading a file/files, a prediction follows, indicating whether it is healthy or infected by powdery mildew. A report is also shown in in a table with its name and prediction results. A user can also download the report by clicking on the download link.

![Mildew Detection](/media/detection.PNG)
![Mildew Detection Result - Healthy](/media/detectionresult.PNG)
![Mildew Detection Result - Diseased](/media/detectionresult2.PNG)

### PROJECT HYPOTHESIS
The information in the box shows the project hypothesis.

![Hypothesis](/media/hypothesis.PNG)

### ML PERFORMANCE METRICS
This section shows the label frequencies for train, validation and test sets. Also, the model history and performance on test set is displayed.

![ML Performance Metrics](/media/metrics.PNG)


## Deployment
- The project was initially deployed using [Heroku](https://www.heroku.com). However, due to the discontuation of their free services, the project was re-deployed using [Render](https://www.render.com). Here are the steps below:
    1. Open a workspace in your repo and delete `Procfile` and `runtime.txt`. Add, commit and push your changes to Github.
    2. Navigate to Render.com to create a web service by clicking "New+".
    3. Click ???Web Service???.
    4. Search for relevant repo and click ???Connect???. and ensure the following settings match.
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1668850241/README/deployment_settings_ddqblf.png">
    5. Set the BUILD COMMAND to:
        `pip install -r requirements.txt && ./setup.sh`
    6. Set the BUILD COMMAND to:
        `streamlit run app.py`
    7. Ensure the Free plan $0/month is selected.
    8. Scroll down and click "Advanced"
    9. Click ???Add Environment Variable??? and input the following:
        <img src="https://res.cloudinary.com/dborxc531/image/upload/v1668853081/README/variables_sljcaz.png">
    10. Click ???Create Web Service???.
    11. Wait for deployment???
    12. Deployment completed!
    13. Open the deployed site via the link below:
            https://mildew-project.onrender.com

### (OLD) Heroku Deployment Process
    The project was deployed to Heroku using the following steps.

    1. Log in to Heroku and create an App
    2. At the Deploy tab, select GitHub as the deployment method.
    3. Select your repository name and click Search. Once it is found, click Connect.
    4. Select the branch you want to deploy, then click Deploy Branch.
    5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App   on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* pandas 
    - this libray was used to manipulate the data used for the project specifically on structuring data like the dataframe.
* numpy 
    - used to operate on objects and numbers
* seaborn
    - this library was used to make/style statistical graphics
* matplotlib 
    - this was used for plotting graphs
* tensorflow
    - this library was used for neural network operations in the project
* keras
    - used for model tuning
* streamlit
    - used for easy development and deployment of the project dashboard.


## Credits 

* The template provided by Code Institute was used in the creation of this whole project. It can be downloaded from [Code Institute Solutions](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves)

### Content 

- The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

- Some information used in the project were taken from these websites:

    * https://en.wikipedia.org/wiki/Powdery_mildew

    * http://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/#:~:text=Powdery%20mildew%20of%20sweet%20and,1

## Acknowledgements
* Big thanks to my Code Institute mentor Rohit and tutor Sean for providing guidance in making this project.
