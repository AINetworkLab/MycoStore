# Re2po

A Distributed Redundancy-aware Model Repository in Edge Serverless Computing

---

## 1. **docker-compose.yml**

A Docker Compose configuration file used to define and start services, including containerized components.

---

## 2. **gateway/**

This directory includes scripts and utilities for model management, data processing, and interaction with MinIO storage.

| **File**                      | **Description**                                           |
| ----------------------------- | --------------------------------------------------------- |
| `data_dao.py`                 | Data Access Object (DAO) layer for handling data storage. |
| `entity.py`                   | Entity definitions for data models.                       |
| `find_common_items.py`        | Utility to find common elements across datasets.          |
| `main.py`                     | Entry point script for the gateway module.                |
| `minio_service.py`            | Interface to interact with MinIO services.                |
| `minio_utils.py`              | Helper functions for MinIO operations.                    |
| `model_compose.py`            | Model composition and integration functions.              |
| `model_compose_tf.py`         | TensorFlow-specific model composition utilities.          |
| `model_dao.py`                | DAO layer for managing model storage.                     |
| `model_save.py`               | Script to save model files.                               |
| `model_save_tf.py`            | TensorFlow-specific model saving utilities.               |
| `ow-load.py`                  | Script for OpenWhisk model loading.                       |
| `ow_test.py`                  | OpenWhisk test script.                                    |
| `safetensor2torch_all.py`     | Convert all safetensors to PyTorch-compatible formats.    |
| `safetensors2torch_single.py` | Convert a single safetensor to PyTorch format.            |
| `storage_dao.py`              | DAO for handling storage operations.                      |
| `temp_dir.py`                 | Temporary directory management utilities.                 |

---

## 3. **openwhisk-deploy-kube/**

This directory contains scripts and configurations for deploying OpenWhisk on Kubernetes.

### **deploy/**

- **`kind/`**: Configuration files for setting up a Kubernetes cluster using Kind.
  - `kind-cluster.yaml`, `kind-cluster-2.yaml`: Kind cluster definitions.
  - `start-kind.sh`, `start-kind-2.sh`: Scripts to start Kind clusters.
- **`mycluster.yaml`**: Custom cluster configuration.

### **helm/openwhisk/**

Helm chart for deploying OpenWhisk components with Kubernetes.

| **File/Directory** | **Description**                                            |
| ------------------ | ---------------------------------------------------------- |
| `Chart.yaml`       | Helm chart metadata.                                       |
| `configMapFiles/`  | Scripts and configurations for initialization and testing. |
| `templates/`       | Kubernetes manifest templates for various components.      |
| `runtimes.json`    | Definitions for supported runtimes.                        |
| `values.yaml`      | Default values for Helm chart customization.               |
| `README.md`        | Documentation for the Helm chart.                          |
| `LICENSE`          | License information.                                       |

### **test_node/**

Scripts for testing and validating various operations.

| **File**                  | **Description**                        |
| ------------------------- | -------------------------------------- |
| `download.py`             | Download utility script.               |
| `model_inference.py`      | Script to perform model inference.     |
| `model_inference_test.py` | Test script for model inference.       |
| `openwhisk_minio.py`      | Integrate OpenWhisk with MinIO.        |
| `send_file.py`            | Script to send files.                  |
| `send_minio.py`           | Upload data to MinIO storage.          |
| `test.ipynb`              | Jupyter Notebook for testing purposes. |
| `upload2minio.py`         | Script to upload files to MinIO.       |

---

## 4. **README.md**

This file provides an overview of the project structure and its components.

---

## Summary

This project integrates multiple services and tools for efficient model management, Kubernetes-based container orchestration, and OpenWhisk deployment.

### Key Components:

- **Gateway**: For data access, model management, and MinIO interactions.
- **OpenWhisk Deployment**: Kubernetes-based deployment scripts using Helm.
- **Testing and Validation**: Scripts for testing model inference and storage functionalities.
