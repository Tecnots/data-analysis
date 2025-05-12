from db_connection import engine
import pandas as pd



def main():
    df = pd.read_sql("select * FROM sales_transactions",engine)
    df['date'] =  pd.to_datetime(df['date'],errors='coerce')
    print(df['date'])
    
    
    




if __name__ == "__main__":
    main()
