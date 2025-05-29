# Gen-AI Assignment: Automated Data Query & Retrieval System

## Overview

This project demonstrates an automated data query and retrieval system using:
- MongoDB
- CSV input/output
- Offline LLM (Ollama's Mistral)
- LangChain

## Setup Instructions

1. Install the required packages:
   ```
   pip install pymongo pandas ollama langchain
   ```

2. Start your local MongoDB server.

3. Ensure Ollama is running and has `mistral` model available:
   ```
   ollama run mistral
   ```

4. Place your `sample_data.csv` in the same directory.

5. Run the script:
   ```
   python main.py
   ```

## Output

- Generated queries are saved in `Queries_generated.txt`.
- Output CSVs for test cases are: `test_case1.csv`, `test_case2.csv`, `test_case3.csv`.

## Author

Generated via OpenAI ChatGPT.
