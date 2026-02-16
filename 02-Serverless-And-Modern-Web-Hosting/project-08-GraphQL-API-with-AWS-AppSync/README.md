# Project: GraphQL API with AWS AppSync

This project demonstrates a serverless GraphQL API built using AWS AppSync, AWS Lambda, and Amazon DynamoDB. The application allows creating and querying poll data using GraphQL queries and mutations.

---

## Architecture Overview
- Client interacts with a GraphQL API
- AWS AppSync handles GraphQL queries and mutations
- AWS Lambda acts as the resolver backend
- Amazon DynamoDB stores poll data
- Amazon CloudWatch provides logging and monitoring

---

## Features
- GraphQL-based API using AWS AppSync
- Serverless backend with AWS Lambda
- Persistent storage using DynamoDB
- Real-time query and mutation handling
- Scalable and fully managed architecture

---

## AWS Services Used
- AWS AppSync (GraphQL API)
- AWS Lambda (Resolvers)
- Amazon DynamoDB (Data storage)
- AWS IAM (Permissions)
- Amazon CloudWatch (Logs)

---

## Workflow
- `createPoll` mutation stores poll data in DynamoDB
- `getPoll` query retrieves poll data by ID
- Lambda resolver handles both read and write operations
- AppSync manages schema, resolvers, and API execution

---

## Testing
- Mutations and queries tested using AppSync Query Editor
- Verified data persistence in DynamoDB
- Logs monitored via CloudWatch

---

## Status
Completed ✅

