#!python

import fire
import boto3
from botocore.exceptions import ClientError


class S3(object):
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.client = boto3.client('s3')

    def list_buckets(self):
        """
        list s3 buckets
        :param region_name: Region of the bucket
        :return:
        """
        try:
            print(self.client.list_buckets())
        except ClientError as e:
            print(e)


if __name__ == '__main__':
    fire.Fire(S3)
