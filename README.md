================================================================================================
#PYSPARK SAMPLE PROJECT
================================================================================================

Overview:

This sample project ingests data from a Web Api. The data ingested is flattened and is saved as csv. Also, the data is loaded into a postgres RDBMS table. To parameterize the code config.json file is used for many values that otherwise would be hard-coded. Following is the structure of the App.

app/
 |-- config.json
 |-- jobs/
 |   |-- transform.py
 |-- main.py
 |-- tests/
 |   |-- test_file.json (optional)
 |   |-- test_etl_job.py (optional)
 |-- build_dependencies.sh (optional)
 
 
 =============================================
 #CONFIG JSON
 =============================================
 
 This json file contains values for different parameters such as Application_Name, Source URL, Target CSV path and Postgres DB details.
 
 =============================================
 #TRANSFORM.PY
 =============================================
 
 This .py file contains 3 functions:
 
	-extract_data() - This function is used to extract the data from the web api.
	-transform_data() - This function is used to flatten the hierarchichal data extracted from web api.
	-load_data() - This function is used to save the data as CSV format. Also, the data is loaded into Postgres RDBMS.
	
	
==============================================
#MAIN.PY
==============================================

This is the main .py file where spark session is initialized. Also, config file is read. Moreover, a function _parse_arguments is created to take input from the spark-submit command line enabling the job to know which .py file to execute(Note: This is more handy when we have multiple .py jobs to be scheduled within one main.py)

==============================================
#BUILD_DEPENDENCIES.sh
==============================================

This is a shell script which could be used to setup the environment suitable for the app to execute. In case, some modules is to be installed, it could be done in this script. We can use this script to run our unit test by executing test_etl_job.py using pytest. This can also be used to zip jobs in a zipped file which could be passed as values to --py-files parameter while executing the job using spark-submit.

==============================================
#TEST_ETL_JOB.PY
==============================================

This is a .py job used to unit test the job end to end. The .py will import pandas to assert the final results of the job and expected results. test_file.json is to be used to source in the data and run against the jobs.transform.py.
