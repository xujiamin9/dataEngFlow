# Transactional Data Flow

![alt text](https://github.com/xujiamin9/transDataFlow/blob/main/transDataFlow.jpeg?raw=true)

<h2>Creating a simple poc dataflow</h2> 

<p>Create data using Faker<br>
Producers publish to Kafka<br> 
Consume and Transform using PySpark<br>
Use PySpark Structured Streaming to Write to GCP BigQuery<br>
Data model BigQuery for Dashboard use<br>
Analysis and Dashboarding with Qlik<br>
Dockerize Producers with scaling for to mimic higher traffic<br>
Dockerize Consumers ingestion can be scaled with high dataloads<br>
Orchestrate Docker with Kubernetes<br>
Monitor with Prometheus, Grafana<br>
Infastructure, Kubernetes management with Terraform<br>
Data Validation with SQLAlchemy, Pandas, scheduled using Airflow<br>
</p>

<h2>Resources:</h2>
<p>
https://dev.to/ankitmalikg/python-generate-fake-data-with-faker-1ecj<br>
https://www.geeksforgeeks.org/how-to-install-and-run-apache-kafka-on-windows/<br>
https://www.svix.com/guides/kafka/python-kafka-producer/<br>
https://medium.com/google-cloud/streaming-events-to-bigquery-using-spark-structured-streaming-96cf541de4ed<br>
https://www.terraform.io/<br>
</p>
Run Locally:

<p>cd C:\Kafka\<br>
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties<br>
.\bin\windows\kafka-server-start.bat .\config\server.properties<br>
.\bin\kafka-topics.bat --describe --topic transactions --bootstrap-server localhost:9092<br>
</p>