
# Automated Data Query and Retrieval System

## Overview
This system allows querying a CSV dataset using natural language. It loads the CSV into MongoDB, uses a local LLM to generate MongoDB queries based on user inputs, retrieves results, and either displays or saves them.

## Setup Instructions
1. Install dependencies:
```bash
pip install pymongo langchain llama-index pandas ollama
```

2. Run MongoDB (locally or via Docker).

3. Load the CSV and use the interface to query the data.

## Files
- `code/load_csv_to_mongo.py`: Loads data from CSV to MongoDB.
- `code/query_interface.py`: Handles user interaction and uses LLM to generate queries.
- `output/test_case1.csv`, etc.: Result CSVs for test cases.
- `output/queries_generated.txt`: MongoDB queries generated by LLM.
