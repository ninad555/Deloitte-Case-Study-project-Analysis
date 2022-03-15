# <ins>Deloitte Case Study project Analysis  
## <ins>Ineuron internship project

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

  
#  📝  Problem Statement.
- This project lies under the banking domain. A banking domain consists of all the components needed to run a financial 
  service end-to-end. It covers the transaction and distribution process; the ways in which customers interact with the 
  system, products, and services the organisation offers.
- In this project the analysis of CPI , Exchange Rate and Export Merchandise data of Deloitte Company is needed. 
  The analysis should be on a respective dashboard, which should be much user interactive so that users can manipulate the 
  graphs and perform EDA on graphs for fetching some information from it. The respective graphs must have sliders with 
  respect to countries and years for dynamic purposes. 

# 🔍 Project Perspective
- The main objective of this project is to show the CAGR analysis and YOY analysis in a graphical and a very interactive 
  way. So that users can fetch some information from it and can be used for further analysis and other work. 


# 📽️ Demo
  
<ins>Short videos of our project

https://user-images.githubusercontent.com/65813824/156899096-3a211789-2929-40f6-80b6-18a3cd2f4757.mp4

  
# 🤔 Problem Faced & Solutions 💡 

✅ As each Data set had unique characteristics while pre processing we handled it by Modularising the code to make it effective 

✅ Making Plotly graph interactive responsive  and integrating it with web app for which we used Javascript  packages.

✅ Integration of database to make the app dynamics. Implemented MongoDB atlas so that the data can be easily accessible.

✅ Deploying and scaling the  application on cloud  executed on heroku.  

# 🔧 Project architecture
  ![image](https://user-images.githubusercontent.com/76054740/155142968-386faef5-2ce8-4c6c-802b-c8d0bf8ec732.png)

##  

  
# 💻 Technology stack
  Analytical & Visualization tools and libraries such as Numpy, Pandas, Plotly and Excel. For interactive UI JavaScript and IDE’s such as Pycharm, VScode and Github are used to build the whole framework.
 <div align = "center">
  
[![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://github.com/7Vivek/User-Response-Prediction-System/tree/main/Python%20Code)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://github.com/7Vivek/User-Response-Prediction-System/tree/main/Model)
[![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)](https://github.com/7Vivek/User-Response-Prediction-System/tree/main/EDA)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://github.com/7Vivek/User-Response-Prediction-System/tree/main/EDA)
[![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://github.com/7Vivek/User-Response-Prediction-System/tree/main/EDA)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://github.com/7Vivek/User-Response-Prediction-System/blob/main/templates/index.html)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://github.com/7Vivek/User-Response-Prediction-System/blob/main/static/css/style.css)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://github.com/7Vivek/User-Response-Prediction-System/blob/main/templates/index.html)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://github.com/7Vivek/User-Response-Prediction-System/blob/main/app.py)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://user-response-prediction.herokuapp.com/)
 </div>
  
  
# 🔔 Optimizations

### 1)	<ins>Code Modularisation :

- Functions are important because they allow us to take large complicated programs and to divide them
 into smaller manageable pieces.

- Code was performed step by step through trial and error method for a number of times. At last when the code is
finalized it is modularized and organized based on what each piece of code does,then one can easily
find and reference the code 
- Class and Modules are made and inherited of each pipeline as where required.

### 2)	<ins>Making Project Dynamic (Introducing Database):
  
- We created a database on Mongo DB and pushed these provided excel sheets on it (total 6 sheets in .csv format).
There were total six sheets of three datasets each of yearly and monthly.

- Then the code is designed in such a way that when we access the respective data for analysis and visualisation on our dashboard.

- It pulls the necessary data from the database, convert it into excel format and further fed to the data pre-processing and analysis.
it pulls the necessary data from the database, convert it into excel format and further fed to the data pre-processing and analysis.



# 💼Documentation

- [LowLevelDocumentation.docx](https://github.com/ninad555/Deloitte-Case-Study-project-Analysis/files/8191344/LowLevelDocumentation.docx)

- [HighLevelDocumentation.docx](https://github.com/ninad555/Deloitte-Case-Study-project-Analysis/files/8191364/HighLevelDocumentation.docx)

- [ProjectDetailedReport.pptx](https://github.com/ninad555/Deloitte-Case-Study-project-Analysis/files/8191367/ProjectDetailedReport.pptx)
  
  
# 🧑‍🔧 Code Set up

  Here we have two branches for the project. 
  1) main branch - without database
  2) master branch - with database
  
  After downloading the code file and opening it any IDE you can do the steps as mentioned below.
  
#### To Create and Conda environment.
### Create conda Env 
```bash
conda create -n BI 
```

### Activate conda Env
```bash
conda activate BI
```

### Installing requirements.txt
```bash
pip install -r requirements.txt
```

### To run the app
###### Run the app.py file
```bash
python app.py
```

## 👥Authors

  [![](https://img.shields.io/badge/Ninad_Kadam-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ninad-kadam-4439081b0/)
  [![](https://img.shields.io/badge/Abhishek_Mestry-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhishek-mestry-833843175/)
  [![](https://img.shields.io/badge/Viresh_Dhuri-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/viresh-dhuri-96b50a216/)
  [![](https://img.shields.io/badge/Omkar_Sutar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/omkar-sutar-739982199/)

  [![](https://img.shields.io/badge/Ninad_kadam-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ninad555)
  [![](https://img.shields.io/badge/Abhishek_Mestry-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbhishekMestry)
  [![](https://img.shields.io/badge/Viresh_Dhuri-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Virey07)
  [![](https://img.shields.io/badge/Omkar_Sutar-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/omkarsutar9702)
  
