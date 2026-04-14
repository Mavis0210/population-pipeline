import pandas as pd
from sqlalchemy import create_engine
import click



@click.command()
@click.option('--user', default='root', help='Database username')
@click.option('--password', default='root', help='Database password')
@click.option('--host', default='localhost', help='Database host')
@click.option('--port', default='5432', help='Database port')
@click.option('--db', default='population_db', help='Database name')
@click.option("--target-table", default="world_population", show_default=True)

def main(user, password, host, port, db, target_table):

    data_url ='https://raw.githubusercontent.com/datasets/population/main/data/population.csv'
    # ========== 1. EXTRACT (Download Data)==========

    df = pd.read_csv(data_url)

     # ========== 2. TRANSFORM (Clean the data!) ==========

     #2a. Fix column names (spaces → underscores, lowercase)
    df.columns = df.columns.str.lower().str.replace(' ', '_') 
    print(f"   Fixed column names: {list(df.columns)}")

    #2b. Check for missing values
    missing = df.isnull().sum() 
    print(f"   Missing values per column:\n{missing}")

    # 2c. Drop rows with missing values (if any)
    rows_before = len(df)
    df = df.dropna()
    rows_after = len(df)
    print(f"   Dropped {rows_before - rows_after} rows with missing data")

    # 2d. Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"   Found {duplicates} duplicate rows")

    # 2e. Remove duplicates (if any)
    df = df.drop_duplicates()
    print(f"   Final row count: {len(df)}")

    # 2. Connect to database
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')

    # 3. Load data
    df.to_sql(name=target_table, con=engine, if_exists='replace', index=False)
    
    count = pd.read_sql(f"SELECT COUNT(*) FROM {target_table}", engine).iloc[0, 0]
    print(f"Done! {count} rows loaded into '{target_table}'")

if __name__ == '__main__':
    main()


