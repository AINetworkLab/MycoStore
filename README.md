# MycoStore

A Cross-Model Layer Sharing Framework for Efficient Neural Network Model Cache at the Network Edge

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
│   ├── redis_dao.py             # Model data operations
│   └── storage_dao.py           # Storage-related database operations
├── model/                       # Models for database schema
│   └── entity.py                # Database schema definition using SQLAlchemy
├── services/                    # Business logic and service layer
│   ├── service.py               # Service logic
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

## 3. **Prerequisites**

To use this project, ensure the following are installed:

- [Docker](https://www.docker.com/)
- [Kubernetes](https://kubernetes.io/)
- [Helm](https://helm.sh/)
- Python 3.8+ with the required dependencies (see `/lib/requirements.txt`)

<!-- 
## Summary

CMLS is a redundancy-aware model repository designed for edge serverless computing environments. It addresses the challenges of high latency and large model sizes in machine learning (ML) inference tasks by caching models at the edge. Unlike traditional cloud-native ML inference systems that retrieve models from cloud repositories, CMLS stores and retrieves models directly at the edge, significantly reducing download times and data transmission overhead.

CMLS employs advanced techniques like model decomposition, layer-wise storage, and redundancy elimination to optimize both storage and data transfer. By identifying and removing redundant data, it reduces the model size by up to 23.9% while ensuring that only essential data is stored at the edge. This approach allows serverless functions to transparently access complete models without being aware of the underlying storage structure.

Key features of the CMLS framework include:
• Redundancy-aware model storage: Minimizes storage and transmission costs by eliminating duplicate data.
• Edge-based caching: Reduces model download times by up to 8.8 times compared to cloud-based retrieval.
• Seamless integration with serverless platforms: Supports various ML frameworks and transparently manages model layer composition and storage.

The project leverages Kubernetes for container orchestration, OpenWhisk for serverless function execution, and MinIO for object storage, providing a robust, scalable solution for deploying ML models in resource-constrained edge environments.
-->
### Contributing

Feel free to submit issues or pull requests if you find any bugs or want to propose new features. Contributions are welcome!
