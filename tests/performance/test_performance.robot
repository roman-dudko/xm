*** Settings ***
Library  ../../resourses/People.py
Library  ../../resourses/get_statistics.py

Library  Collections


*** Test Cases ***
Test People endpoint performance
    ${response_results}=  Create List
    ${current_time}=  Get Time  epoch
    ${run_time}=  Get Variable Value  ${testing_time}  60
    ${end_time}=  Evaluate  ${current_time}+${run_time}
    WHILE  ${current_time}<${end_time}
        ${response}=  Get Person  5  get_response_obj=${True}
        ${response_time}=  Evaluate  ${response.elapsed.microseconds}/1000
        Append To List  ${response_results}  ${response_time}
        ${current_time}=  Get Time  epoch
    END
    ${mean}=  Get Mean  ${response_results}
    ${stdev}=  Get Stdev  ${response_results}
    Log To Console  Performance test results: response time mean = ${mean}, standard deviation = ${stdev}