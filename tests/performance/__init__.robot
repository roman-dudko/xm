*** Settings ***
Library  Process
Suite Setup  Start Fake Application
Suite Teardown  Stop Fake Application


*** Keywords ***
Start Fake Application
    ${process}=  Start Process   python  app/fake_app.py
    Set Suite Variable  ${process}
    Sleep  5s

Stop Fake Application
    Terminate Process  ${process}