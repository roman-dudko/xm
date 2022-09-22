# Technical task for XM
Download project, create venv and install requirements:
``` bash
pip install -r requirements.txt
```

## Functional testsuite
For functional tests execution run command:
``` bash
robot -d results tests/functional
```
Robot Framework report and log will be stored in 'results' folder

## Performance test
"People" endpoint is modified to return response with random delay 0-999ms.

For performance test run command:
``` bash
robot -d results -v testing_time:90 tests/performance
```
'testing_time' variable is optional and indicates testing time in seconds. By default test is executed for 60 sec.

Response time mean and standard deviation are logged to console during test execution and also can be found in ${mean} and ${stdev} variables in Robot test log.