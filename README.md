# DZC_Project

This project aims to create a dashboard for basic analysis on the suicide rates in different countries. 
The aim is to identify the most critical target group to carry out awareness and counselling campign for them.
The dataset consists of the suicide data obtained from various countries from 1990 to 2022. 


## Table of Contents

- [SettingUp](#settingup)
- [Usage](#usage)
- [Dashboard](#dashboard)


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

![DBT Lineage](/Images/dbt-lineage2.jpg)

Staging - suicide_data  
Seed - country, countrycode, population  
Macro- generation_name.sql is used to label the age group to their respective generation name according to [USC Research Library Guides](https://libguides.usc.edu/busdem/age#:~:text=The%20Baby%20Boomer%20Generation%20%E2%80%93%20born,Z%20%E2%80%93%20born%201995%2D2012)

4) GCP
- Verify that in BQ under the dataset your named in DBT project details during sync up, the tables are created and most importantly full_suicide_data.

Feel free to use the full_suicide_data on any BI tools. For me, I downloaded the dataset and used Tableau Public for my analysis.

If you need to download the dataset, you can find it in Dataset folder.

## Dashboard  

![Dashboard](/Images/full-dashboard.JPG)

Analysis:  
Summing up over the years from 1990 to 2022, the country that has the highest suicide count is Russia. 
Regionally, Europe has the highest suicide count, followed by Asia. Although North America and the Caribbean is ranked 3rd in the suicide count regionally, it is noted that USA is ranked 2nd for the highest suicide count based on Country. 

By looking at the Suicide Distribution by Region, we can identify the top highest suicide count country for each region.   
Africa - South Africa  
Asia - Japan  
Central and South America - Brazil  
Europe - Russia  
North America and the Caribbean - USA  
Oceania - Australia  

Overall, the suicide rate is generally showing a decline over the years, with significant drop from 2021 onwards. This is a good sign, perhaps people are treasuring themselves more after going through the Covid period. However, it is interesting to note that while in general the suicide rates have declined over the years, the suicide rate for USA has increased over the years.

From the line chart, it is apparent that the suicide count for Male is much larger than that of the Female. 

Also, by Age group, the Generation X (35-54 years old) holds the highest suicide count and is apparent throughout the regions as well.

In summary, the most vulnerable group in general is the Male from the Generation X (35-54 years old), and perhaps especially in the USA. More effort and emphasis should be placed on this target group with the aim to reduce the suicide count as much as possible. Authorities and Social Groups can reach out to them by having more awareness campaign to understand them better and hope to resolve their problems before they choose suicide as their option.


P.S You can also play around with the dashboard to see the counts and distribution in different year by making use of the filter on the top right.

[Click to visit the dashboard on Tableau Public](https://public.tableau.com/app/profile/eugene6791/viz/SuicideCount/Dashboard1?publish=yes)