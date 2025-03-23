# Notification Service

## Overview
The Notification Service is a key component of the microservices-based application. It is responsible for sending email notifications to users once their video-to-MP3 conversion job is complete. The service subscribes to an event queue (RabbitMQ) and listens for messages indicating that a conversion job has been completed. Upon receiving such a message, it sends an email to the user containing a download link for the converted file. This service is part of the larger pdf2podcast-microservice project. For more information about the main project, visit [pdf2podcast-microservice](https://github.com/Prosperibe12/pdf2podcast-microservice).

## Prerequisites
- Docker: For containerizing the service.
- Kubernetes cluster: For deploying and managing the service
- RabbitMQ: A running instance of RabbitMQ in the Kubernetes cluster for event queuing.
- MongoDB: A running instance of MongoDB in the Kubernetes cluster for data storage.
- SMTP Server: Access to an SMTP server for sending emails (e.g., Gmail, SendGrid, or a custom SMTP server).

## Configuration
visit [pdf2podcast-microservice](https://github.com/Prosperibe12/pdf2podcast-microservice)

## Contact
For any questions or support, please contact [Prosperibe12@gmail.com](mailto:Prosperibe12@gmail.com).
