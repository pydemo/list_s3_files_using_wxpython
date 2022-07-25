import boto3
from pprint import pprint as pp
client = boto3.client('s3')
pfx_paginator = client.get_paginator('list_objects_v2')
pfx_iterator = pfx_paginator.paginate(Bucket='k9-filestore', Delimiter='/',Prefix='k9-feed-doc-lims/',StartAfter='k9-feed-doc-lims/A010157901.FINAL_v1_report.pdf', 
 MaxKeys=1000)
for page in pfx_iterator:
    pp(page)
    break