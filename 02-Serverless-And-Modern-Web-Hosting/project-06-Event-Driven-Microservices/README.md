## Project: Event-Driven Microservices on AWS

This project demonstrates an event-driven microservices architecture using AWS managed services. The system is designed to publish events asynchronously and process them through decoupled consumer services.

### Architecture Overview
- A publisher microservice emits events
- Events are published to an Amazon SNS topic
- Amazon SQS queues buffer the events
- A consumer microservice processes messages asynchronously

This architecture enables loose coupling, scalability, and fault tolerance.

### Features
- Event-driven communication between microservices
- Asynchronous message processing
- Loose coupling using SNS and SQS
- Fully serverless architecture
- Scalable and resilient design

### AWS Services Used
- AWS Lambda (Publisher & Consumer)
- Amazon SNS (Event Publisher)
- Amazon SQS (Message Queue)
- AWS IAM (Execution roles & permissions)
- Amazon CloudWatch (Logging & monitoring)

### Workflow
1. Publisher Lambda publishes an event to SNS
2. SNS forwards the event to an SQS queue
3. Consumer Lambda is triggered by SQS
4. Consumer processes the event asynchronously

### Testing
- Publisher Lambda tested using Lambda test events
- Verified message delivery through SNS and SQS
- Confirmed consumer execution using CloudWatch logs

### Status
Completed ✅

