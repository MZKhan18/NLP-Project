# Quora Duplicate Question Detection

This project aims to detect duplicate question pairs using Natural Language Processing (NLP) techniques and machine learning algorithms. The project was developed for the Quora Duplicate Question Pairs competition on Kaggle.

## Project demo at https://qoura-duplicate-question-pairs.onrender.com

## Snapshot of project

![qdqp](https://github.com/MZKhan18/NLP-Project/assets/83308074/aacd8832-9347-4a8b-ac6a-a11c77778c7b)

## Introduction

The Quora Duplicate Question Detection project utilizes NLP techniques and machine learning algorithms to identify duplicate question pairs in the Quora dataset. The goal is to provide an accurate prediction of whether two questions are duplicates or not.

## Dataset

The project uses the Quora Question Pairs dataset, which consists of over 30,000 question pairs. Each pair is labeled as either duplicate or non-duplicate. The dataset serves as the training and testing data for the machine learning model.

## Methodology

The project follows these main steps:

1. **Data Preprocessing:** The dataset is cleaned and preprocessed to remove any noise and inconsistencies. This includes removing stop words, punctuation, and performing other text cleaning operations.

2. **Feature Engineering:** The text data is transformed into numerical features to be used by the machine learning algorithm. Bag-of-words representation is applied, and additional features are created using various NLTK libraries.

3. **Model Building:** The Random Forest algorithm is chosen as the model for this project due to its effectiveness in handling text data and classification tasks. The model is trained on the preprocessed dataset and evaluated using appropriate metrics.

4. **Website Development:** A user-friendly website is created using Streamlit, a Python library for building interactive web applications. The website allows users to input question pairs and obtain predictions on whether they are duplicates or not.

5. **Deployment:** The website is deployed to a hosting platform, allowing users to access the duplicate question detection functionality easily.

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/quora-duplicate-question-detection.git`
2. Change into the project directory: `cd quora-duplicate-question-detection`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use the duplicate question detection website:

1. Ensure you have followed the installation steps.
2. Run the Streamlit application: `streamlit run app.py`
3. Access the website in your browser at `http://localhost:8501`.

The website provides an interface for users to enter two questions and receive a prediction of whether they are duplicates or not.

## Results

The model achieved an accuracy of 80% in detecting duplicate question pairs. This metric indicates the proportion of correct predictions made by the model.
