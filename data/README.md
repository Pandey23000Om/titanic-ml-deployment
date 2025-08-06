# Data Folder Structure

- **raw/**: Original, immutable data.
- **cleaned/**: Cleaned data for processing/EDA.
- **processed/**: processed data for modeling.

## Usage

- Place original data files in the `raw/` folder.
- Store cleaned data in `cleaned/` for EDA
- Put feature-engineered data in `processed/`.

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
