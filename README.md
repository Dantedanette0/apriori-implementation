# Synthetic Apriori Project

This repository implements the Apriori algorithm from scratch in Python and demonstrates its use on synthetic transactional datasets.

## Features

* **Generate synthetic data**: Create customizable sets of transactions for testing.
* **Frequent itemset mining**: Find all itemsets that meet a minimum support threshold using Apriori.
* **Association rule generation**: Derive implication rules from frequent itemsets with configurable confidence thresholds.

## Files

* `apriori.py` – Core implementation of Apriori and rule generation.
* `generate_data.py` – Utility to create synthetic transaction datasets.
* `examples/` – Sample Jupyter notebooks demonstrating usage and results.
* `requirements.txt` – Python dependencies.

## Requirements

* Python 3.7+
* `numpy`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Getting Started

1. **Clone the repository**:

   ```bash
   ```

git clone [https://github.com/Dantedanette0/apriori-implementation.git](https://github.com/Dantedanette0/apriori-implementation.git)
cd apriori-implementation

````

2. **Generate synthetic data** (optional):
   ```bash
python generate_data.py --transactions 100 --items 10 --max-items-per-transaction 5 --output data/transactions.csv
````

This will write a CSV file of transactions to `data/transactions.csv`.

3. **Run Apriori**:

   ```bash
   ```

python apriori.py --data data/transactions.csv --min-support 5 --min-confidence 0.6

````
   The script will print frequent itemsets and association rules.

4. **Explore examples**:
   Open one of the notebooks in the `examples/` folder to see visualizations and deeper explanations.

## Usage Options

```bash
# View help for Apriori script
env/bin/python apriori.py --help
````

Common flags:

* `--min-support`: Minimum support count (integer).
* `--min-confidence`: Minimum confidence (0–1).
* `--output`: Path to save rules as JSON.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
