#Import and Load Data into SQLite

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("../data/yapayzeka_duzenli.csv")

# Create SQLite database and write data into it
conn = sqlite3.connect("../data/chatbot_analiz.db")
df.to_sql("chatbot_anketi", conn, if_exists="replace", index=False)

print("✅ Data successfully written to SQLite.")


#Gender vs. AI Acceptance (YZORT)

# Query: Does gender affect average AI acceptance (YZORT)?
query1 = """
SELECT 
    Cinsiyet AS Gender, 
    COUNT(*) AS Count, 
    ROUND(AVG(YZORT), 2) AS Avg_AI_Acceptance
FROM chatbot_anketi
GROUP BY Cinsiyet;
"""

gender_ai_acceptance = pd.read_sql_query(query1, conn)
gender_ai_acceptance


#Education vs. Trust in AI (GUVORT)

# Query: Which education groups show higher average trust in chatbots (GUVORT)?
query2 = """
SELECT 
    EğitimDurumu AS EducationLevel, 
    COUNT(*) AS Count, 
    ROUND(AVG(GUVORT), 2) AS Avg_Trust
FROM chatbot_anketi
GROUP BY EğitimDurumu
ORDER BY Avg_Trust DESC;
"""

education_trust = pd.read_sql_query(query2, conn)
education_trust



#Attitude by AI Acceptance Group

# Query: Do users with high AI acceptance (YZORT > 4) have more positive chatbot attitudes (TUTORT)?
query3 = """
SELECT 
    CASE 
        WHEN YZORT > 4 THEN 'High Acceptance'
        ELSE 'Low-Mid Acceptance'
    END AS AI_Acceptance_Level,
    COUNT(*) AS Count,
    ROUND(AVG(TUTORT), 2) AS Avg_Attitude
FROM chatbot_anketi
GROUP BY AI_Acceptance_Level;
"""

attitude_by_acceptance = pd.read_sql_query(query3, conn)
attitude_by_acceptance



