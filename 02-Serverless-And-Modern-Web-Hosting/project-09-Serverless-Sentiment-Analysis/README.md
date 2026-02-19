# Project: Serverless Sentiment Analysis on AWS

This project demonstrates a serverless sentiment analysis API built using AWS managed services. The application analyzes user-provided text and determines its sentiment using Amazon Comprehend.

---

## Architecture Overview
- Client sends text input via an HTTP API
- API Gateway forwards the request to AWS Lambda
- Lambda invokes Amazon Comprehend for sentiment detection
- Sentiment result is returned to the client
- Logs and metrics are captured in Amazon CloudWatch

This architecture is fully serverless, scalable, and cost-efficient.

---

## Features
- Real-time sentiment analysis
- Fully serverless backend
- REST API exposed via API Gateway
- AI-powered text analysis using Amazon Comprehend
- Error handling for invalid inputs
- Production-style request parsing

---

## AWS Services Used
- AWS Lambda (Backend logic)
- Amazon API Gateway (HTTP API)
- Amazon Comprehend (Sentiment analysis)
- AWS IAM (Permissions & roles)
- Amazon CloudWatch (Logging & monitoring)

---

## Workflow
1. Client sends a POST request with text input
2. API Gateway triggers the Lambda function
3. Lambda parses the request body
4. Amazon Comprehend analyzes the sentiment
5. Sentiment result is returned as JSON

---

## Testing
- Lambda function tested using AWS Lambda test events
- API tested using Postman with real HTTP requests
- Verified sentiment response and confidence scores

---

## Status
Completed ✅

