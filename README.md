# Students' score prediction

- LinkedIn [Elvis Gideon](https://www.linkedin.com/in/elvis-gideon-4340911a9)

## Aim or Objective:
This project is aimed at understanding to what extent Students' Maths scores can be influenced by factors such as 
their Gender, Ethnicity, Parental level of education, type of lunch, test preparation, as well as, scores in other subjects.

### Information about the Dataset:
There are 8 independent variables:

- `gender` : Sex of a student (Male/Female)
- `race/ethnicity` : Ethnicity of a student (Group A,B,C,D,E)
- `parental level of education` : parents' final education (bachelor's degree,some college,master's degree,associate's degree,high school)
- `lunch` : What type of lunch the student had before test (standard or free/reduced)
- `test preparation course` : Whether the student completed any preparation course before the test.
- `reading score` : Reading score obtained by the student.
- `writing score` : Writing score obtained by the student.

Target variable:
- `math score`: Math score of a student.

Dataset Source Link :
[https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?resource=download](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?resource=download)

# Project Development Approach

1. **Data Ingestion :**
 - This is the foremost phase of the data pipeline in which a script is used to ingest the data, and gets it saved as a csv file.
 - Data gets splitted into train and test set, and saved separately.

2. **Data Transformation :**
 - Similar to the first, this phase is handled entirely by a module which utilizes a ColumnTransformer Pipeline.
- For Numeric variables, SimpleImputer is applied with strategy of median (because there are some outliers in the data that have to be replaced), after which standard scaling follows.
 - For Categorical variables, SimpleImputer is applied with most-frequent strategy, after which One-Hot encoding follows.
 - An instance of the ColumnTransformer is fitted to the independent variables, after which it's saved as a pickle file obj (used to transform inputted data to the right form).

3. **Model training and tuning:**
 - Inside a module, different estimators are trained and evaluated. The most performant turned out to be Linear regression.
 - Thereafter, the parameters of the chosen regressor are tweaked, so as to boost model's accuracy .
 - The model is finally saved as a pickle file, to be used for the predict pipeline.

4. **Prediction Pipeline :**
 - This is responsible for ingesting user-inputted data (during which it's converted into a dataframe).
 - Predefined functions are imported and used to load both pickle files - one of which preprocesses the inputted data, and the other predicts Student's maths score (based on the inputted data)

5. **Flask app creation :**
 - A Flask app is created inside a python file(script). 
 - Upon running the script, a development server is started, serving the Flask app. 
 - The server accepts user-inputted data as a POST request and returns the predicted maths score as the response, while being rendered on the web client as a HTML-based UI.

## Exploratory Data Analysis Notebook
Link : [EDA Notebook](https://github.com/Xelvise/End-to-End-Students-score-prediction/blob/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20.ipynb)

## Getting Started

To get a local copy up and running, follow these simple Installation steps:

### Installation from GitHub:

Follow these steps to install and set up the project directly from the GitHub repo:

1. **Clone the Repository**
 - Open your terminal or command prompt.
 - Navigate to the directory where you want to install the project.
 - Run the following command to clone the GitHub repository:
     ```
     git clone https://github.com/Xelvise/End-to-End-Students-score-prediction.git
     ```

2. **Create a Virtual Environment** (Optional, but recommended)
 - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
 - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
 - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
 - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
 - Start the project by running the appropriate command.
     ```
     python app.py
     ```

6. **Access the Project**
 - To access and interact with the project, open a web browser on your local machine, using the following URL:
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Contributing:

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact
Elvis Gideon - [@elvisgideonuzuegbu@gmail.com](elvisgideonuzuegbu@gmail.com)
