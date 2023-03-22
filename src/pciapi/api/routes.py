# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.about import About
from .api.auth import Auth
from .api.business_notifications import BusinessNotifications
from .api.business_notifications_notifid import BusinessNotificationsNotifid
from .api.business_qrcode import BusinessQrcode
from .api.business_testrequirements import BusinessTestrequirements
from .api.business_users import BusinessUsers
from .api.business_users_health import BusinessUsersHealth
from .api.business_users_queureport import BusinessUsersQueureport
from .api.business_users_userid import BusinessUsersUserid
from .api.business_users_userid_invite import BusinessUsersUseridInvite
from .api.business_users_userid_suspend import BusinessUsersUseridSuspend
from .api.businesses_registration import BusinessesRegistration
from .api.changepassword import Changepassword
from .api.console_businesses import ConsoleBusinesses
from .api.console_businesses_businessid import ConsoleBusinessesBusinessid
from .api.console_businesses_businessid_members import ConsoleBusinessesBusinessidMembers
from .api.console_businesses_businessid_members_memberid import ConsoleBusinessesBusinessidMembersMemberid
from .api.console_businesses_businessid_registration import ConsoleBusinessesBusinessidRegistration
from .api.covidtest_current import CovidtestCurrent
from .api.facilities import Facilities
from .api.facilities_recid import FacilitiesRecid
from .api.facility_queue import FacilityQueue
from .api.facility_queue_facilityId import FacilityQueueFacilityid
from .api.facility_queue_userId_grant import FacilityQueueUseridGrant
from .api.forgotpassword import Forgotpassword
from .api.loadtest_vitals_userKey_facilityId import LoadtestVitalsUserkeyFacilityid
from .api.notifications import Notifications
from .api.ping import Ping
from .api.questionnaires_current import QuestionnairesCurrent
from .api.registration import Registration
from .api.roles import Roles
from .api.terms import Terms
from .api.testfacilities import Testfacilities
from .api.testfacilities_recid import TestfacilitiesRecid
from .api.testfacility_patients import TestfacilityPatients
from .api.testfacility_patients_userId import TestfacilityPatientsUserid
from .api.testfacility_patients_userId_covid import TestfacilityPatientsUseridCovid
from .api.testfacility_patients_userId_vitals import TestfacilityPatientsUseridVitals
from .api.users import Users
from .api.users_covidtest import UsersCovidtest
from .api.users_questionnaires import UsersQuestionnaires
from .api.users_self import UsersSelf
from .api.users_self_acceptbusiness import UsersSelfAcceptbusiness
from .api.users_self_acceptbusiness_recordId import UsersSelfAcceptbusinessRecordid
from .api.users_self_covidtest import UsersSelfCovidtest
from .api.users_self_covidtest_history import UsersSelfCovidtestHistory
from .api.users_self_covidtest_testId import UsersSelfCovidtestTestid
from .api.users_self_hippa import UsersSelfHippa
from .api.users_self_image import UsersSelfImage
from .api.users_self_laodtestqr import UsersSelfLaodtestqr
from .api.users_self_logindescription import UsersSelfLogindescription
from .api.users_self_profileaccess import UsersSelfProfileaccess
from .api.users_self_profileaccess_companyId import UsersSelfProfileaccessCompanyid
from .api.users_self_questionnaire import UsersSelfQuestionnaire
from .api.users_self_related import UsersSelfRelated
from .api.users_self_related_userid import UsersSelfRelatedUserid
from .api.users_self_related_userid_covidtest import UsersSelfRelatedUseridCovidtest
from .api.users_self_related_userid_covidtest_history import UsersSelfRelatedUseridCovidtestHistory
from .api.users_self_related_userid_covidtest_testId import UsersSelfRelatedUseridCovidtestTestid
from .api.users_self_related_userid_hippa import UsersSelfRelatedUseridHippa
from .api.users_self_related_userid_laodtestqr import UsersSelfRelatedUseridLaodtestqr
from .api.users_self_related_userid_questionnaire import UsersSelfRelatedUseridQuestionnaire
from .api.users_self_related_userid_vitals import UsersSelfRelatedUseridVitals
from .api.users_self_teststatuses import UsersSelfTeststatuses
from .api.users_self_vitals import UsersSelfVitals
from .api.users_vitals import UsersVitals
from .api.users_userid import UsersUserid
from .api.users_userid_notifications import UsersUseridNotifications
from .api.users_userid_notifications_notifid import UsersUseridNotificationsNotifid
from .api.vitals_current import VitalsCurrent


routes = [
    dict(resource=About, urls=['/about'], endpoint='about'),
    dict(resource=Auth, urls=['/auth'], endpoint='auth'),
    dict(resource=BusinessNotifications, urls=['/business/notifications'], endpoint='business_notifications'),
    dict(resource=BusinessNotificationsNotifid, urls=['/business/notifications/<int:notifid>'], endpoint='business_notifications_notifid'),
    dict(resource=BusinessQrcode, urls=['/business/qrcode'], endpoint='business_qrcode'),
    dict(resource=BusinessTestrequirements, urls=['/business/testrequirements'], endpoint='business_testrequirements'),
    dict(resource=BusinessUsers, urls=['/business/users'], endpoint='business_users'),
    dict(resource=BusinessUsersHealth, urls=['/business/users/health'], endpoint='business_users_health'),
    dict(resource=BusinessUsersQueureport, urls=['/business/users/queureport'], endpoint='business_users_queureport'),
    dict(resource=BusinessUsersUserid, urls=['/business/users/<int:userid>'], endpoint='business_users_userid'),
    dict(resource=BusinessUsersUseridInvite, urls=['/business/users/<int:userid>/invite'], endpoint='business_users_userid_invite'),
    dict(resource=BusinessUsersUseridSuspend, urls=['/business/users/<int:userid>/suspend'], endpoint='business_users_userid_suspend'),
    dict(resource=BusinessesRegistration, urls=['/businesses/registration'], endpoint='businesses_registration'),
    dict(resource=Changepassword, urls=['/changepassword'], endpoint='changepassword'),
    dict(resource=ConsoleBusinesses, urls=['/console/businesses'], endpoint='console_businesses'),
    dict(resource=ConsoleBusinessesBusinessid, urls=['/console/businesses/<int:businessid>'], endpoint='console_businesses_businessid'),
    dict(resource=ConsoleBusinessesBusinessidMembers, urls=['/console/businesses/<int:businessid>/members'], endpoint='console_businesses_businessid_members'),
    dict(resource=ConsoleBusinessesBusinessidMembersMemberid, urls=['/console/businesses/<int:businessid>/members/<int:memberid>'], endpoint='console_businesses_businessid_members_memberid'),
    dict(resource=ConsoleBusinessesBusinessidRegistration, urls=['/console/businesses/<int:businessid>/registration'], endpoint='console_businesses_businessid_registration'),
    dict(resource=CovidtestCurrent, urls=['/covidtest/current'], endpoint='covidtest_current'),
    dict(resource=Facilities, urls=['/facilities'], endpoint='facilities'),
    dict(resource=FacilitiesRecid, urls=['/facilities/<int:recid>'], endpoint='facilities_recid'),
    dict(resource=FacilityQueue, urls=['/facility/queue'], endpoint='facility_queue'),
    dict(resource=FacilityQueueFacilityid, urls=['/facility/queue/<facilityId>'], endpoint='facility_queue_facilityId'),
    dict(resource=FacilityQueueUseridGrant, urls=['/facility/queue/<userId>/grant'], endpoint='facility_queue_userId_grant'),
    dict(resource=Forgotpassword, urls=['/forgotpassword'], endpoint='forgotpassword'),
    dict(resource=LoadtestVitalsUserkeyFacilityid, urls=['/loadtest/vitals/<userKey>/<facilityId>'], endpoint='loadtest_vitals_userKey_facilityId'),
    dict(resource=Notifications, urls=['/notifications'], endpoint='notifications'),
    dict(resource=Ping, urls=['/ping'], endpoint='ping'),
    dict(resource=QuestionnairesCurrent, urls=['/questionnaires/current'], endpoint='questionnaires_current'),
    dict(resource=Registration, urls=['/registration'], endpoint='registration'),
    dict(resource=Roles, urls=['/roles'], endpoint='roles'),
    dict(resource=Terms, urls=['/terms'], endpoint='terms'),
    dict(resource=Testfacilities, urls=['/testfacilities'], endpoint='testfacilities'),
    dict(resource=TestfacilitiesRecid, urls=['/testfacilities/<int:recid>'], endpoint='testfacilities_recid'),
    dict(resource=TestfacilityPatients, urls=['/testfacility/patients'], endpoint='testfacility_patients'),
    dict(resource=TestfacilityPatientsUserid, urls=['/testfacility/patients/<userId>'], endpoint='testfacility_patients_userId'),
    dict(resource=TestfacilityPatientsUseridCovid, urls=['/testfacility/patients/<userId>/covid'], endpoint='testfacility_patients_userId_covid'),
    dict(resource=TestfacilityPatientsUseridVitals, urls=['/testfacility/patients/<userId>/vitals'], endpoint='testfacility_patients_userId_vitals'),
    dict(resource=Users, urls=['/users'], endpoint='users'),
    dict(resource=UsersCovidtest, urls=['/users/covidtest'], endpoint='users_covidtest'),
    dict(resource=UsersQuestionnaires, urls=['/users/questionnaires'], endpoint='users_questionnaires'),
    dict(resource=UsersSelf, urls=['/users/self'], endpoint='users_self'),
    dict(resource=UsersSelfAcceptbusiness, urls=['/users/self/acceptbusiness'], endpoint='users_self_acceptbusiness'),
    dict(resource=UsersSelfAcceptbusinessRecordid, urls=['/users/self/acceptbusiness/<int:recordId>'], endpoint='users_self_acceptbusiness_recordId'),
    dict(resource=UsersSelfCovidtest, urls=['/users/self/covidtest'], endpoint='users_self_covidtest'),
    dict(resource=UsersSelfCovidtestHistory, urls=['/users/self/covidtest/history'], endpoint='users_self_covidtest_history'),
    dict(resource=UsersSelfCovidtestTestid, urls=['/users/self/covidtest/<int:testId>'], endpoint='users_self_covidtest_testId'),
    dict(resource=UsersSelfHippa, urls=['/users/self/hippa'], endpoint='users_self_hippa'),
    dict(resource=UsersSelfImage, urls=['/users/self/image'], endpoint='users_self_image'),
    dict(resource=UsersSelfLaodtestqr, urls=['/users/self/laodtestqr'], endpoint='users_self_laodtestqr'),
    dict(resource=UsersSelfLogindescription, urls=['/users/self/logindescription'], endpoint='users_self_logindescription'),
    dict(resource=UsersSelfProfileaccess, urls=['/users/self/profileaccess'], endpoint='users_self_profileaccess'),
    dict(resource=UsersSelfProfileaccessCompanyid, urls=['/users/self/profileaccess/<companyId>'], endpoint='users_self_profileaccess_companyId'),
    dict(resource=UsersSelfQuestionnaire, urls=['/users/self/questionnaire'], endpoint='users_self_questionnaire'),
    dict(resource=UsersSelfRelated, urls=['/users/self/related'], endpoint='users_self_related'),
    dict(resource=UsersSelfRelatedUserid, urls=['/users/self/related/<int:userid>'], endpoint='users_self_related_userid'),
    dict(resource=UsersSelfRelatedUseridCovidtest, urls=['/users/self/related/<userid>/covidtest'], endpoint='users_self_related_userid_covidtest'),
    dict(resource=UsersSelfRelatedUseridCovidtestHistory, urls=['/users/self/related/<int:userid>/covidtest/history'], endpoint='users_self_related_userid_covidtest_history'),
    dict(resource=UsersSelfRelatedUseridCovidtestTestid, urls=['/users/self/related/<userid>/covidtest/<int:testId>'], endpoint='users_self_related_userid_covidtest_testId'),
    dict(resource=UsersSelfRelatedUseridHippa, urls=['/users/self/related/<int:userid>/hippa'], endpoint='users_self_related_userid_hippa'),
    dict(resource=UsersSelfRelatedUseridLaodtestqr, urls=['/users/self/related/<int:userid>/laodtestqr'], endpoint='users_self_related_userid_laodtestqr'),
    dict(resource=UsersSelfRelatedUseridQuestionnaire, urls=['/users/self/related/<userid>/questionnaire'], endpoint='users_self_related_userid_questionnaire'),
    dict(resource=UsersSelfRelatedUseridVitals, urls=['/users/self/related/<userid>/vitals'], endpoint='users_self_related_userid_vitals'),
    dict(resource=UsersSelfTeststatuses, urls=['/users/self/teststatuses'], endpoint='users_self_teststatuses'),
    dict(resource=UsersSelfVitals, urls=['/users/self/vitals'], endpoint='users_self_vitals'),
    dict(resource=UsersVitals, urls=['/users/vitals'], endpoint='users_vitals'),
    dict(resource=UsersUserid, urls=['/users/<int:userid>'], endpoint='users_userid'),
    dict(resource=UsersUseridNotifications, urls=['/users/<int:userid>/notifications'], endpoint='users_userid_notifications'),
    dict(resource=UsersUseridNotificationsNotifid, urls=['/users/<int:userid>/notifications/<int:notifid>'], endpoint='users_userid_notifications_notifid'),
    dict(resource=VitalsCurrent, urls=['/vitals/current'], endpoint='vitals_current'),
]