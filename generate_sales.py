import pandas as pd
import datetime
import random


def generate_sample_data():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Create sample data
    data = {
        'Date': [current_date] * 5,
        'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
        'Sales': [random.randint(100, 1000) for _ in range(5)],
        'Revenue': [random.randint(1000, 5000) for _ in range(5)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Generate filename with current date
    filename = f"sales_data_{datetime.datetime.now().strftime('%m-%d-%y')}.csv"

    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Generated file: {filename}")


if __name__ == "__main__":
    generate_sample_data()