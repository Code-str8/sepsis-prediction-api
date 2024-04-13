
<a name="readme-top"></a>

<div align="center">
  <h1><b>🩺Sepssis-Prediction-API</b></h1>
</div>



### 📘Table of Contents
1. [Setup](#setup)
2. [Running the App](#running-the-app)
3. [Usage](#usage)
4. [Models Used](#models-used)
5. [Deployment](#deployment)
6. [Further Development](#further-development)
7. [Contributing](#contributing)
8. [License](#license)


# 📲 sepssis predictor <a name="about-project"></a>

 The sepsis prediction project revolves around a machine learning model designed to accurately predict sepsis in intensive care unit (ICU) patients. The model has undergone rigorous training and evaluation to ensure its effectiveness in identifying patients at risk of sepsis.
 The sepsis prediction API allows seamless integration of the trained model into healthcare systems, providing professionals with valuable risk insights to improve patient care. The project includes a Dockerfile to streamline deployment and ensure all dependencies are properly installed, enabling easy setup in local or cloud environments.

### Data Fields

| Column   Name                | Attribute/Target | Description                                                                                                                                                                                                  |
|------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | N/A              | Unique number to represent patient ID                                                                                                                                                                        |
| PRG           | Attribute1       |  Plasma glucose|
| PL               | Attribute 2     |   Blood Work Result-1 (mu U/ml)                                                                                                                                                |
| PR              | Attribute 3      | Blood Pressure (mm Hg)|
| SK              | Attribute 4      | Blood Work Result-2 (mm)|
| TS             | Attribute 5      |     Blood Work Result-3 (mu U/ml)|         


### Setup🔧 <a name="setup"></a>
 
1. **Clone Repository**: Clone the repository containing the Streamlit app code.
2. **Install Dependencies**: Install the required dependencies using pip.
 
### 💻 Running the App <a name="running-the-app"></a>

### Prerequisites

In order to run this project you need:

- Uvicorn
- fastAPI
 
To run the app locally, execute the following command in the project directory:
 
```bash
   uvicorn api:app --reload 
```
 
The app will start running locally and can be accessed through a web browser and go to http://127.0.0.1:8000/docs to access the API documentation

### Pulling the Docker Image

To pull the Docker image for this project from Docker Hub, follow these steps:

1. Open your terminal or command prompt.

2. Make sure you have Docker installed on your system. If not, you can download and install it from the official Docker website: https://www.docker.com/get-started

3. Once Docker is installed, run the following command to pull the image:

```bash
docker pull codestr8/sepsis-prediction-api:v1.0
```
 Docker will now pull the image from Docker Hub and download it to your local machine.

 
### Usage <a name="usage"></a>
### Tech Stack  
<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">FastAPI</a></li>
  </ul>
</details>

<details>
<summary>start</summary>
  <ul>
    <li><a href="">Uvicorn</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">Sklearn</a></li>
  </ul>
</details>


 
### Models Used <a name="models-used"></a>
 
#### Supported Models 🤖
1. Logistic Regression
2. Sector Vector Machine
 
#### Model Training
- Data Preprocessing
- Pipeline Creation
- Model Training
- Evaluation
 
#### Model Selection
- User Choice
- Performance Comparison
 
### 🎉Deployment <a name="deployment"></a>
 
- Docker: [Dockerhub](https://hub.docker.com/repositories/codestr8)
- Article: [Medium](https://medium.com/@Codestr8/sepsis-prediction-in-
patients-227446951756)

### Further Development <a name="further-development"></a>
 
- Model Tuning
- Model Expansion
- Model Monitoring

## 👥 Authors

🕵🏽‍♀️ **Alexander Ndunda**

- GitHub: [GitHub Profile](https://github.com/Code-str8)
- Medium: [Medium Handle](https://medium.com/@Codestr8)
- LinkedIn: [LinkedIn Profile](https://linkedin.com/in/alexandernyambongo)

 
### 💡Contributing <a name="contributing"></a>
 
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or create a pull request.
 
### 🔐 License <a name="license"></a>
 
This project is licensed under the [MIT](LICENSE). Feel free to use, modify, and distribute the code for personal and commercial purposes.




