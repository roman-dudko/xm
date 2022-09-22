*** Settings ***
Library  ../../resourses/Starships.py


*** Test Cases ***
Get starship from list
    ${res}=  Get Starship  77
    #Please note that I verify just a few fileds becaus this is a test project
    Should Be Equal  ${res['name']}  Death Star
    Should Be Equal  ${res['MGLT']}  10
    Should Be Equal  ${res['starship_class']}  Deep Space Mobile Battlestation
    Should Be Equal  ${res['consumables']}  3 years

Get non starship planet
    ${res}=  Get Starship  107  expected_code=404
    Should Contain  ${res}  Starship with ID=107 is not found

Get starship with invalid id
    ${res}=  Get Starship  hi  expected_code=400
    Should Contain  ${res}  Starship ID should be positive integer
