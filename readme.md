# Example of Python sqlalchemy

## Summary

- MySQL [Error Code: 2013] occurs when a Python sqlalchemy connection exceeds the MySQL wait_timeout.

## Detail

### 1. Error case

![error case](/readme_image/01_mysql_2013_error.png)

### 2. Fix case

![fix case](/readme_image/02_mysql_2013_fix.png)

## How to use
```bash
# Stop & delete docker container
docker stop test_mysql
docker rm test_mysql
# Build container
docker build . -t test_mysql:1.0
# Run containe
docker run --name test_mysql -p 33067:3306 -h localhost test_mysql:1.0

# Install python package
pip install -r requirements.txt
# Run python and see error!
python code/test_01_simple_sqlalchemy.py
python code/test_02_example_class.py
```