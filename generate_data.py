import random

def generate_synthetic_dataset(num_transactions, max_items_per_transaction, num_unique_items):
    """
    Generates a synthetic transactional dataset.
    Parameters:
        num_transactions (int): Number of transactions
        max_items_per_transaction (int): Maximum number of items in a transaction
        num_unique_items (int): Total unique items in the dataset
    Returns:
        list of list: Synthetic transactional dataset
    """
    dataset = [
        random.sample(range(1, num_unique_items + 1), random.randint(1, max_items_per_transaction))
        for _ in range(num_transactions)
    ]
    return dataset

def save_dataset(dataset, filepath):
    """
    Saves the dataset to a file in transactional format.
    Parameters:
        dataset (list of list): The transactional dataset
        filepath (str): Path to save the dataset
    """
    with open(filepath, 'w') as f:
        for transaction in dataset:
            f.write(','.join(map(str, transaction)) + '\n')

# Example usage
if __name__ == "__main__":
    synthetic_data = generate_synthetic_dataset(100, 5, 10)
    save_dataset(synthetic_data, 'data/synthetic_dataset.csv')
    print("Synthetic dataset saved to data/synthetic_dataset.csv")
