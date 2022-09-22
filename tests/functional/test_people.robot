*** Settings ***
Library  ../../resourses/People.py


*** Test Cases ***
Get person from list
    ${res}=  Get Person  45
    #Please note that I verify just a few fileds becaus this is a test project
    Should Be Equal  ${res['birth_year']}  19BBY
    Should Be Equal  ${res['eye_color']}  blue
    Should Be Equal  ${res['gender']}  male
    Should Be Equal  ${res['hair_color']}  blond

Get non existing person
    ${res}=  Get Person  101  expected_code=404
    Should Contain  ${res}  Person with ID=101 is not found

Get person with invalid id
    ${res}=  Get Person  test  expected_code=400
    Should Contain  ${res}  Person ID should be positive integer
