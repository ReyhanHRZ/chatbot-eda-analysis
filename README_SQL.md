## 🗃 SQL-Based Analysis

To perform structured group-wise analysis, the cleaned dataset was written into a local SQLite database. Using SQL queries embedded in a Jupyter Notebook, we explored how key psychological and demographic factors relate to chatbot usage and perception.

All queries were executed using Python's built-in `sqlite3` module in the notebook [`sql/02_sql_analiz.ipynb`](sql/02_sql_analiz.ipynb).

### ✅ Objectives of the SQL Analysis

- Investigate whether **gender** impacts **AI acceptance**.
- Analyze the relationship between **education level** and **perceived trust** in AI-driven chatbots.
- Compare **user attitude** toward chatbots across different levels of **AI acceptance**.

### 🧠 SQL Queries Performed

1. **Average AI Acceptance by Gender**  
   Compared `YZORT` (AI acceptance score) between male and female participants.

2. **Trust in AI by Education Level**  
   Grouped by `EğitimDurumu`, calculated the average trust score (`GUVORT`) and ranked groups.

3. **Attitude by AI Acceptance Segments**  
   Created categorical segments:  
   `'High Acceptance'` (YZORT > 4) vs `'Low-Mid Acceptance'`,  
   then calculated average chatbot attitude (`TUTORT`) for each.

4. **Visual Output**  
   A bar chart was created to visualize how user attitude toward chatbots changes depending on their AI acceptance level.  
   This graphic was saved to `outputs/gorseller/attitude_by_acceptance.png`.

### 📊 Key Findings from SQL Queries

- **Female participants** demonstrated slightly **higher AI acceptance** on average.
- **Higher education levels** corresponded with **greater trust** in chatbot systems.
- Users with **high AI acceptance** also reported **more positive attitudes** toward chatbots.

These SQL insights complement the EDA and visualization results and provide a more structured perspective on user perception and acceptance of AI in the banking context.
