import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64",
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
]


@click.command()
@click.option("--pg-user", "--db-user", "pg_user", default="root", show_default=True, help="PostgreSQL username")
@click.option("--pg-pass", "--db-pass", "pg_pass", default="root", show_default=True, help="PostgreSQL password")
@click.option("--pg-host", "--db-host", "pg_host", default="localhost", show_default=True, help="PostgreSQL host")
@click.option("--pg-port", "--db-port", "pg_port", default=5432, show_default=True, type=int, help="PostgreSQL port")
@click.option("--pg-db", "--db-name", "pg_db", default="ny_taxi", show_default=True, help="PostgreSQL database name")
@click.option("--year", default=2021, show_default=True, type=int, help="Year of dataset")
@click.option("--month", default=1, show_default=True, type=int, help="Month of dataset")
@click.option("--chunk-size", default=100000, show_default=True, type=int, help="Chunk size for batch ingestion")
@click.option("--target-table", default="yellow_taxi_data", show_default=True, help="Target PostgreSQL table name")
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, chunk_size, target_table):
    """Ingest NY Taxi data into a PostgreSQL database in chunks."""
    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow"
    url = f"{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz"

    print(f"Connecting to postgresql://{pg_user}:***@{pg_host}:{pg_port}/{pg_db} ...")
    print(f"Downloading and reading dataset from: {url}")

    engine = create_engine(f"postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")

    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunk_size,
    )
    first = True

    for df_chunk in tqdm(df_iter, desc="Ingesting chunks"):
        if first:
            df_chunk.to_sql(name=target_table, con=engine, if_exists="replace")
            first = False
        else:
            df_chunk.to_sql(name=target_table, con=engine, if_exists="append")

    print(f"Successfully finished ingestion into '{target_table}' table!")


if __name__ == "__main__":
    run()
