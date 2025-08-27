# Titanic ML Deployment

## Project Structure

- organized data folder for raw, cleaned and processed data.
- notebooks for data preparation and EDA.
- requirements file for dependencies.
- api for end-to-end ML App backend code
- frontend - html and streamlit app to hit the api

## Getting Started

successfully tested with python 3.11.9

### 1. Create a Virtual Environment

```bash
python -m venv ml-venv
```
---
### 2. Activate the Virtual Environment

- **Windows (Command Prompt):**

  ```bash
  ml-venv\Scripts\activate
  ```

- **Windows (Git Bash):**

  ```bash
  source ml-venv/Scripts/activate
  ```
---
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
---
### Note

- All data files should be placed in the appropriate `data/` subfolders.
- The virtual environment (`ml-venv/`) is excluded from version control via `.gitignore`.
- If you want to use Jupyter notebooks, install `ipykernel` in VS-Code. It will probabily be automatically prompted.

---

### 4. Handelling Data, inside data/

- Downloaded raw data was placed in 'raw' directory
- 0-data-cleaning.ipynb cleans the data using various methods and places them inside their respective folders in 'cleaned' directory
- For the variety of datasets, we have separate notebook collections for EDA (Exploratory Data Analysis) and data-preparation.
- Data-prep notebooks place their respective processed data in 'processed' sub-folders.
- The predictive-analysis notebooks to all kinds of modelling and can save models in the 'model/' folder
---
### 5. Running the notebooks and saving a model
- run notebooks\0-data-cleaning.ipynb, it saves all the cleaned datasets.
- run data-preparation.ipynb present inside any of the notebook collection and run its predictive_analysis.ipynb file. At the end of 'notebooks\2-simple-impute-collection\predictive_analysis.ipynb' file, you can run this code-block to save the any-model of your choice to the 'model/' directory. You will need to create the model folder in the root of this repository. 
```python
import joblib
joblib.dump(<model-object/function-name>, "../../model/svm_model.pkl")
print("Model saved successfully!")
```
---
## Running the FastApi and working with Frontend on your local

### 1. Run the backend api
- activate the virtual environment
- run 
```bash
cd api
uvicorn ml_app:app --reload
```

### 2. Using HTML file as frontend to hit the API
- Open http://127.0.0.1:8000/ on your local web-browser.
- You can fill the form and hit predict to see the model output.

### 3. Using streamlit app to hit the API
- Keep the backend running on 1 teminal
- On a separate terminal, start the streamlit app
```bash
cd api
streamlit run streamlit_app.py
```
- You will get the url to open in your local web-browser and use the app