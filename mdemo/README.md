1. Create Pub/Sub Topic
```
gcloud pubsub topics create TOPIC_NAME 
```

2. Create BigQuery Dataset 
```
bq --location=us mk --dataset PROJECT_ID:DATASET_NAME
```

3. Create BigQuery Table
bq mk --table PROJECT_ID:DATASET_NAME.TABLE_NAME PATH_TO_SCHEMA

*Note the following schema created from an extract of the BigQuery New York 311 public dataset (bigquery-public-data.new_york_311.311_service_requests)*

```json
[
 {
   "name": "unique_key",
   "type": "STRING",
   "mode": "NULLABLE"
 },
 {
  
   "name": "created_date",
   "type": "TIMESTAMP",
   "mode": "NULLABLE"
 },
 {
  
   "name": "complaint_type",
   "type": "STRING",
   "mode": "NULLABLE"
 },  
 {
  
   "name": "location_type",
   "type": "STRING",
   "mode": "NULLABLE"
 }
]
```

4. Create a temporary storage bucket for Dataflow 
```
gsutil mb gs://BUCKET_NAME
```

5. Create Datflow job using the Google-provided template: **PubSub_to_BigQuery**
```
gcloud dataflow jobs run JOB_NAME \
    --gcs-location gs://dataflow-templates/VERSION/PubSub_to_BigQuery \
    --region REGION_NAME \
    --staging-location TEMP_LOCATION \
    --parameters \
inputTopic=projects/PROJECT_ID/topics/TOPIC_NAME,\
outputTableSpec=PROJECT_ID:DATASET.TABLE_NAME
```

6. Create Python virtual environment
``` 
python -m venv venv
```

7. Activate Python virtual environment 
```
source venv/bin/activate
```

8. Install python packages in virtual environment
```
pip install argparse google-cloud-pubsub
```

7. Run python script in virtual environment
``` 
python send.py --filename PATH_TO_NEWLINE_DELIMITED_JSON_FILE   --topic TOPIC_NAME  --projectid PROJECT_ID
```
