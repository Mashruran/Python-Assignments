# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Example 1: Writing to a Text File
with open('data/example.txt', 'w') as file:
    file.write("Hello, Python developers!\n")
    file.write("Welcome to file I/O operations.")

# Example 2: Reading from a Text File
with open('data/example.txt', 'r') as file:
    content = file.read() # readlines(), readlines()
    print(content)

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

import csv

# Example 3: Writing to a CSV File
with open('data/example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 28, "New York"])
    writer.writerow(["Bob", 22, "Los Angeles"])
    writer.writerow(["Carol", 24, "Chicago"])

# Example 4: Reading from a CSV File
with open('data/example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Section 3: JSON Data
# --------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.

import json

# Example 5: Writing JSON to a File
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('data/data.json', 'w') as file:
    json.dump(data, file)


# Example 6: Reading JSON from a File
with open('data/data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Example 7: Processing JSON Data from a File
# Suppose we have a JSON file containing multiple user records.
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"}
]
with open('data/users.json', 'w') as file:
    json.dump(users, file)

with open('data/users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        print(f"{user['name']} ({user['age']}): {user['email']}")

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import os

# Function to append new product data to the CSV file
def add_product_to_csv(csv_file, product_info):
    file_exists = os.path.isfile(csv_file)  # Check if the file exists
    try:
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ["ProductID", "Name", "Price", "Stock"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # If the file is new, write headers first
            if not file_exists:
                writer.writeheader()

            # Append the new product data
            writer.writerow(product_info)
            print(f"Product {product_info['Name']} added successfully to {csv_file}.")
    except Exception as e:
        print(f"Error while adding product: {e}")

# Function to convert CSV to JSON (reuse the previous code)
def csv_to_json(csv_file, json_file):
    try:
        # Read CSV file and convert to JSON
        data = []
        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        # Write to JSON file
        with open(json_file, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully converted {csv_file} to {json_file}")
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage to add a new product
csv_file_path = "products.csv"
json_file_path = "products.json"

# New product information to add
new_product = {
    "ProductID": "P004",
    "Name": "Tablet",
    "Price": "299.99",
    "Stock": "25"
}

# Step 1: Add the product to the CSV file
add_product_to_csv(csv_file_path, new_product)

# Step 2: Update the JSON file to reflect the new data
csv_to_json(csv_file_path, json_file_path)

# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.
import datetime

# Function to write log messages to a file with timestamps
def write_log(message, log_file="app.log"):
    try:
        # Generate a timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"

        # Append the log message to the file
        with open(log_file, mode='a', encoding='utf-8') as file:
            file.write(log_message)
        print("Log message written successfully.")
    
    except Exception as e:
        print(f"An unexpected error occurred while writing to the log file: {e}")

# Example usage
write_log("Application started.")
write_log("An error occurred: Unable to connect to the database.")
write_log("Application closed.")

# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
