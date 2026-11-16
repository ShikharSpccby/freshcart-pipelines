# FreshCart Pipelines: End-to-End Data Platform
**Author:** Shikhar Pandey (`26pcso05`)  
**Repository:** [github.com/ShikharSpccby/freshcart-pipelines](https://github.com/ShikharSpccby/freshcart-pipelines)

An end-to-end modern data engineering platform demonstrating version control, CI/CD automation, Medallion ELT data warehousing on Snowflake, orchestrated machine learning pipelines with Mage, and real-time event streaming using RabbitMQ topic exchanges.

---

## Repository Structure

```text
freshcart-pipelines/
├── README.md                           # Project overview, architecture, and documentation
├── .gitignore                          # Ignored patterns (.env, *.pkl, *.csv, mage.log, __pycache__/)
├── .env.example                        # Environment variable template for Snowflake & RabbitMQ
├── requirements.txt                    # Project Python dependencies
├── config/
│   ├── __init__.py
│   └── settings.py                     # Centralized project configuration and environment bindings
├── elt/                                # Part B: FreshCart ELT Pipeline on Snowflake
│   ├── freshcart_elt.py                # Python orchestration script for Snowflake SQL & DQ checks
│   ├── freshcart_elt.ipynb             # Interactive Jupyter notebook with outputs
│   └── sql/
│       ├── 00_setup_and_bronze.sql     # Database, schema, staging, tables, and reference data setup
│       ├── 10_orders_clean.sql         # Silver cleaning, validation rules, and quarantine MERGE
│       ├── 20_orders_dedup.sql         # Silver deduplication via window ranking
│       └── 30_gold_fct_orders.sql      # Gold fact table model with SCD2 temporal joins & row_hash
├── iris_project/                       # Part C: Orchestrated ML Pipeline with Mage
│   ├── metadata.yaml
│   ├── pipelines/iris_classifier/
│   │   └── metadata.yaml               # Directed Acyclic Graph (DAG) configuration
│   ├── data_loaders/
│   │   └── load_iris.py                # Load raw Iris dataset with 150-row test gate
│   ├── transformers/
│   │   ├── validate_iris_schema.py     # Custom block: Checks nulls and 3 target classes
│   │   ├── prepare_data.py             # 80/20 train/test split with quality test
│   │   ├── train_model.py              # Decision tree classifier with 80% accuracy gate
│   │   └── evaluate_model.py           # Evaluation branch: Confusion matrix & macro metrics
│   └── data_exporters/
│       └── save_results.py             # Downstream exporter writing iris_predictions.csv
├── stream/                             # Part D: Real-Time Event Streaming with RabbitMQ
│   ├── dispatcher.py                   # Topic publisher generating city.zone.type events
│   ├── driver.py                       # Driver consumer with ACK/NACK validation logic
│   └── lakehouse_consumer.py           # Bonus: Streaming micro-batch consumer into Lakehouse
├── tests/
│   ├── __init__.py
│   ├── test_project_identity.py        # Project metadata and identity tests
│   ├── test_prepare_data.py            # CI unit test validating 80/20 partition logic
│   └── test_pipeline_blocks.py         # End-to-end integration tests for Mage blocks
└── .github/workflows/
    └── ci.yml                          # GitHub Actions CI workflow running Python 3.12 & pytest
```

---

## Quickstart Guide

### 1. Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running Unit Tests
```bash
PYTHONPATH=. pytest -v
```

### 3. Running the Snowflake ELT Pipeline
```bash
# Set up environment variables in .env, then run orchestration script
python elt/freshcart_elt.py
```

### 4. Running the Mage ML Pipeline
```bash
# Run pipeline from command line with test execution
mage run iris_project iris_classifier --test

# Pass custom runtime parameters (e.g., max_depth)
mage run iris_project iris_classifier --runtime-vars '{"max_depth": 3}' --test
```

### 5. Running the Real-Time Event Stream (RabbitMQ)
```bash
# Terminal 1: Launch Dispatcher
python stream/dispatcher.py

# Terminal 2: Driver Ravi (Koramangala any)
python stream/driver.py Ravi "bangalore.koramangala.*"

# Terminal 3: Supervisor Control (All Bangalore events)
python stream/driver.py Control "bangalore.#"
```

### 6. Running the Lakehouse Stream Ingestion (Bonus)
```bash
python stream/lakehouse_consumer.py
```

---

## Summary of Assignment Parts

* **Part A (Git & CI/CD):** Four-box Git architecture, git command lifecycle, automated GitHub Actions workflow (`ci.yml`) verifying test gates on push.
* **Part B (FreshCart ELT on Snowflake):** Medallion architecture (`bronze.orders_raw` VARIANT $\rightarrow$ `silver.orders_clean` $\rightarrow$ `gold.fct_orders`), SCD Type 2 dimension tracking (`dim.customers_scd2`), currency validation, quarantine error handling, and strict idempotency via `row_hash` + `MERGE`.
* **Part C (Mage ML Pipeline):** Modular ML pipeline with block-level quality test gates. Demonstrates fail-fast test-gating where failing assertions (e.g. at `max_depth=1`) abort downstream file exports (`save_results`).
* **Part D (RabbitMQ Event Stream):** Topic exchange (`rapido-dispatch`) with routing keys (`city.zone.type`) and binding patterns (`*`, `#`). Implements consumer `ACK`/`NACK` handling to discard poison-pill payloads (`requeue=False`).
* **Bonus:** Real-time 60-second micro-batch ingestion into Snowflake Lakehouse with verified idempotency.