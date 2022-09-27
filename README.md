## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.

* The dataset contains more than thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



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
* The idea of the business is to create a study to visually differentiate cherry leaves between healthy and diseased with powdery mildew. 
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



### CHERRY LEAVES VISUALIZER
### MILDEW DETECTION
### PROJECT HYPOTHESIS
### ML PERFORMANCE METRICS


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.


## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

https://en.wikipedia.org/wiki/Powdery_mildew

http://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/#:~:text=Powdery%20mildew%20of%20sweet%20and,1).

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.
