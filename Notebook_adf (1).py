# Databricks notebook source
pip install powerbiclient

# COMMAND ----------

# Import the DeviceCodeLoginAuthentication class to authenticate against Power BI
from powerbiclient.authentication import DeviceCodeLoginAuthentication

# Initiate device authentication
device_auth = DeviceCodeLoginAuthentication()

# COMMAND ----------

group_id="Workspace ID"
report_id="Report ID"

# COMMAND ----------

report = Report(group_id=group_id, report_id=report_id, auth=device_auth)

report
