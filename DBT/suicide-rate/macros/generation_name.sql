{% macro description_generation(agegroup) -%}
    case {{ agegroup }}
        when '0-14 years' then	'Generation Alpha'
        when '15-24 years' then	'Generation Z'
        when '25-34 years' then 'Millennials'
        when '35-54 years' then	'Generation X'
        when '55-74 years' then	'Baby Boomers'
        when '75+ years' then 'Silent Generation'
        when 'Unknown'then 'Unknown'
        else 'Unknown'
    end
{%- endmacro %}
