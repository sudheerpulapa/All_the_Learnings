import os          # This tool helps us work with files and folders on the computer.
import mlflow      # This tool helps us track and manage our machine learning experiments.
import argparse    # This tool helps us handle special instructions given when we run the program.
import time        # This tool helps us work with time-related tasks, like measuring how long something takes.


def eval(p1, p2):
    output_metric = p1**2 + p2**2  # This function calculates a metric based on two numbers.
    return output_metric

def main(inp1, inp2):
    mlflow.set_experiment("Demo_Experiment")  # This function sets up an experiment in MLflow, a tool for managing machine learning experiments.
    with mlflow.start_run():                  # This starts a new run within the experiment.
        mlflow.set_tag("version","1.0.0")    # This adds a tag to the run, like labeling a box.
        mlflow.log_param("param1",inp1)      # This logs a parameter value to the run.
        mlflow.log_param("param2",inp2)      # This logs another parameter value to the run.
        metric = eval(p1 = inp1, p2 = inp2)  # This calculates a metric using the eval function we defined earlier.
        mlflow.log_metric("Eval_Metric",metric)  # This logs the calculated metric to the run.
        os.makedirs("dummy", exist_ok=True)  # This creates a folder called "dummy" if it doesn't exist already.
        with open("dummy/example.txt", "wt") as f:  # This opens a file within the "dummy" folder for writing.
            f.write(f"Artifact created at {time.asctime()}")  # This writes a message with the current time to the file.
        mlflow.log_artifacts("dummy")         # This logs the contents of the "dummy" folder as artifacts to the run.


if __name__ == '__main__':                    # This checks if the program is being run directly.
    args = argparse.ArgumentParser()          # This creates a tool for handling special instructions given when running the program.
    args.add_argument("--param1","-p1", type=int, default=5)  # This defines a special instruction for a parameter called param1.
    args.add_argument("--param2","-p2", type=int, default=10) # This defines another special instruction for a parameter called param2.
    parsed_args = args.parse_args()           # This reads and understands the special instructions given when running the program.
    main(parsed_args.param1, parsed_args.param2)  # This starts the main part of the program, using the special instructions provided.
