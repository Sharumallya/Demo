import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    # Your code goes here, inside the "main" handler.
   from snowflake.snowpark.functions import col

def filter_by_role(session, table_name, role):
  df = session.table(table_name)
  return df.filter(col("role") == role)
