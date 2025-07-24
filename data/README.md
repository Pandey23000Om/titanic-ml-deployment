# Data Folder Structure

- **raw/**: Original, immutable data.
- **processed/**: Cleaned and processed data for modeling.
- **interim/**: Intermediate data files.
- **external/**: Data from third-party sources.

## Usage

- Place original data files in the `raw/` folder.
- Store cleaned and feature-engineered data in `processed/`.
- Use `interim/` for temporary or intermediate files.
- Add any third-party datasets to `external/`.

## Data Dictionary

| Variable   | Definition                        | Key                                            |
|------------|-----------------------------------|------------------------------------------------|
| survival   | Survival                          | 0 = No, 1 = Yes                                |
| pclass     | Ticket class                      | 1 = 1st, 2 = 2nd, 3 = 3rd                      |
| sex        | Sex of the person                 |                                                |
| age        | Age in years                      |                                                |
| sibsp      | No. of siblings/spouses aboard    |                                                |
| parch      | No. of parents/children aboard    |                                                |
| ticket     | Ticket number                     |                                                |
| fare       | Passenger fare                    |                                                |
| cabin      | Cabin number                      |                                                |
| embarked   | Port of Embarkation               | C = Cherbourg, Q = Queenstown, S = Southampton |
