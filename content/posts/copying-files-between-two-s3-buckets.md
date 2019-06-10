+++
title = "Copying Files Between Two S3 Buckets"
date = "2015-10-16"
slug = "2015/10/16/copying-files-between-two-s3-buckets"
Categories = ["AWS"]
+++

Today, I have to copy files from one S3 bucket to another S3 bucket which sitting in separate AWS account.

Initially, I was thinking to use S3 clients ( Tranmit or Cyberduck ) to download the files first and manually upload the files again to the other S3 Bucket. However, this approach will consume a lot of bandwidth and really slow if you have a lot of files in your S3 bucket.

After a bit of research, I found that you can easily copy files between two S3 buckets. You can use either s4cmd or AWS CLI.

## s3cmd or s4cmd

Run this command to install s4cmd

```bash
pip install s4cmd
```

After you finished setting up the AWS credentials, you can start the copying process.

```bash
# format
s4cmd cp s3://<source-bucket> s3://<target-bucket>/ --recursive

#example
s4cmd cp s3://rudylee-images s3://rudylee-new-images/ --recursive
```

## AWS CLI

Install the cli through pip

```bash
pip install awscli
```

And configure it

```bash
awscli configure
```

The usage is quite similar to s4cmd, see below:

```bash
aws s3 cp s3://<source-bucket> s3://<destination-bucket>
```

I prefer using AWS CLI because it has more options and official support. AWS CLI has a built it support can specify the ACL and permission of the objects.

```bash
# The command below will allow the target bucket owner to have full access to the object
aws s3 cp s3://<source-bucket> s3://<target-bucket> --acl "bucket-owner-full-control" --recursive
```

Since my target bucket is sitting in separate AWS account, I have to set another permission to allow everyone to upload and delete files into my target bucket.

If you want to follow this approach, make sure to delete that permission after you finished with the copying.

The other option is to set the S3 bucket policy manually, see this link: [http://serverfault.com/questions/556077/what-is-causing-access-denied-when-using-the-aws-cli-to-download-from-amazon-s3](http://serverfault.com/questions/556077/what-is-causing-access-denied-when-using-the-aws-cli-to-download-from-amazon-s3)
