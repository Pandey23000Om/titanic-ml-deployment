# Titanic ML Deployment

## Project Structure

- Organized data folder for raw, cleaned and processed data.
- Notebooks for data preparation and EDA.
- Requirements file for dependencies.

## Getting Started

### 1. Create a Virtual Environment

```bash
python -m venv ml-venv
```

### 2. Activate the Virtual Environment

- **Windows (Command Prompt):**

  ```bash
  ml-venv\Scripts\activate
  ```

- **Windows (Git Bash):**

  ```bash
  source ml-venv/Scripts/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Notes

- All data files should be placed in the appropriate `data/` subfolders.
- The virtual environment (`ml-venv/`) is excluded from version control via `.gitignore`.
- If you want to use Jupyter notebooks, `ipykernel` is included in the requirements so you can select this environment as a kernel.

---
