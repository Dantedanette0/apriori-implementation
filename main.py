import os
from generate_data import generate_synthetic_dataset, save_dataset
from apriori import apriori, generate_association_rules

if __name__ == "__main__":
    # Generate synthetic data
    num_transactions = 100
    max_items_per_transaction = 5
    num_unique_items = 10
    min_support = 2
    min_confidence = 0.6

    dataset = generate_synthetic_dataset(num_transactions, max_items_per_transaction, num_unique_items)
    save_dataset(dataset, 'results/synthetic_dataset.csv')

    print("Synthetic dataset generated and saved to results/synthetic_dataset.csv")

    # Run Apriori Algorithm
    frequent_sets = apriori(dataset, min_support)
    print("Frequent Itemsets:")
    print(frequent_sets)

    # Save frequent itemsets
    with open('results/frequent_itemsets.txt', 'w') as f:
        for itemset in frequent_sets:
            f.write(f"{itemset}\n")

    # Generate association rules
    association_rules = generate_association_rules(dataset, frequent_sets, min_confidence)
    print("\nAssociation Rules:")
    print(association_rules)

    # Save association rules
    with open('results/association_rules.txt', 'w') as f:
        for rule in association_rules:
            f.write(f"{rule}\n")
