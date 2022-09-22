*** Settings ***
Library  ../../resourses/Planets.py


*** Test Cases ***
Get planet from list
    ${res}=  Get Planet  10
    #Please note that I verify just a few fileds becaus this is a test project
    Should Be Equal  ${res['name']}  Yavin IV
    Should Be Equal  ${res['population']}  1000
    Should Be Equal  ${res['rotation_period']}  24
    Should Be Equal  ${res['surface_water']}  8

Get non existing planet
    ${res}=  Get Planet  555  expected_code=404
    Should Contain  ${res}  Planet with ID=555 is not found

Get planet with invalid id
    ${res}=  Get Planet  one  expected_code=400
    Should Contain  ${res}  Planet ID should be positive integer
