from kafka import KafkaConsumer
from json import loads
from kafka import TopicPartition
import json
import pandas as pd
import boto3
from pandasql import sqldf

if __name__=='__main__':
    consumer = KafkaConsumer(bootstrap_servers=['broker0:19092'],auto_offset_reset='earliest')
    consumer.assign([TopicPartition('order2', 0)])
    print("starting the consumer")
    # dataframe = pd.DataFrame(columns=['_id','first_name','last_name','gender', 'city','email']) # Note that there are now row data inserted.
    dataframe = []
    i = 0
    # print(dataframe)
    for msg in consumer:
        df1 = msg.value.decode('utf-8')
        data_dict = json.loads(df1)
        df2 = pd.DataFrame(data_dict["_airbyte_data"], index=[0])

        dataframe.append(df2)
        result_df = pd.concat(dataframe, ignore_index=True)
        print(result_df)
        result_df.drop(['_ab_cdc_updated_at','_ab_cdc_log_file', '_ab_cdc_log_pos', '_ab_cdc_lsn'], axis=1, errors='ignore').to_csv("/home/appuser/files/data.csv", index=False)

        i+=1

        q1 = "select _ab_cdc_deleted_at, _ab_cdc_updated_at,_id,city,email,first_name,gender,last_name from result_df where _ab_cdc_deleted_at is null group by _id"
        main_data = sqldf(q1,globals())
        # print(main_data2)
        q2="select round(_id) as _id,city,email,first_name,gender,last_name from main_data"
        main_data3 = sqldf(q2,globals())
        # print(main_data3)
        main_data3.to_parquet("/home/appuser/files/main_data.parquet")
        session = boto3.Session(aws_access_key_id='aws_access_key',aws_secret_access_key='aws_secret_key')
        s3 = session.resource('s3')
        s3.Bucket('bucket_name').upload_file("/home/appuser/files/main_data.parquet",'main_data.parquet')