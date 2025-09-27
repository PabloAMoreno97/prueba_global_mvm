import os

from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd

from utils.constants import s3_bucket, s3_data_folder, file_name


load_dotenv()

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)


def read_parquet_from_s3(path):
    try:
        df = pd.read_parquet(path, engine="pyarrow")
        return df
    except Exception as e:
        print(f"Error while reading file {path} from S3", e)


if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    s3_path = f"s3://{s3_bucket}/{s3_data_folder}/{file_name}"
    employees_df = read_parquet_from_s3(s3_path)

    with engine.connect() as conn:
        employees_df.to_sql(name="employees", con=conn, if_exists="replace", index=False)
