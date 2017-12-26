# hbase


## install


## cli

list
count 'tablename'

scan 'tablename',{LIMIT=>20}

### export
hbase org.apache.hadoop.hbase.mapreduce.Driver export  tablename    location
hbase org.apache.hadoop.hbase.mapreduce.Driver import  tablename    location
