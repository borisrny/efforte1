import io
from uuid import uuid4
from datetime import datetime, timedelta
import qrcode
from json import dumps

from src.model import user_get
from src.util import util_get_config, s3_presigned_url_get, s3_do_upload_buffer, pg_create


def qrcode_facility_queue_get(facility_id):
    cnf = util_get_config()
    name = cnf['s3']['facilityQRCode'].format(facility_id)
    return s3_presigned_url_get(name)


def qrcode_facility_queue_generate(facility_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    cnf = util_get_config()
    facility_url = '/'.join((cnf['apiBaseURL'], cnf['facilityQueueURL'].format(facility_id)))
    qr.add_data(facility_url)
    img = qr.make_image(fill_color="black", back_color="white")
    in_mem_file = io.BytesIO()
    img.save(in_mem_file)
    in_mem_file.seek(0)
    name = cnf['s3']['facilityQRCode'].format(facility_id)
    s3_do_upload_buffer(in_mem_file, name, 'image/jpeg')
    return s3_presigned_url_get(name)


def qrcode_user_access_generate(parent_id, user_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    cnf = util_get_config()
    temp_key = str(uuid4())
    pg_create(cnf, 'tempuserwaccess', {
        'akey': temp_key,
        'userid': user_id,
        'postuser': parent_id,
        'expiry': datetime.utcnow() + timedelta(hours=1)
    }, idfield='akey')

    facility_url = '/'.join((cnf['apiBaseURL'], cnf['userFacilityVITALWrite'].format(temp_key)))
    u = user_get(user_id)
    qr_data = {
        'url': facility_url,
        'firstName': u['first_name'],
        'lastName': u['last_name']
    }
    qr.add_data(dumps(qr_data))
    img = qr.make_image(fill_color="black", back_color="white")
    in_mem_file = io.BytesIO()
    img.save(in_mem_file)
    in_mem_file.seek(0)
    return in_mem_file
