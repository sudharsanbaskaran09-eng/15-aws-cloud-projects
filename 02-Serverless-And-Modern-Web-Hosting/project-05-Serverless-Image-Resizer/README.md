## Project: Serverless Image Resizer on AWS

This project demonstrates an event-driven serverless image processing pipeline using AWS services. When an image is uploaded to an S3 bucket, a Lambda function is automatically triggered to process the image and store the output in another S3 bucket.

### Features
- Event-driven serverless architecture
- Automatic image processing on upload
- No servers or infrastructure management
- Scalable and cost-efficient design
- Fully automated workflow using S3 triggers

### Architecture Flow
- User uploads an image to S3 (source bucket)
- S3 ObjectCreated event triggers AWS Lambda
- Lambda processes the image
- Processed image is stored in S3 (destination bucket)

### AWS Services Used
- Amazon S3 (Source & Destination buckets)
- AWS Lambda (Python runtime)
- AWS IAM (Execution role & permissions)
- Amazon CloudWatch (Logs & monitoring)

### Testing
- Uploaded image files to the source S3 bucket
- Verified automatic processing and output in destination bucket
- Confirmed execution using CloudWatch logs

### Status
Completed ✅

