📊 RFM Analytics Dashboard

An end-to-end RFM (Recency, Frequency, Monetary) Analytics Dashboard that transforms raw retail transaction data into actionable customer segments.

This project analyzes customer purchase behavior using the RFM framework:

1)Recency – How recently a customer made a purchase

2)Frequency – How often a customer purchases

3)Monetary – How much a customer spends

The computed RFM metrics are scored, segmented, stored in a MySQL database, exposed via REST APIs, and validated using SQL queries and unit tests

Tech Stack

Python (Pandas, SQLAlchemy)

MySQL 8.0

Flask (REST APIs)

Pytest (unit testing)


How to Run
1)Set environment variables in .env

2)Run data cleaning & RFM scripts

3)Store results:

python backend/scripts/rfm_to_mysql.py

4)Start API server:

python backend/scripts/app.py

5)Run tests:

pytest
