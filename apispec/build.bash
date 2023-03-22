 rm -rf swagger.yaml v1 api/*
 . venv/bin/activate
 ./merge_yaml.py
 swagger_py_codegen -s ./swagger.yaml .
rm  -f __init__.py
