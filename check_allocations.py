import pandas as pd
import os
import sys
from datetime import datetime

# Define file paths
ALLOCATIONS_DIR = os.path.join(os.path.dirname(__file__), 'src')
ADDRESSES_FILE = os.path.join(os.path.dirname(__file__), 'addresses.txt')

class Logger(object):
    def __init__(self, filename="default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, 'w', encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        pass

def format_number(num, is_lam=False):
    """Formats a number for beautiful printing."""
    if isinstance(num, float):
        if is_lam:
            return str(num)
        return f"{num:,.2f}"
    return f"{num:,}"

def load_all_allocations(directory):
    """Loads and combines all CSV files from a given directory."""
    all_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]
    if not all_files:
        return pd.DataFrame()
        
    df_list = [pd.read_csv(file) for file in all_files]
    return pd.concat(df_list, ignore_index=True)

def check_allocations():
    """
    Checks allocation data for a given list of addresses and prints a summary.
    """
    results_dir = os.path.join(os.path.dirname(__file__), 'results')
    os.makedirs(results_dir, exist_ok=True)
    log_filename = os.path.join(results_dir, datetime.now().strftime("result-%H-%M-%d-%m-%y.log"))
    sys.stdout = Logger(log_filename)
    
    try:
        # --- Read Input Files ---
        if not os.path.isdir(ALLOCATIONS_DIR):
             raise FileNotFoundError(f"The source directory '{ALLOCATIONS_DIR}' was not found. Please run the script to split the main CSV first.")

        allocations_df = load_all_allocations(ALLOCATIONS_DIR)
        if allocations_df.empty:
            print("No allocation files found in the 'src' directory or the files are empty.")
            return

        with open(ADDRESSES_FILE, 'r') as f:
            addresses_to_check = [line.strip() for line in f if line.strip()]

        # Prepare for case-insensitive matching
        allocations_df['address_lower'] = allocations_df['address'].str.lower()
        addresses_to_check_lower = [addr.lower() for addr in addresses_to_check]

        # --- Process Data ---
        found_allocations = allocations_df[allocations_df['address_lower'].isin(addresses_to_check_lower)]

        # --- Print Individual Results ---
        print("\n--- Allocation Checker Results ---")
        if not found_allocations.empty:
            print(f"\nFound {len(found_allocations)} of {len(addresses_to_check)} addresses:\n")
            for _, row in found_allocations.iterrows():
                print(f"  Address: {row['address']}")
                print(f"    ├─ LXP  : {format_number(row.get('lxp', 'N/A'))}")
                print(f"    ├─ LAM  : {format_number(row.get('lam', 'N/A'), is_lam=True)}")
                print(f"    └─ LINEA: {format_number(row.get('linea_allocation', 'N/A'))}")
                print("  " + "-"*30)
        else:
            print("\nNo matching addresses found in the allocation file.\n")

        # --- Print Summary Statistics ---
        total_addresses = len(addresses_to_check)
        found_count = len(found_allocations)
        percentage_found = (found_count / total_addresses * 100) if total_addresses > 0 else 0
        total_linea = found_allocations['linea_allocation'].sum()
        total_lxp = found_allocations['lxp'].sum()

        print("\n--- Summary ---")
        print(f"  Total addresses to check: {format_number(total_addresses)}")
        print(f"  Addresses found         : {format_number(found_count)} ({percentage_found:.2f}%)")
        print(f"  Total LXP on found      : {format_number(total_lxp)}")
        print(f"  Total LINEA on found    : {format_number(total_linea)}")
        print("-"*19 + "\n")

    except FileNotFoundError as e:
        print(f"Error: A required file was not found. Please ensure both 'addresses.txt' and 'linea_allocations.csv' exist.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    check_allocations()
