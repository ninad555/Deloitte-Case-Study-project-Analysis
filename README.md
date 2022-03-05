
# <ins>Deloitte Case Study project Analysis  
## <ins>Ineuron internship project
Project Members: Ninad Kadam, Abhishek Mestry, Viresh Dhuri, Omkar Sutar. 

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

  
## 1. Problem Statement.
- This project lies under the banking domain. A banking domain consists of all the components needed to run a financial 
  service end-to-end. It covers the transaction and distribution process; the ways in which customers interact with the 
  system, products, and services the organisation offers.
- In this project the analysis of CPI , Exchange Rate and Export Merchandise data of Deloitte Company is needed. 
  The analysis should be on a respective dashboard, which should be much user interactive so that users can manipulate the 
  graphs and perform EDA on graphs for fetching some information from it. The respective graphs must have sliders with 
  respect to countries and years for dynamic purposes. 

## 2. Project Perspective
- The main objective of this project is to show the CAGR analysis and YOY analysis in a graphical and a very interactive 
  way. So that users can fetch some information from it and can be used for further analysis and other work. 


## 👨‍🏫Demo

<ins>Tuturial videos of our project

https://user-images.githubusercontent.com/76054740/154712115-ba37290b-1912-4edc-82e4-96e0501fb89b.mp4
    
## 🔤 Problem faced
  skdjf
  

## 🏺 Project architecture
  ![image](https://user-images.githubusercontent.com/76054740/155142968-386faef5-2ce8-4c6c-802b-c8d0bf8ec732.png)

  
  
## 💻Technology stack
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
  
  
  
## 💡Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?


## 🪛Optimizations

1)	<ins>Code Modularisation :
  
One of the most important concepts of programming is the ability to group some lines of code into a unit that can be included in our program. The original wording for this was a sub-program. Other names include: macro, sub-routine, procedure, module and function. We are going to use the term function for that is what they are called in most of the predominant programming languages of today. Functions are important because they allow us to take large complicated programs and to divide them into smaller manageable pieces. For performing all above steps and getting at this point, the code is was performed step by step through trial and error method for a number of times. At last when the code is finalized it is modularized in such a way that it is understandable for the users and IT technicians too. To organize the code in modularize way we organized each piece of code based on what it does, then one can easily find and reference the code based on his/her organization scheme.

2)	<ins>Making Project Dynamic (Introducing Database):
  
A database management system (DBMS) is a software tool that enables users to manage a database easily. It allows users to access and interact with the underlying data in the database. These actions can range from simply querying data to defining database schemas that fundamentally affect the database structure. Furthermore, DBMS allow users to interact with a database securely and concurrently without interfering with each user and while maintaining data integrity.
 Firstly, we were provided only the three excel workbooks of CPI (Consumer Price Index), Exports Merchandise, Exchange Rate. Those three excel workbooks were having two-three sheets naming yearly, monthly, quarterly. We created a database on Mongo DB and pushed these provided excel sheets on it (total 6 sheets in .csv format). There were total six sheets of three datasets each of yearly and monthly. Then the code is designed in such a way that when we access the respective data for analysis and visualisation on our dashboard, it pulls the necessary data from the database, convert it into excel format and further fed to the data pre-processing and analysis.



## 💼Documentation

[Documentation](https://linktodocumentation)


## 👥Authors

  [![](https://img.shields.io/badge/Ninad_Kadam-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ninad-kadam-4439081b0/)
  [![](https://img.shields.io/badge/Abhishek_Mestry-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhishek-mestry-833843175/)
  [![](https://img.shields.io/badge/Viresh_Dhuri-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/viresh-dhuri-96b50a216/)
  [![](https://img.shields.io/badge/Omkar_Sutar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/omkar-sutar-739982199/)

  [![](https://img.shields.io/badge/Ninad_kadam-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ninad555)
  [![](https://img.shields.io/badge/Abhishek_Mestry-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbhishekMestry)
  [![](https://img.shields.io/badge/Viresh_Dhuri-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Virey07)
  [![](https://img.shields.io/badge/Omkar_Sutar-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/omkarsutar9702)
  
