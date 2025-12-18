## MeetingBank Data Engineering Project 

## Overview

This project implements an **end-to-end data engineering pipeline** using the **MeetingBank dataset**. It demonstrates data ingestion, cleaning, feature engineering, hybrid storage (PostgreSQL + MongoDB), and **query optimization with benchmarking**.

---

## Project Structure

```text
MeetingBank_Project/
├── Data                           # Dataset
├── README.md
├── .gitignore
│
├── step1_read_meetingbank.py      # Load & filter MeetingBank dataset
├── step2_filter_meetingbank.py      # Clean and normalize raw data
├── step3_build_transcripts.py     # Feature engineering (word & speaker counts)
│
├── step4_load_mongodb.py          # Store full transcripts in MongoDB
├── step4_load_postgres.py         # Load structured data into PostgreSQL
├── step4_schema.sql               # 3NF + Star schema definition
│
├── step5_queries.sql              # Analytical SQL queries
├── step5_benchmark.sql            # Query benchmarking (EXPLAIN ANALYZE)
│
├── step6_visualization.ipynb      # Data visualization (optional extension)
```

---

## Pipeline Summary

1. **Ingest** MeetingBank data (Boston & Seattle)
2. **Clean & normalize** semi-structured JSON
3. **Extract features** for analytics
4. **Store data** using a hybrid database design
5. **Optimize queries** using indexes, CTEs, and benchmarking

---

## Technologies Used

* **Python** – ETL & feature engineering
* **MongoDB** – Unstructured transcript storage
* **PostgreSQL** – Structured analytical storage
* **SQL** – Query optimization & benchmarking

---

## Group 3 Focus

* Index-based query optimization
* Performance comparison using `EXPLAIN ANALYZE`
* Analytical queries with CTEs and window functions

---

## Dataset

* **MeetingBank** (Hu et al., ACL 2023)
* Public city council meeting transcripts
* Subset: **Boston & Seattle**

---

## Status

✔ Meets all course project requirements
✔ Includes Group 3 specialization (benchmarking & optimization)
