# Observations from EDA-1 (Dropna Cleaned Data)

- **Embarkation:**  
  - The majority of passengers boarded from port S (Southampton).
  - However, a higher proportion of survivors boarded from port C (Cherbourg), indicating embarkation point may influence survival odds.

- **Passenger Class:**  
  - Most passengers were in 3rd class.
  - Survival rates were highest in 1st class and lowest in 3rd class.

- **Gender:**  
  - More males than females were on board.
  - Females had a much higher survival rate than males.

- **Age:**  
  - Most passengers were young adults (20s–30s).
  - Children had a higher chance of survival compared to adults and seniors.

- **Fare:**  
  - Most fares were low, but survivors tended to have paid higher fares.
  - Fare distribution is right-skewed; log transformation helps normalize it.

- **Family Size:**  
  - Most people traveled alone or with one family member.
  - Solo travelers had lower survival rates compared to those with small families.

- **Parch/SibSp:**  
  - Most passengers had no parents/children or siblings/spouses aboard.
  - Having a small number of family members on board slightly increased survival odds.

- **Overall Survival:**  
  - About 40% of passengers survived.
  - Survival was strongly associated with being female, being in 1st class, and embarking from Cherbourg.

---

*These insights can guide feature selection and engineering