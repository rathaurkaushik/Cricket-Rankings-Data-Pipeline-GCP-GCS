from googleapiclient.discovery import build

def trigger_df_job(cloud_event, environment):

    service = build('dataflow', 'v1b3')
    project = "cricket-api-505613"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "JobName": "beam-bq-job", #provide unique name for the job
        "parameters": {
            "javascriptTextTransformGcsPath": "gs://source-bucket-cricket/udf.js",  # paste bucket udf path here
            "JSONPath": "gs://source-bucket-cricket/bq.json",  # Paste the JSON path here
            "javascriptTextTransformFunctionName": "transform",
            "outputTable": "cricket-api-505613.raw_ds:icc_odi_batsman_ranking",  # provide the output table name here from bigquery
            "inputFilePattern": "gs://cricket-ranking-data-de/batsmen_rankings.csv",  # provide the input file path here from GCS
            "bigQueryLoadingTemporaryDirectory": "gs://source-bucket-cricket/temp"  # provide the temp directory path here from GCS

        }
    }

    request = service.projects().templates().launch(projectId=project, body=template_body, gcsPath=template_path)
    response = request.execute()
    print(response)