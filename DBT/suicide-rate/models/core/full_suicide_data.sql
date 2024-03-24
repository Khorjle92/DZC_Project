{{ 
    config(
        materialized='table'
    )
}}

with suicidedata as (
    select * 
    from {{ ref("stg_staging__suicide_data")}}
),
dim_country as (
    select * 
    from {{ ref("country")}}
),
dim_countrycode as (
    select *
    from {{ ref("countrycode")}}
),
dim_population as (
    select * 
    from {{ ref("population")}}
)






SELECT
    r.RegionCode,
    s.Year,
    s.Sex,
    s.AgeGroup,
    s.Generation,
    s.SuicideCount,
    s.CauseSpecificDeathPercentage,
    s.DeathRatePer100K,
    s.CountryName,
    r.RegionName,
    p.Population
    
FROM
    suicidedata s
INNER JOIN
    dim_countrycode r ON s.countrycode = r.countrycode
LEFT JOIN
    dim_population p ON s.countrycode = p.countrycode AND s.Year = p.Year 
