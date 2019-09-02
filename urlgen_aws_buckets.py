import sys

# http://bucket.s3.aws-region.amazonaws.com
# http://bucket.s3.amazonaws.com (if bucket created prior to 03.2019, this won't work)

#Hint: pipe all variations to /tmp/list, then use firefox to open them all like this:
# for i in `cat /tmp/list`; do firefox --new-tab $i; done

regions=['us-east-1',
'us-east-2',
'us-west-1',
'us-west-2',
'ca-central-1',
'eu-central-1',
'eu-west-1',
'eu-west-2',
'eu-west-3',
'eu-north-1',
'ap-east-1',
'ap-northeast-1',
'ap-northeast-2',
'ap-northeast-3',
'ap-southeast-1',
'ap-southeast-2',
'ap-south-1',
'me-south-1',
'sa-east-1']

import sys
if len (sys.argv) != 2 :
    print "Usage: python urlget_aws_buckets.py bucketname" 
    sys.exit (1)
bucketname = sys.argv[1]


for region in regions:
	print ("http://s3."+ str(region) + ".amazonaws.com/" + bucketname)
	print ("http://" + bucketname + ".s3."+ str(region) + ".amazonaws.com")
	print ("http://" + bucketname + ".s3"+ ".amazonaws.com")

