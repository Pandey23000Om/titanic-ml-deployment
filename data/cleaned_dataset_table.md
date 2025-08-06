# Summary of Cleaned Titanic Data Versions

| Version         | Rows | Columns | Remaining Nulls | Description                          |
|-----------------|------|---------|-----------------|--------------------------------------|
| Dropna          | 712  | 11      |  0              | Rows with nulls dropped, Cabin removed |
| Simple Impute   | 891  | 11      |  0              | Nulls filled with median/mean/mode, Cabin removed |
| Grouped Impute  | 891  | 12      |  0              | Nulls filled by grouped medians, Deck extracted, Cabin removed |
