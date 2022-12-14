import json
import importlib
import argparse
from pyspark.sql import SparkSession

def _parse_arguments():
    """ Parse arguments provided by spark-submit command"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--job",required=True)
    return parser.parse_args()

def main():
    """Main function executed by spark-submit command """
    args = _parse_arguments()

    with open("config.json","r") as config_file:
        config = json.load(config_file)

        spark = SparkSession.builder\
                .appName(config.get("AppName")) \
                .getOrCreate()
        f = "jobs."+args.job
        job_module = importlib.import_module(f)
        job_module.run_job(spark, config)

if __name__ == "__main__":
    main()