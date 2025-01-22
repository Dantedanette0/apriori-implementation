from itertools import combinations

def count_single_items(dataset):
    counts = {}
    for transaction in dataset:
        for item in transaction:
            counts[item] = counts.get(item, 0) + 1
    return counts

def apriori(dataset, min_support):
    counts = count_single_items(dataset)
    candidates = [[item] for item, count in counts.items() if count >= min_support]

    frequent_sets = []
    k = 0
    while candidates:
        frequent_sets.extend(candidates)
        k += 1
        new_candidates = []
        for i in range(len(candidates)):
            for j in range(i + 1, len(candidates)):
                candidate = sorted(list(set(candidates[i]) | set(candidates[j])))
                if len(candidate) == k + 1 and candidate not in new_candidates:
                    support = sum([1 for transaction in dataset if set(candidate).issubset(set(transaction))])
                    if support >= min_support:
                        new_candidates.append(candidate)
        candidates = new_candidates
    return frequent_sets

def calculate_support(itemset, dataset):
    return sum([1 for transaction in dataset if set(itemset).issubset(set(transaction))])

def subsets(itemset):
    return [list(comb) for i in range(1, len(itemset)) for comb in combinations(itemset, i)]

def generate_association_rules(dataset, frequent_sets, min_confidence):
    rules = []
    for itemset in frequent_sets:
        for antecedent in subsets(itemset):
            consequent = list(set(itemset) - set(antecedent))
            if antecedent and consequent:
                antecedent_support = calculate_support(antecedent, dataset)
                rule_support = calculate_support(itemset, dataset)
                confidence = rule_support / antecedent_support if antecedent_support != 0 else 0
                if confidence >= min_confidence:
                    rules.append((antecedent, consequent))
    return rules
