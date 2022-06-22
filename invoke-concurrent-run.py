import sys
from awsglue.job import Job
import boto3

client = boto3.client('glue')

for x in range(1,21):
    response1 = client.start_job_run(
                 JobName = 'artemis-1-math-fn-concurrent-run',
                 Arguments = {
                   '--key_1':   str(2+x),
                   '--key_2':  str(3+x),
                   '--key_3':  str(4+x),
                   '--key_4': str(5+x) } )
