import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

from src.util import util_get_config


def send_sms(phone_number, text):
    cnf = util_get_config()
    session = boto3.Session(profile_name=cnf['aws']['profile'])
    client = session.client("sns", region_name='us-east-1')
    client.publish(
        PhoneNumber=phone_number,
        Message=text
    )


def s3_presigned_url_get(object_name, expiration=3600):
    cnf = util_get_config()
    session = boto3.Session(profile_name=cnf['aws']['profile'])
    client = session.client('s3', region_name='us-east-2',
                            config=Config(s3={'addressing_style': 'path'}, signature_version='s3v4'))
    try:
        client.head_object(Bucket=cnf['s3']['name'], Key=object_name)
        response = client.generate_presigned_url('get_object',
                                                 Params={'Bucket': cnf['s3']['name'],
                                                         'Key': object_name},
                                                 ExpiresIn=expiration)
    except ClientError as e:
        return None
    return response


def s3_get_profile_url(recid):
    cnf = util_get_config()['s3']['profile']
    return s3_presigned_url_get('{}/{}/{}'.format(cnf['dir'], recid, cnf['fileName']))


def s3_get_covidtest_url(recid):
    cnf = util_get_config()['s3']['covidtest']
    return s3_presigned_url_get('{}/{}/{}'.format(cnf['dir'], recid, cnf['fileName']))


def s3_get_requisition_url(recid):
    cnf = util_get_config()['s3']['requisition']
    return s3_presigned_url_get('{}/{}/{}'.format(cnf['dir'], recid, cnf['fileName']))


def s3_do_upload(file, obj_name):
    cnf = util_get_config()
    session = boto3.Session(profile_name=cnf['aws']['profile'])
    client = session.client('s3')
    client.upload_fileobj(
        file,
        cnf['s3']['name'],
        obj_name,
        ExtraArgs={
            "ContentType": file.content_type
        }
    )


def s3_do_upload_buffer(file_buffer, obj_name, content_type):
    cnf = util_get_config()
    session = boto3.Session(profile_name=cnf['aws']['profile'])
    client = session.client('s3')
    client.upload_fileobj(
        file_buffer,
        cnf['s3']['name'],
        obj_name,
        ExtraArgs={
            "ContentType": content_type
        }
    )


def s3_upload_avatar(file, user_id):
    cnf_prof = util_get_config()['s3']['profile']
    obj_name = '{}/{}/{}'.format(cnf_prof['dir'], user_id, cnf_prof['fileName'])
    s3_do_upload(file, obj_name)


def s3_upload_covidtest(file, test_id):
    cnf_prof = util_get_config()['s3']['covidtest']
    obj_name = '{}/{}/{}'.format(cnf_prof['dir'], test_id, cnf_prof['fileName'])
    s3_do_upload(file, obj_name)


def s3_upload_requisition(file, test_id):
    cnf_prof = util_get_config()['s3']['requisition']
    obj_name = '{}/{}/{}'.format(cnf_prof['dir'], test_id, cnf_prof['fileName'])
    s3_do_upload(file, obj_name)
