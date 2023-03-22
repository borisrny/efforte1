# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
# TODO: datetime support

class RefNode(object):

    def __init__(self, data, ref):
        self.ref = ref
        self._data = data

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __getattr__(self, key):
        return self._data.__getattribute__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return repr({'$ref': self.ref})

    def __eq__(self, other):
        if isinstance(other, RefNode):
            return self._data == other._data and self.ref == other.ref
        elif six.PY2:
            return object.__eq__(other)
        elif six.PY3:
            return object.__eq__(self, other)
        else:
            return False

    def __deepcopy__(self, memo):
        return RefNode(copy.deepcopy(self._data), self.ref)

    def copy(self):
        return RefNode(self._data, self.ref)

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/api'

definitions = {'definitions': {'About': {'properties': {'contact': {'type': 'string'}, 'name': {'type': 'string'}}, 'type': 'object'}, 'AcceptBusiness': {'properties': {'token': {'type': 'string'}}, 'type': 'object'}, 'AcceptBusinessItem': {'properties': {'id': {'type': 'integer'}, 'name': {'type': 'string'}, 'status': {'type': 'string'}}, 'type': 'object'}, 'AcceptBusinessList': {'items': {'$ref': '#/definitions/AcceptBusinessItem'}, 'type': 'array'}, 'Address': {'properties': {'city': {'type': 'string'}, 'country': {'type': 'string'}, 'county': {'type': 'string'}, 'postal': {'type': 'string'}, 'state': {'type': 'string'}, 'street1': {'type': 'string'}, 'street2': {'type': 'string'}}, 'type': 'object'}, 'AuthChangePassword': {'properties': {'newPassword': {'type': 'string'}, 'oldPassword': {'type': 'string'}}, 'type': 'object'}, 'AuthChangePasswordResp': {'properties': {'status': {'type': 'string'}}, 'type': 'object'}, 'AuthForgotPassword': {'properties': {'email': {'type': 'string'}}, 'type': 'object'}, 'AuthResponse': {'properties': {'token': {'type': 'string'}}, 'type': 'object'}, 'Business': {'allOf': [{'$ref': '#/definitions/Address'}, {'properties': {'description': {'type': 'string'}, 'email': {'type': 'string'}, 'id': {'type': 'integer'}, 'latitude': {'type': 'number'}, 'longitude': {'type': 'number'}, 'name': {'type': 'string'}, 'phone_number': {'type': 'string'}}, 'type': 'object'}]}, 'Businesses': {'items': {'$ref': '#/definitions/Business'}, 'type': 'array'}, 'BussinessAccessRequirements': {'properties': {'covidTest': {'$ref': '#/definitions/COVIDTestRequirements'}, 'questionnaireRequirements': {'$ref': '#/definitions/QuestionnaireRequirements'}, 'vitalRequirements': {'$ref': '#/definitions/VitalsRequirements'}}, 'type': 'object'}, 'COVIDTest': {'properties': {'date_of_test': {'example': '03-13-2019', 'type': 'string'}, 'id': {'type': 'number'}, 'igg': {'type': 'boolean'}, 'igm': {'type': 'boolean'}, 'overall_status': {'type': 'boolean'}, 'picture': {'required': False, 'type': 'binary'}, 'pictureURL': {'required': False, 'type': 'string'}, 'requisition': {'required': False, 'type': 'binary'}, 'requisitionTestURL': {'required': False, 'type': 'string'}, 'viral_ag_load': {'type': 'boolean'}}, 'type': 'object'}, 'COVIDTestRequirements': {'allOf': [{'$ref': '#/definitions/COVIDTest'}, {'properties': {'number_of_positives': {'type': 'integer'}, 'valid_days': {'type': 'integer'}}, 'type': 'object'}]}, 'COVIDTests': {'items': {'$ref': '#/definitions/COVIDTest'}, 'type': 'array'}, 'FacilityQueueAddResp': {'items': {'$ref': '#/definitions/FacilityQueueAddRespNode'}, 'type': 'array'}, 'FacilityQueueAddRespNode': {'properties': {'id': {'type': 'integer'}, 'status': {'type': 'boolean'}}, 'type': 'object'}, 'FacilityQueueItem': {'properties': {'access_status': {'type': 'integer'}, 'facilityid': {'type': 'integer'}, 'related': {'type': 'integer'}, 'time_in': {'type': 'string'}, 'time_out': {'type': 'string'}, 'time_requested': {'type': 'string'}, 'userid': {'type': 'integer'}}, 'type': 'object'}, 'FacilityQueueUser': {'properties': {'covidTest': {'$ref': '#/definitions/COVIDTest'}, 'questionnaire': {'$ref': '#/definitions/Questionnaire'}, 'queueItem': {'$ref': '#/definitions/FacilityQueueItem'}, 'requirementsMatch': {'type': 'boolean'}, 'user': {'$ref': '#/definitions/User'}, 'vitals': {'$ref': '#/definitions/Vitals'}}, 'type': 'object'}, 'FacilityQueueUsers': {'items': {'$ref': '#/definitions/FacilityQueueUser'}, 'type': 'array'}, 'HIPPAParams': {'properties': {'sendEmail': {'type': 'boolean'}, 'ssn': {'type': 'string'}}, 'type': 'object'}, 'HIPPAText': {'properties': {'ssn': {'type': 'string'}, 'text': {'type': 'string'}}, 'type': 'object'}, 'IDs': {'items': {'type': 'integer'}, 'type': 'array'}, 'LoginDescription': {'properties': {'companyName': {'type': 'string'}, 'firstName': {'type': 'string'}, 'lastName': {'type': 'string'}, 'username': {'type': 'string'}}, 'type': 'object'}, 'Notification': {'properties': {'id': {'type': 'integer'}, 'postdate': {'example': '03-13-2019', 'type': 'string'}, 'postername': {'type': 'string'}, 'text': {'type': 'string'}, 'title': {'type': 'string'}}, 'type': 'object'}, 'Notifications': {'items': {'$ref': '#/definitions/Notification'}, 'type': 'array'}, 'ProfileAccess': {'properties': {'accesCode': {'enum': ['Allow', 'Decline', 'Suspend', 'Delete'], 'type': 'string'}, 'id': {'description': 'company ID', 'type': 'integer'}, 'name': {'description': 'company name', 'type': 'string'}}, 'type': 'object'}, 'ProfileAccessList': {'items': {'$ref': '#/definitions/ProfileAccess'}, 'type': 'array'}, 'Questionnaire': {'properties': {'aches_pains': {'type': 'boolean'}, 'cough': {'type': 'boolean'}, 'diarrhea': {'type': 'boolean'}, 'fatigue': {'type': 'boolean'}, 'fever': {'type': 'boolean'}, 'headache': {'type': 'boolean'}, 'id': {'type': 'number'}, 'loss_of_taste': {'type': 'boolean'}, 'nausea_vomiting': {'type': 'boolean'}, 'postdate': {'example': '03-13-2019', 'type': 'string'}, 'runny_nose': {'type': 'boolean'}, 'shortnes_of_breath': {'type': 'boolean'}, 'sneezing': {'type': 'boolean'}, 'sore_throat': {'type': 'boolean'}}, 'type': 'object'}, 'QuestionnaireRequirements': {'allOf': [{'$ref': '#/definitions/Questionnaire'}, {'properties': {'number_of_positives': {'type': 'integer'}, 'valid_hours': {'type': 'integer'}}, 'type': 'object'}]}, 'Questionnaires': {'items': {'$ref': '#/definitions/Questionnaire'}, 'type': 'array'}, 'Registration': {'allOf': [{'$ref': '#/definitions/User'}, {'properties': {'password': {'type': 'string'}, 'username': {'type': 'string'}}, 'type': 'object'}]}, 'Role': {'properties': {'id': {'type': 'integer'}, 'name': {'type': 'string'}}, 'type': 'object'}, 'Roles': {'items': {'$ref': '#/definitions/Role'}, 'type': 'array'}, 'TestsSummary': {'properties': {'covidtestDate': {'type': 'string'}, 'covidtestExpDate': {'type': 'string'}, 'questionnairyDate': {'type': 'string'}, 'questionnairyExpDate': {'type': 'string'}, 'userId': {'type': 'number'}}, 'type': 'object'}, 'TestsSummaryList': {'items': {'$ref': '#/definitions/TestsSummary'}, 'type': 'array'}, 'User': {'allOf': [{'$ref': '#/definitions/Address'}, {'properties': {'avatar': {'required': False, 'type': 'string'}, 'dob': {'example': '03-13-2019', 'type': 'string'}, 'email': {'type': 'string'}, 'first_name': {'type': 'string'}, 'id': {'type': 'integer'}, 'last_name': {'type': 'string'}, 'phone_number': {'type': 'string'}, 'roles': {'items': {'type': 'integer'}, 'type': 'array'}, 'ssn': {'example': '111-11-1111', 'required': False, 'type': 'string'}, 'username': {'type': 'string'}}, 'type': 'object'}]}, 'UserActivation': {'allOf': [{'$ref': '#/definitions/User'}, {'properties': {'activationstatus': {'type': 'integer'}}, 'type': 'object'}]}, 'UserList': {'items': {'$ref': '#/definitions/User'}, 'type': 'array'}, 'UserRelated': {'allOf': [{'$ref': '#/definitions/UserUpdate'}, {'properties': {'relationReason': {'type': 'string'}}, 'type': 'object'}]}, 'UserRelatedList': {'items': {'$ref': '#/definitions/UserRelated'}, 'type': 'array'}, 'UserUpdate': {'allOf': [{'$ref': '#/definitions/User'}, {'properties': {'profileImage': {'required': False, 'type': 'binary'}}, 'type': 'object'}]}, 'Users': {'items': {'$ref': '#/definitions/UserActivation'}, 'type': 'array'}, 'Vitals': {'properties': {'bp': {'type': 'string'}, 'id': {'type': 'number'}, 'percent': {'type': 'number'}, 'postdate': {'example': '03-13-2019', 'type': 'string'}, 'temp': {'type': 'number'}}, 'type': 'object'}, 'VitalsList': {'items': {'$ref': '#/definitions/Vitals'}, 'type': 'array'}, 'VitalsRequirements': {'allOf': [{'properties': {'bp_diastolic_h': {'type': 'number'}, 'bp_diastolic_l': {'type': 'number'}, 'bp_systolic_h': {'type': 'number'}, 'bp_systolic_l': {'type': 'number'}, 'id': {'type': 'integer'}, 'number_of_positives': {'type': 'integer'}, 'percent': {'type': 'number'}, 'temp': {'type': 'number'}, 'valid_hours': {'type': 'integer'}}, 'type': 'object'}]}}, 'parameters': {}}

validators = {
    ('business_notifications', 'GET'): {'args': {'required': [], 'properties': {'fromdate': {'default': None, 'description': 'Start Date', 'required': False, 'type': 'string'}, 'todate': {'default': None, 'description': 'end Date', 'required': False, 'type': 'string'}}}},
    ('business_notifications', 'POST'): {'json': {'$ref': '#/definitions/Notification'}},
    ('business_notifications_notifid', 'PUT'): {'json': {'$ref': '#/definitions/Notification'}},
    ('business_testrequirements', 'POST'): {'json': {'$ref': '#/definitions/BussinessAccessRequirements'}},
    ('business_testrequirements', 'PUT'): {'json': {'$ref': '#/definitions/BussinessAccessRequirements'}},
    ('business_users', 'GET'): {'args': {'required': [], 'properties': {'status': {'default': 0, 'description': '0 - all, 1 - activated, 2 - pending activation, 3 - removed', 'enum': [0, 1, 2, 3], 'type': 'integer'}, 'firstname': {'default': None, 'required': False, 'type': 'string'}, 'lastname': {'default': None, 'required': False, 'type': 'string'}}}},
    ('business_users', 'POST'): {'json': {'$ref': '#/definitions/User'}},
    ('businesses_registration', 'POST'): {'json': {'$ref': '#/definitions/Registration'}},
    ('changepassword', 'POST'): {'json': {'$ref': '#/definitions/AuthChangePassword'}},
    ('console_businesses', 'POST'): {'json': {'$ref': '#/definitions/Business'}},
    ('console_businesses_businessid', 'PUT'): {'json': {'$ref': '#/definitions/Business'}},
    ('console_businesses_businessid_members', 'POST'): {'json': {'$ref': '#/definitions/User'}},
    ('console_businesses_businessid_registration', 'POST'): {'json': {'$ref': '#/definitions/Registration'}},
    ('facilities', 'POST'): {'json': {'$ref': '#/definitions/Business'}},
    ('facilities_recid', 'PUT'): {'json': {'$ref': '#/definitions/Business'}},
    ('facility_queue_facilityId', 'POST'): {'json': {'$ref': '#/definitions/IDs'}},
    ('facility_queue_userId_grant', 'PUT'): {'args': {'required': ['status'], 'properties': {'status': {'description': 'grant (true)/decline (false) access', 'schema': {'type': 'boolean'}}}}},
    ('forgotpassword', 'POST'): {'json': {'$ref': '#/definitions/AuthForgotPassword'}},
    ('loadtest_vitals_userKey_facilityId', 'POST'): {'json': {'$ref': '#/definitions/Vitals'}},
    ('notifications', 'POST'): {'json': {'$ref': '#/definitions/Notification'}},
    ('registration', 'POST'): {'json': {'$ref': '#/definitions/Registration'}},
    ('roles', 'POST'): {'json': {'$ref': '#/definitions/Role'}},
    ('testfacilities', 'POST'): {'json': {'$ref': '#/definitions/Business'}},
    ('testfacilities_recid', 'PUT'): {'json': {'$ref': '#/definitions/Business'}},
    ('testfacility_patients_userId_covid', 'POST'): {'json': {'$ref': '#/definitions/COVIDTest'}},
    ('testfacility_patients_userId_vitals', 'POST'): {'json': {'$ref': '#/definitions/Vitals'}},
    ('users', 'POST'): {'json': {'$ref': '#/definitions/User'}},
    ('users_covidtest', 'POST'): {'json': {'$ref': '#/definitions/COVIDTest'}},
    ('users_questionnaires', 'POST'): {'json': {'$ref': '#/definitions/Questionnaire'}},
    ('users_self', 'PUT'): {'json': {'$ref': '#/definitions/UserUpdate'}},
    ('users_self_acceptbusiness', 'PUT'): {'json': {'$ref': '#/definitions/AcceptBusiness'}},
    ('users_self_covidtest', 'POST'): {'json': {'$ref': '#/definitions/COVIDTest'}},
    ('users_self_covidtest_testId', 'PUT'): {'json': {'$ref': '#/definitions/COVIDTest'}},
    ('users_self_hippa', 'POST'): {'json': {'$ref': '#/definitions/HIPPAParams'}},
    ('users_self_image', 'POST'): {'form': {'required': [], 'properties': {'avatar': {'description': 'The file to upload.', 'type': 'file'}}}},
    ('users_self_profileaccess_companyId', 'PUT'): {'json': {'$ref': '#/definitions/ProfileAccess'}},
    ('users_self_questionnaire', 'POST'): {'json': {'$ref': '#/definitions/Questionnaire'}},
    ('users_self_related', 'POST'): {'json': {'$ref': '#/definitions/UserRelated'}},
    ('users_self_related_userid', 'PUT'): {'json': {'$ref': '#/definitions/UserRelated'}},
    ('users_self_related_userid_covidtest', 'POST'): {'json': {'$ref': '#/definitions/COVIDTest'}},
    ('users_self_related_userid_covidtest_testId', 'PUT'): {'json': {'$ref': '#/definitions/COVIDTest'}},
    ('users_self_related_userid_hippa', 'POST'): {'json': {'$ref': '#/definitions/HIPPAParams'}},
    ('users_self_related_userid_questionnaire', 'POST'): {'json': {'$ref': '#/definitions/Questionnaire'}},
    ('users_self_related_userid_vitals', 'POST'): {'json': {'$ref': '#/definitions/Vitals'}},
    ('users_self_vitals', 'POST'): {'json': {'$ref': '#/definitions/Vitals'}},
    ('users_vitals', 'POST'): {'json': {'$ref': '#/definitions/Vitals'}},
    ('users_userid', 'PUT'): {'json': {'$ref': '#/definitions/User'}},
}

filters = {
    ('about', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/About'}}},
    ('auth', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/AuthResponse'}}},
    ('business_notifications', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Notifications'}}},
    ('business_notifications', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Notification'}}},
    ('business_notifications_notifid', 'DELETE'): {200: {'headers': None, 'schema': None}},
    ('business_notifications_notifid', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Notification'}}},
    ('business_notifications_notifid', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Notification'}}},
    ('business_qrcode', 'GET'): {200: {'headers': None, 'schema': {'type': 'string'}}},
    ('business_qrcode', 'POST'): {200: {'headers': None, 'schema': {'type': 'string'}}},
    ('business_testrequirements', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/BussinessAccessRequirements'}}},
    ('business_testrequirements', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/BussinessAccessRequirements'}}},
    ('business_testrequirements', 'PUT'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/BussinessAccessRequirements'}}},
    ('business_users', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Users'}}},
    ('business_users', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('business_users_health', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/FacilityQueueUsers'}}},
    ('business_users_queureport', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/FacilityQueueUsers'}}},
    ('business_users_userid', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('business_users_userid', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('business_users_userid_invite', 'POST'): {200: {'headers': None, 'schema': None}},
    ('business_users_userid_suspend', 'POST'): {200: {'headers': None, 'schema': None}},
    ('businesses_registration', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('changepassword', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/AuthChangePasswordResp'}}},
    ('console_businesses', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Businesses'}}},
    ('console_businesses', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Business'}}},
    ('console_businesses_businessid', 'DELETE'): {200: {'headers': None, 'schema': None}},
    ('console_businesses_businessid', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Business'}}},
    ('console_businesses_businessid', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Business'}}},
    ('console_businesses_businessid_members', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Users'}}},
    ('console_businesses_businessid_members', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('console_businesses_businessid_members_memberid', 'DELETE'): {200: {'headers': None, 'schema': None}},
    ('console_businesses_businessid_registration', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('covidtest_current', 'GET'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTest'}}},
    ('facilities', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Businesses'}}},
    ('facilities', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Business'}}},
    ('facilities_recid', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Business'}}},
    ('facility_queue', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/FacilityQueueUsers'}}},
    ('facility_queue_facilityId', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/FacilityQueueAddResp'}}},
    ('facility_queue_userId_grant', 'PUT'): {200: {'headers': None, 'schema': None}},
    ('forgotpassword', 'POST'): {200: {'headers': None, 'schema': None}},
    ('loadtest_vitals_userKey_facilityId', 'POST'): {201: {'headers': None, 'schema': None}},
    ('notifications', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Notifications'}}},
    ('notifications', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Notification'}}},
    ('ping', 'GET'): {200: {'headers': None, 'schema': None}},
    ('questionnaires_current', 'GET'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Questionnaire'}}},
    ('registration', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/AuthResponse'}}},
    ('roles', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Roles'}}},
    ('roles', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Role'}}},
    ('terms', 'GET'): {200: {'headers': None, 'schema': {'type': 'string'}}},
    ('testfacilities', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Businesses'}}},
    ('testfacilities', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Business'}}},
    ('testfacilities_recid', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Business'}}},
    ('testfacility_patients', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/UserList'}}},
    ('testfacility_patients_userId', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('testfacility_patients_userId_covid', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTests'}}},
    ('testfacility_patients_userId_covid', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTests'}}},
    ('testfacility_patients_userId_vitals', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/VitalsList'}}},
    ('testfacility_patients_userId_vitals', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Vitals'}}},
    ('users', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Users'}}},
    ('users', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('users_covidtest', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTests'}}},
    ('users_covidtest', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTests'}}},
    ('users_questionnaires', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Questionnaires'}}},
    ('users_questionnaires', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Questionnaire'}}},
    ('users_self', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('users_self', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('users_self_acceptbusiness', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/AcceptBusinessList'}}},
    ('users_self_acceptbusiness', 'PUT'): {200: {'headers': None, 'schema': None}},
    ('users_self_acceptbusiness_recordId', 'DELETE'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/AcceptBusinessList'}}},
    ('users_self_covidtest', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTest'}}},
    ('users_self_covidtest', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTest'}}},
    ('users_self_covidtest_history', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTests'}}},
    ('users_self_covidtest_testId', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTest'}}},
    ('users_self_hippa', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/HIPPAText'}}},
    ('users_self_hippa', 'POST'): {200: {'headers': None, 'schema': None}},
    ('users_self_laodtestqr', 'POST'): {201: {'headers': None, 'schema': None}},
    ('users_self_logindescription', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/LoginDescription'}}},
    ('users_self_profileaccess', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/ProfileAccessList'}}},
    ('users_self_profileaccess_companyId', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/ProfileAccessList'}}},
    ('users_self_questionnaire', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Questionnaire'}}},
    ('users_self_questionnaire', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Questionnaire'}}},
    ('users_self_related', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/UserRelatedList'}}},
    ('users_self_related', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/UserRelated'}}},
    ('users_self_related_userid', 'DELETE'): {200: {'headers': None, 'schema': None}},
    ('users_self_related_userid', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('users_self_related_userid', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/UserRelated'}}},
    ('users_self_related_userid_covidtest', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTest'}}},
    ('users_self_related_userid_covidtest', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTest'}}},
    ('users_self_related_userid_covidtest_history', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTests'}}},
    ('users_self_related_userid_covidtest_testId', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/COVIDTest'}}},
    ('users_self_related_userid_hippa', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/HIPPAText'}}},
    ('users_self_related_userid_hippa', 'POST'): {200: {'headers': None, 'schema': None}},
    ('users_self_related_userid_laodtestqr', 'POST'): {201: {'headers': None, 'schema': None}},
    ('users_self_related_userid_questionnaire', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Questionnaire'}}},
    ('users_self_related_userid_questionnaire', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Questionnaire'}}},
    ('users_self_related_userid_vitals', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/VitalsList'}}},
    ('users_self_related_userid_vitals', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Vitals'}}},
    ('users_self_teststatuses', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/TestsSummaryList'}}},
    ('users_self_vitals', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/VitalsList'}}},
    ('users_self_vitals', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Vitals'}}},
    ('users_vitals', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/VitalsList'}}},
    ('users_vitals', 'POST'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Vitals'}}},
    ('users_userid', 'DELETE'): {200: {'headers': None, 'schema': None}},
    ('users_userid', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('users_userid', 'PUT'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}},
    ('users_userid_notifications', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Notifications'}}},
    ('users_userid_notifications_notifid', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Notification'}}},
    ('vitals_current', 'GET'): {201: {'headers': None, 'schema': {'$ref': '#/definitions/Vitals'}}},
}

scopes = {
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
