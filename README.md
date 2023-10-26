# Binary Prediction of Smoker Status

## Problem Description

The goal of this project is to create a machine learning model to predict a patient's smoking status using various bio-signals. This is part of a [Kaggle Playground Series Competition](https://www.kaggle.com/competitions/playground-series-s3e24).

Smoking's well-established adverse effects on health are unquestionable, making it a leading cause of preventable global morbidity and mortality by 2018. A World Health Organization report forecasts that smoking-related deaths will reach 10 million by 2030. Although evidence-based smoking cessation strategies have been advocated, their success remains limited, with traditional counseling often considered ineffective and time-consuming. To address this, various factors have been proposed to predict an individual's likelihood of quitting, but their application yields inconsistent results. A solution lies in developing predictive models using machine learning techniques, a promising approach in recent years for understanding an individual's chances of quitting smoking and improving public health outcomes.

## Data

I will be combining 2 datasets for this project. Both datasets contain a train set and test set, where the target column is missing from the test set.

1. [Kaggle Competition Data](https://www.kaggle.com/competitions/playground-series-s3e24/data): This data was provided by Kaggle for the competition and was **synthetically generated** using a deep learning model. The deep learning model was trained using the data from the second dataset.
2. [Smoker Status Prediction using Bio-Signals](https://www.kaggle.com/datasets/gauravduttakiit/smoker-status-prediction-using-biosignals): This data was used to train the deep learning model which generated the data in the first dataset.

## Usage

### Environment Setup

- `conda env create -f environment.yaml`
- `conda activate smoker-prediction`
- `poetry install`

## Deliverables

- [ ] `README.md` with
  - [ ] Description of the problem
  - [ ] Instructions on how to run the project
- [x] Data
  - [x] You should either commit the dataset you used or have clear instructions how to download the dataset
- [ ] Notebook (suggested name - `notebook.ipynb`) with
  - [ ] Data preparation and data clearning
  - [ ] EDA (ranges of values, missing values, analysis of target variable, feature importance analysis, etc)
  - [ ] Model selection process and parameter tuning
- [ ] Script `train.py` (suggested name)
  - [ ] Training the final model
  - [ ] Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
- [ ] Script `predict.py` (suggested name)
  - [ ] Loading the model
  - [ ] Serving it via a web serice (with Flask or specialized sofware - BentoML, KServe, etc)
- [ ] Files with dependencies
  - [ ] `Pipenv` and `Pipenv.lock` if you use Pipenv
  - [ ] or equivalents: conda environment file, requirements.txt or pyproject.toml
- [ ] `Dockerfile` for running the service
- [ ] Deployment
  - [ ] URL to the service you deployed or
  - [ ] Video or image of how you interact with the deployed service

## Future Work

- [One Kaggle user pointed out](https://www.kaggle.com/competitions/playground-series-s3e24/discussion/450510) that the target values for the second test set can be found in another dataset on Kaggle: [Body signal of smoking](https://www.kaggle.com/datasets/kukuroo3/body-signal-of-smoking/data). This dataset cites its source as the [Korean Government](https://www.data.go.kr/data/15007122/fileData.do#/tab-layer-file). Since the competition dataset was synthetically generated, will using additional data sources improve accuracy on the competition test set?
