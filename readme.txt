TODO:
Home page stat request.


API:
/users generic user interface

HR
/business - business profile (veiw/edit)
/business/members - business employees (business id from login)
/business/users - clients of business (business id from login)


Facility Queue
/facility/queue - get queue
/facility/queue/{businessId} - put self (user) on queue
/facility/queue/{userid}/grant - allow/decline acess

/console/businesses - list/add/delete business
/console/businesses/${businessId}/members - business employees
/console/users - clients of business


admin - business id == -1
one employee can have only one assotiated businees login

swagger:
http://localhost:5000/api/ui/
http://localhost:5000/api/


setup
from apispec
python3 -m venv venv
. venv/bin/activate
pip install six swagger_py_codegen


from srproject apispec:. ./venv/bin/activate
merge_yaml.py
swagger_py_codegen -s ./swagger.yaml .
merge src/pciapi/api apispec/v1 (schemas, routes etx)


Tables:
facility
facilitytype: 1-client, 2-facility, 3-testfacility
userfacility: binds user and facility's activation request

userfacilitytestaccess: request for facility to access user test status
    This is effectively list of facility emploees or just users who give
    fcility permanent acess to their status (untill declined)

customerqueu - access to facility request (line in the office etc)