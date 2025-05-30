
# 📊 Atlas Labs HR Analytics Report (Power BI Portfolio)

A multi-page HR analytics dashboard built in Power BI for Atlas Labs, designed to track employee metrics, performance trends, attrition, and diversity insights.

---

## 🧱 Dataset Overview

Files used:
- **DimEducationLevel.csv**
- **DimEmployee.csv**
- **FactPerformanceRating.csv**
- **DimRatingLevel.csv**
- **DimSatisfiedLevel.csv**

Created:
- **Date Table** (`DimDate`)
- **Relationships**:
  - `DimDate[Date]` ↔ `FactPerformanceRating[ReviewDate]`
  - `DimDate[Date]` ↔ `DimEmployee[HireDate]` *(inactive)*
  - `DimEducationLevel[EducationLevelID]` ↔ `DimEmployee[EducationLevelID]`
  - `DimSatisfiedLevel[SatisfactionID]` ↔
    - `EnvironmentSatisfaction` *(active)*
    - `JobSatisfaction`, `RelationshipSatisfaction`, `WorkLifeBalance` *(inactive)*
  - `DimRatingLevel[RatingID]` ↔
    - `SelfRating` *(active)* and `ManagerRating` *(inactive)*


---

## 📍 Page 1: **Overview**

### 🔑 Key Insights:
- Atlas Labs has a total of **X employees**, with an attrition rate of **Y%**.
- Clear trends in hiring and employee separation are visible over time.
- Some departments show significantly higher active headcounts.
- Job roles are clustered heavily in a few departments, providing insight into resourcing patterns.



For high-level leadership tracking key employee metrics such as attrition.

### 🔧 Measures:
- **TotalEmployees**: `DISTINCTCOUNT(DimEmployee[EmployeeID])`
- **ActiveEmployees**: `CALCULATE([TotalEmployees], DimEmployee[Attrition] = "No")`
- **InactiveEmployees**: `CALCULATE([TotalEmployees], DimEmployee[Attrition] = "Yes")`
- **% Attrition Rate**: `DIVIDE([InactiveEmployees], [TotalEmployees])`

### 📊 Visuals:
- Card visuals for the 4 KPIs above
- **Stacked Column Chart**:
  - X-Axis: `DimDate[Date]` *(via USERELATIONSHIP)*
  - Values: `TotalEmployeesDate`
  - Legend: `Attrition`

- **Active Employees by Department** (Bar chart)
- **Active Employees by Department & Job Role** (Treemap)


---

## 📍 Page 2: **Demographics**

### 🔑 Key Insights:
- The organization has a fairly diverse age group, with employees ranging from early career to pre-retirement age.
- Gender distribution is relatively balanced, though slight variations exist by age group.
- Ethnicity data reveals areas for potential diversity improvement.
- Salaries vary significantly across ethnic groups — potential equity insight.



Focuses on diversity and inclusion.

### 👤 Visuals:
- **Card visuals**:
  - Youngest Employee
  - Oldest Employee

- **Age Bins**: created using Power Query → `AgeBins` column

- **Bar Chart**: Employees by `AgeBins` and `Gender`
- **Column & Line Combo Chart**: 
  - Columns: Employee count by `Ethnicity`
  - Line: **AverageSalary** (`AVERAGE(DimEmployee[Salary])`)


---

## 📍 Page 3: **Performance Tracker**

### 🔑 Key Insights:
- Employee performance trends are trackable year by year with key satisfaction metrics.
- Individual metrics allow for personalized coaching and HR follow-up.
- Self and manager ratings allow insight into performance alignment.
- Employees with no recent reviews are easily identifiable via the **NextReviewDate** measure.



Tracks employee review metrics.

### ✏️ Setup:
- Created `FullName` column in `DimEmployee` via concatenation
- Slicer: `FullName`
- Card: **Hire Date** (renamed to "Start Date")

### 🔧 Measures:
- **LastReviewDate**:
  ```DAX
  VAR last = MAX(FactPerformanceRating[ReviewDate])
  RETURN IF(ISBLANK(last), BLANK(), last)
  ```

- **NextReviewDate**:
  ```DAX
  VAR reviewOrHire =
    IF(
      ISBLANK(MAX(FactPerformanceRating[ReviewDate])),
      MAX(DimEmployee[HireDate]),
      MAX(FactPerformanceRating[ReviewDate])
    )
  RETURN reviewOrHire + 365
  ```

- **Line Graphs**: Individual yearly ratings for:
  - **JobSatisfaction**
  - **RelationshipSatisfaction**
  - **EnvironmentSatisfaction**
  - **SelfRating**
  - **ManagerRating**
  - **WorkLifeBalance**

> `USERELATIONSHIP()` is used for measures connected to inactive relationships.


---

## 📍 Page 4: **Attrition**

### 🔑 Key Insights:
- Certain departments, especially **Sales**, show higher attrition compared to others.
- Job roles with higher attrition can inform future recruitment and engagement strategies.
- Business travel and overtime are correlated with higher attrition rates.
- Employees with longer tenure show a different attrition pattern — useful for retention analysis.



Provides deeper insight into attrition causes and trends.

### 🔧 Measures:
- **InactiveEmployeesDate**: `CALCULATE([InactiveEmployees], USERELATIONSHIP(DimEmployee[HireDate], DimDate[Date]))`
- **TotalEmployeesDate**: `CALCULATE([TotalEmployees], USERELATIONSHIP(DimEmployee[HireDate], DimDate[Date]))`
- **% Attrition Rate Date**: `DIVIDE([InactiveEmployeesDate], [TotalEmployeesDate])`

### 📊 Visuals:
- Card: **Attrition Rate**
- Bar chart: Attrition rate by Department → Drilldown: Job Role
- **Line Chart**: `% Attrition Rate Date` by `DimDate[Date]` (date hierarchy enabled)

### Additional Visuals:
- **Attrition by Business Travel**
- **Attrition by Overtime**
- **Attrition by Tenure**

---

## ✨ Final Touches

- Header bar on each page with:
  - Company name
  - Current page title
- **Navigation bar** for switching between pages quickly

---

## 🖼️ Adding Screenshots

To add the screenshot(s) to this README on GitHub:

### 1. Place the image in your repository (e.g. in an `assets/` folder).
```bash
/assets/overview.png
```

### 2. Embed in Markdown:
```markdown
![Overview Page](assets/overview.png)
```

Repeat this for other images like demographics, performance tracker, etc.

---

## 📂 File Structure Suggestion
```
📁 HR-Analytics-Dashboard/
├── assets/
│   ├── overview.png
│   ├── demographics.png
│   ├── tracker.png
│   ├── attrition.png
├── PowerBI portfolio 1.pdf
├── README.md
```

---

## ✅ Tools Used
- Power BI
- DAX (CALCULATE, USERELATIONSHIP, FORMAT, etc.)
- Power Query
