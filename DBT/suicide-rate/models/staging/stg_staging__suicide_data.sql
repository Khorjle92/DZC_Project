with 

source as (

    select * from {{ source('staging', 'suicide_data') }}

),

renamed as (

    select
        countrycode,
        countryname,
        year,
        sex,
        agegroup,
        {{ description_generation('agegroup') }} as generation,
        suicidecount,
        causespecificdeathpercentage,
        deathrateper100k

    from source
    where agegroup != 'Unknown'    
)

select * from renamed
