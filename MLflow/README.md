# MLflow Virtual Environment Setup Guide

---

## 🚀 Quick Start

1. **Create Virtual Environment:** 
   ```bash
   conda create -n mlflow-venv python=3.10

2. **Activate Virtual Environment:**
    ```bash
    conda activate mlflow-venv

3. **Install MLflow:**
    ```bash
    pip install mlflow 

4. **Verify Installation:**
    ```bash
    mlflow 

5. **MLflow UI:**
    ```bash
    mlflow ui

## 🚀 **MLflow Tracking:**

1. `mlflow.set_tracking_uri()`: Sets the URI (Uniform Resource Identifier) for the MLflow tracking server, which is used to log and query experiments and runs.

2. `mlflow.get_tracking_uri()`: Retrieves the URI of the MLflow tracking server currently set in the environment.

3. `mlflow.create_experiment()`: Creates a new experiment in the MLflow tracking server. Experiments are containers for runs, where each run represents a specific execution of code.

4. `mlflow.set_experiment()`: Sets the active experiment for the current session. Subsequent runs will be associated with this experiment until another experiment is set.

5. `mlflow.start_run()`: Starts a new MLflow run within the active experiment. This function is typically called at the beginning of a script or function to track the execution and parameters of the code.

6. `mlflow.log_param()`: Logs a parameter value to the active MLflow run.

7. `mlflow.log_metric()`: Logs a metric value to the active MLflow run.

8. `mlflow.log_artifact()`: Logs an artifact file (e.g., model file, image) to the active MLflow run.

9. `mlflow.end_run()`: Ends the active MLflow run. This function is typically called at the end of a script or function to signify the completion of the run.

10. `mlflow.active_run()`: Retrieves the active MLflow run, if one exists. This function is useful for accessing run-specific information within the code.

11. `mlflow.get_experiment_by_name()`: Retrieves an experiment by its name from the MLflow tracking server.

12. `mlflow.delete_run()`: Deletes a run with the specified run ID from the MLflow tracking server.

13. `mlflow.delete_experiment()`: Deletes an experiment with the specified experiment ID from the MLflow tracking server.

14. `mlflow.list_experiments()`: Lists all experiments available in the MLflow tracking server.

15. `mlflow.list_run_infos()`: Lists run information (e.g., run ID, status, start time) for runs in the specified experiment.

16. `mlflow.search_runs()`: Searches for runs that match the specified filter criteria.

17. `mlflow.search_projects()`: Searches for projects that match the specified filter criteria.

