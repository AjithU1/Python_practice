from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import logging
import time


class MyData:
    def __init__(self):
        try:
            # self.db_conn = create_engine(pymysql::/"username" + ":" + "password" + "@" + "host_name" + "/" +
            # "schema").connect()
            self.mysql_engine = create_engine(
                'mysql+pymysql://your_mysql_user:your_mysql_password@your_mysql_host/your_mysql_database')
            # self.load_conn = create_engine(postgresql::/"username" + ":" + "password" + "@" + "host_name" + "/" +
            # "schema").connect()
            self.pg_engine = create_engine(
                'postgresql+psycopg2://your_postgresql_user:your_postgresql_password@your_postgresql_host'
                '/your_postgresql_database')
        except Exception as e:
            logging.info(str(e))

    def extract_data(self):
        cus_query = f"select id,name from customer_information where date(created_date) = {cur_date};"
        cus_df = pd.read_sql(cus_query, self.mysql_engine)

        prod_info_query = f"select prod_name,prod_id from product_information where date(created_date) = {cur_date};"
        prod_df = pd.read_sql(prod_info_query, self.mysql_engine)

        sales_query = f"select sales_id, invoice_no from sales where date(crete_date) = {cur_date};"
        sales_df = pd.read_sql(sales_query, self.mysql_engine)

        df = pd.concat([cus_df, prod_df, sales_df])
        return df

    def load_data(self, df):
        load_df = df.to_sql("table_name", self.pg_engine, if_exists='append', index=False)


if __name__ == '__main__':
    now = datetime.now()
    cur_date = now.date()
    if now.strftime("%H:%M") in ["01:00", "15:00"]:
        ob = MyData()
        my_data = ob.extract_data()
        ob.load_data(my_data)
        time.sleep(60)
    else:
        exit()
