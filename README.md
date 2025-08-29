
# Linea Allocation Checker

This script checks the LINEA token allocation for a list of wallet addresses based on a provided allocation file.

## Features

- Displays detailed allocation information (LXP, LAM, LINEA tokens) for each found address.
- Provides summary statistics, including the number of found addresses, total tokens, and total LXP for the found wallets.
- Case-insensitive address matching.

## Prerequisites

- Python 3.6+
- `pandas` library

## Setup

1.  **Place your files in this directory:**
    - `linea_allocations.csv`: This file must contain the airdrop data, including the columns `address`, `lxp`, `lam`, and `linea_allocation`.
    - `addresses.txt`: This file should contain the list of wallet addresses you want to check, with one address per line.

2.  **Install dependencies:**
    Open your terminal in this directory and run the following command to install the required Python library:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the setup is complete, run the script with the following command:

```bash
python3 check_allocations.py
```

### Example Output

The script will print the results directly to your terminal. 

```
--- Allocation Checker Results ---

Found 2 of 3 addresses:

  Address: 0x1234...abcd
    ├─ LXP  : 1,234.56
    ├─ LAM  : 500.00
    └─ LINEA: 1,000.00
  ------------------------------
  Address: 0x5678...efgh
    ├─ LXP  : 6,543.21
    ├─ LAM  : 1,000.00
    └─ LINEA: 5,000.00
  ------------------------------

--- Summary ---
  Total addresses to check: 3
  Addresses found         : 2 (66.67%)
  Total LXP on found      : 7,777.77
  Total LINEA on found    : 6,000.00
-------------------

```

<h1 align="center">🙏 Support My Work 🙏</h1>

If you find this script useful, please consider a donation to help fuel future development and more tools like this. Every little bit helps!

---

###  wallets:

- **EVM (Ethereum, Polygon, BSC, etc.):**
  ```
  0xa45d667f720545946af5ba8f1dc3d099c1003aff
  ```

- **SOL (Solana):**
  ```
  HS7Sza5EHv6xvvd1Pjuy1YsovPNFjkqr2W7cu4XEGQ1e
  ```

---

**Thank you for your support!**