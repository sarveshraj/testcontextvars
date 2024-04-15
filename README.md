This is a demo app to test [contextvars](https://docs.python.org/3/library/contextvars.html).

## API

The API is written in `views.py > test()`. 

It contains a context variable (`requestIdCtxVar`) to store the `requestId` of the request. 

For every request the API stores the `requestId` in `requestIdCtxVar` and then runs the internal functions with the context. The internal functions contain two nested calls that print the `requestId` passed as argument and from `requestIdCtxVar` to check for equality.

## Test

The test is located in `test.sh`. 

The script starts the django server and then sends 10 parallel requests to it. It routes the server logs to `logs.txt` where the equality of the `requestId` from the two sources can be compared.

## Steps:

1. Install Django: `python -m pip install Django`
2. Run test: `bash test.sh`
3. Optionally pass the number of requests to be triggered as a positional argument, e.g. `bash test.sh 5`
