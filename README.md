# DZC_Project

This project aims to create a dashboard for analysis on the social-economical factors that could possibly affect the suicide rates amongst the population in different countries. The analysis is also detailed down to the different generations of people based on their age group.


## Table of Contents

- [SettingUp](#settingup)
- [Usage](#usage)
- [Features](#features)


## SettingUp
Instructions for installing or setting up the project. 

1) Git Clone this repo

2) Google Cloud - Cloud  
1- Go to IAM and download your Terraform IAM service account json file and save under Terraform/keys as my-creds.json  
2- Go to IAM and donwload your Mage IAM service account json file and save as your-gcp-mage.json under Mage  
3- Go to IAM and download your DBT IAM service accont json (for DBT Cloud) as your-gcp-dbt.json
Sample of roles is shown below  

![IAM roles](/Images/roles-gcp.JPG)


3) Terraform - IaC  
1- Edit the Project Name in variables.tf to your own GCP Project Name  
2- Save your GCP Terraform IAM service account json under Terraform/keys as my-creds.json  
3- Open a terminal and run terraform apply to get the set up in action  
4- Check that the bucket is created in Google Cloud Storage  



4) DBT - Cloud
1- Create a new project and sync up to this repo that you have cloned 



## Usage

Ensure Terraform-IaC steps are done before continuation  

1) Mage
- Go to the directory of Mage and docker-compose up.
- Go to localhost:6789
- Run pipeline loading_local_data_to_cloud  
- Go 

![Mage UI](/Images/mage-pipeline-ui.jpg)

The pipeline consists of 4 blocks  
First - Load Local CSV file  
Second - Export csv file to parquet file in GCS  
Third - Load the parquet file in GCS  
Fourth - Export the file to GCP  

![Mage Pipeline](/Images/mage-pipeline.jpg)

2) GCP
- Verify suicide_data are uploaded to your Google Cloud Storage bucket and in BQ

3) DBT - Cloud
- Run dbt built or deploy a job to run the project  

![DBT Lineage](/Images/dbt-lineage.jpg)

Staging - suicide_data  
Seed - country, countrycode, population, country_social_economic_year  
Macro- generation_name.sql is used to label the age group to their respective generation name according to [USC Research Library Guides](https://libguides.usc.edu/busdem/age#:~:text=The%20Baby%20Boomer%20Generation%20%E2%80%93%20born,Z%20%E2%80%93%20born%201995%2D2012)

4) GCP
- Verify that in BQ under the dataset your named in DBT project details during sync up, the tables are created and most importantly full_suicide_data.

Feel free to use the full_suicide_data on any BI tools. For me, I downloaded the dataset and used Tableau Public for my analysis.

## Features

- Feature 1
- Feature 2
- ...



