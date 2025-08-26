## 🚀 Tools We’ll Use in API Phase

### 1. **FastAPI**

* **What it is**: A modern Python web framework to build APIs quickly.
* **Why we use it**:

  * Super fast (built on ASGI, not old WSGI).
  * Auto-generates **Swagger docs** (`/docs`).
  * Plays nicely with ML models → just wrap `.predict()` inside an endpoint.

* **Install**:

  ```bash
  pip install fastapi
  ```

---

### 2. **Pydantic**

* **What it is**: A data validation library.
* **Why we use it**:

  * When a user sends JSON to the API, we need to check if the format & datatypes are correct.
  * Example: If `Age` should be a float but user sends `"twenty"`, Pydantic will reject it gracefully.
* **Install**: (already installed with your step)

  ```bash
  pip install pydantic
  ```

---

### 3. **Uvicorn**

* **What it is**: A server that runs FastAPI (ASGI server).
* **Why we use it**:

  * FastAPI is just the “framework”; to serve it we need a server.
  * Think of Uvicorn like a lightweight web server for running APIs.
* **Install**:

  ```bash
  pip install uvicorn
  ```

Run API with:

```bash
uvicorn app:app --reload
```

* `app:app` → first `app` is the filename (`app.py`), second `app` is the FastAPI object.
* `--reload` → auto restart when you change code.

---

### 4. **Joblib**

* **What it is**: A library to save & load ML models (`.pkl` files).
* **Why we use it**:

  * Saves your trained model once → reuse it in API.
  * Without this, you’d have to retrain every time you restart the API.

Install:

```bash
pip install joblib
```

---

### 5. **Requests**

* **Why**: If you want to test API calls from Python instead of Swagger.

  ```bash
  pip install requests
  ```

---

### 5. **Streamlit**

* **What**: is a Python framework for building interactive web apps—specifically designed for data science, machine learning, and analytics projects.

* **Why**: you can instantly build a web form where users input data → click a button → get predictions. Explore datasets, filter, sort, visualize—without html, css, or js.

* **Benefit**: Run locally or deploy online with Streamlit Cloud, Hugging Face Spaces, or Heroku.