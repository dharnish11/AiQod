import pandas as pd
from pymongo import MongoClient
from langchain.llms import Ollama
import json
import os

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["genai_assignment"]
collection = db["products"]

# Load CSV to MongoDB
def load_csv_to_mongo(csv_path):
    df = pd.read_csv(csv_path)
    collection.drop()  # Clean existing data
    collection.insert_many(df.to_dict(orient="records"))
    print("[INFO] CSV data loaded into MongoDB.")

# Initialize Ollama Mistral LLM
llm = Ollama(model="mistral")

# Generate MongoDB query using Mistral
def generate_query(user_input):
    prompt = f"""You are an expert in MongoDB queries. Generate a valid MongoDB query for the following question:
    Question: "{user_input}"
    Collection name is 'products'.
    Only return the query string using Python dictionary format.
    """
    response = llm(prompt)
    query = response.strip()
    log_query(user_input, query)
    return query

# Log query to file
def log_query(question, query):
    with open("Queries_generated.txt", "a") as f:
        f.write(f"Q: {question}\nQuery: {query}\n\n")

# Execute and return MongoDB query results
def execute_query(query):
    try:
        mongo_query = eval(query)
        results = list(collection.find(mongo_query))
        return pd.DataFrame(results)
    except Exception as e:
        print(f"[ERROR] Failed to execute query: {e}")
        return pd.DataFrame()

# Save or display results
def save_or_display(df, file_name=None):
    if df.empty:
        print("[INFO] No results found.")
    elif file_name:
        df.drop(columns=['_id'], inplace=True, errors='ignore')
        df.to_csv(file_name, index=False)
        print(f"[INFO] Results saved to {file_name}.")
    else:
        print(df)

# Process test case
def process_test_case(question, output_filename):
    query = generate_query(question)
    df = execute_query(query)
    save_or_display(df, output_filename)

# ---------- Main Execution ----------
if __name__ == "__main__":
    load_csv_to_mongo("sample_data.csv")

    # Test Case 1
    process_test_case(
        "Find all products with a rating below 4.5 that have more than 200 reviews and are offered by the brand 'Nike' or 'Sony'.",
        "test_case1.csv"
    )

    # Test Case 2
    process_test_case(
        "Which products in the Electronics category have a rating of 4.5 or higher and are in stock?",
        "test_case2.csv"
    )

    # Test Case 3
    process_test_case(
        "List products launched after January 1, 2022, in the Home & Kitchen or Sports categories with a discount of 10% or more, sorted by price in descending order.",
        "test_case3.csv"
    )
