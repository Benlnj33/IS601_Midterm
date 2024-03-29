import pandas as pd

HISTORY_FILE = 'test.csv'

def load_history():
    try:
        history_df = pd.read_csv(HISTORY_FILE)
    except FileNotFoundError:
        history_df = pd.DataFrame(columns=['Expression', 'Result'])
    return history_df

def save_history(history_df):
    history_df.to_csv(HISTORY_FILE, index=False)

def clear_history():
    history_df = pd.DataFrame(columns=['Expression', 'Result'])
    save_history(history_df)

def delete_record(history_df, index):
    try:
        history_df.drop(index, inplace=True)
        save_history(history_df)
        print('Record deleted successfully.')
    except KeyError:
        print('Invalid record index. Record not found.')
