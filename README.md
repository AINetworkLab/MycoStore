# Re2po

A Redundancy-aware Model Repository in Edge Serverless Computing

---

## 1. **Project Structure**

The main project structure is as follows:

```plaintext
deps/
├── docker-compose.yml           # Docker Compose configuration for containerized services
└── openwhisk-deploy-kube/       # Deployment files for OpenWhisk on Kubernetes
    ├── deploy/                  # Configuration files and scripts for cluster setup
    ├── helm/                    # Helm Charts for Kubernetes application deployment
    └── test_node/               # Test scripts and utilities for OpenWhisk and MinIO integration
src/
├── dao/                         # Data Access Objects for managing database operations
│   ├── data_dao.py              # General data access logic
│   ├── model_dao.py             # Model-related database operations
│   └── storage_dao.py           # Storage-related database operations
├── model/                       # Models for database schema
│   └── entity.py                # Database schema definition using SQLAlchemy
├── services/                    # Business logic and service layer
│   ├── minio_service.py         # MinIO-related service logic
│   ├── model_compose.py         # Logic for composing models
│   ├── model_compose_tf.py      # TensorFlow-specific model composition logic
│   ├── model_save.py            # Logic for saving models
│   └── model_save_tf.py         # TensorFlow-specific model saving logic
└── utils/                       # Utility scripts
    ├── minio_utils.py           # Helper functions for MinIO operations
    └── temp_dir.py              # Temporary scripts for debugging or experimentation
```

## 2. **Key Components**

### 1. **deps**

- **`docker-compose.yml`**: Defines and manages containerized services for local development and testing.
- **`openwhisk-deploy-kube/`**: Contains all the deployment configurations and scripts for running OpenWhisk on a Kubernetes cluster.
  - **`deploy/`**: Includes Kind cluster configurations and startup scripts.
  - **`helm/`**: Helm Charts for deploying OpenWhisk and its dependencies.
  - **`test_node/`**: Python scripts for testing OpenWhisk functions, MinIO integration, and other components.

### 2. **src**

- **`dao/`**: Data Access Layer.
  - Handles interactions with the database.
- **`model/`**: Database schema definitions using SQLAlchemy.
- **`services/`**: Core business logic and service implementations.
  - Includes TensorFlow-specific logic for handling AI models and MinIO services.
- **`utils/`**: General utility functions and scripts for various tasks.

---

## 3. **Prerequisites**

To use this project, ensure the following are installed:

- [Docker](https://www.docker.com/)
- [Kubernetes](https://kubernetes.io/)
- [Helm](https://helm.sh/)
- Python 3.8+ with the required dependencies (see `/lib/requirements.txt`)

---

## Summary

This project integrates multiple services and tools for efficient model management, Kubernetes-based container orchestration, and OpenWhisk deployment.

### Contributing

Feel free to submit issues or pull requests if you find any bugs or want to propose new features. Contributions are welcome!
