## Project: Serverless Expense Tracker on AWS

This project demonstrates a fully serverless backend for tracking expenses using AWS managed services. The application allows users to add expense records through a REST API and stores them securely in a NoSQL database.

### Features
- Serverless expense tracking backend
- REST API for adding expenses
- Input validation and error handling
- Scalable and cost-efficient architecture
- No server or infrastructure management

### Expense Data Model
Each expense record includes:
- Expense ID (UUID)
- Title
- Amount
- Category
- Date
- Created timestamp

### AWS Services Used
- AWS Lambda (Python runtime)
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- Amazon CloudWatch (logging)

### Testing
- API tested using Postman
- Verified HTTP status codes and JSON responses
- Confirmed data persistence in DynamoDB

### Status
Completed ✅

