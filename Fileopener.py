import pickle
import os

def load_and_explore_pkl(filename):
    # Load the pickle file with latin1 encoding
    with open(filename, 'rb') as f:
        data = pickle.load(f, encoding='latin1')  # Use 'latin1' to avoid encoding issues
    
    # Print a summary of the loaded data
    if isinstance(data, dict):
        print("Loaded data keys:")
        print(data.keys())  # Print all keys
        
        # Print summary of each key
        for key in data:
            print(f"\nKey: {key}")
            if key == 'signal':
                print("  - signal keys:", data[key].keys())
                print("    - chest keys:", data[key]['chest'].keys())
                print("    - wrist keys:", data[key]['wrist'].keys())
            elif key == 'label':
                print("  - label shape:", data[key].shape)
            else:
                print(f"  - {key}:", data[key])
    else:
        print("Loaded data is not a dictionary")
    
    return data

# Example usage:
if __name__ == "__main__":
    filename = "S2.pkl"  # Replace with your actual .pkl filename
    data = load_and_explore_pkl(filename)
    
    # Now you can use 'data' for further processing
    # Example: Access chest ACC data
    chest_acc_data = data['signal']['chest']['ACC']
    print("\nChest ACC data (first 5 samples):")
    print(chest_acc_data[:5])
