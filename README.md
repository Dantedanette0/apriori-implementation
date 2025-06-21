# Apriori Implementation

This repository implements the Apriori algorithm from scratch in Python using synthetic data that I generate in the generate_data.py file.

![assosiative law demonstration](apriori.png)

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


pip install -r requirements.txt


## Getting Started

1. **Clone the repository**:

   ```bash
   git clone [https://github.com/Dantedanette0/apriori-implementation.git](https://github.com/Dantedanette0/apriori-implementation.git)

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
