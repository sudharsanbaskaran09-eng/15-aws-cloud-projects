# Project: Real-Time Polling App using AWS WebSockets

This project demonstrates a **real-time serverless application** built using AWS WebSocket APIs. The system enables **bi-directional communication** between clients and the backend, allowing real-time polling and live message exchange.

---

## Architecture Overview
- Clients establish a WebSocket connection with the backend
- Amazon API Gateway manages WebSocket connections
- Connection lifecycle events are handled using AWS Lambda
- Custom routes process real-time actions (polling events)
- Amazon CloudWatch is used for logging and monitoring

This architecture enables **low-latency communication**, **scalability**, and **serverless real-time processing**.

---

## Features
- Real-time bi-directional communication using WebSockets
- Serverless backend using AWS Lambda
- Handling of `$connect`, `$disconnect`, and custom routes
- Event-based message routing
- Fully managed and scalable architecture

---

## AWS Services Used
- AWS API Gateway (WebSocket API)
- AWS Lambda (Connection handlers & business logic)
- AWS IAM (Execution roles & permissions)
- Amazon CloudWatch (Logging & monitoring)

---

## Workflow
- Client connects to the WebSocket endpoint
- `$connect` route initializes the connection
- Client sends polling actions through WebSocket messages
- Custom route processes the action using Lambda
- Messages are handled in real time
- `$disconnect` route handles connection termination

---

## Testing
- WebSocket connection tested using AWS CloudShell (`wscat`)
- Verified successful connection handshake
- Validated real-time message flow
- Monitored execution and logs using CloudWatch

---

## Status
Completed ✅

