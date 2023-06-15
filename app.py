"""
Stream zoom recordings to an S3 bucket
"""
import zoom
import hashlib
import hmac
from flask import Flask, request, json, jsonify
from config import config
from hashlib import sha256



app = Flask(__name__)

@app.route("/")
def test():
    return "Hello world!"

@app.route("/webhook", methods=["POST"])
def webhook():
    response = None
    message = f"v0:{request.headers.get('x-zm-request-timestamp')}:{request.json}"
    hash_for_verify = hmac.new(config.zoom_webhook_secret_token.encode("utf-8"),
                               message.encode("utf-8"), hashlib.sha256).hexdigest()
    signature = f"v0={hash_for_verify}"
    
    data = request.json
   

    if request.headers.get("x-zm-signature") == signature:
        
        if data["event"] == "endpoint.url_validation":
            plain_token = data["payload"]["plainToken"]
            hash_obj = hmac.new(config.zoom_webhook_secret_token.encode("utf-8"),
                                plain_token.encode("utf-8"),
                                hashlib.sha256).hexdigest()
            response = {
                "message": {
                    "plainToken": plain_token,
                    "encryptedToken": hash_obj
                },
                "status": 200
            }
            return jsonify(response["message"]), response["status"]
        else:
            response = {"message": "Authorized request to Zoom Webhook sample.", "status": 200}
            print(response["message"])
            return jsonify(response), response["status"]
    else:
        response = {'message': 'Unauthorized request to Zoom Webhook sample.', 'status': 401}
        print(response['message'])
        return jsonify(response), response['status']


    # phone.recording_completed
    # recording.completed

    
    
   

if __name__ == "__main__":
    app.run(debug=True, port=8000)

    # user_email = config.user_email
    # start_date = config.start_date.split("-")
    # start_date = [int(start_date[0]), int(start_date[1]), int(start_date[2])]
    
    # start_date = [int(config.start_date[0]), int(config.start_date[1]), int(config.start_date[2])]
    # end_date = [int(config.end_date[0]), int(config.end_date[1]), int(config.end_date[2])]
    # recordings = zoom.get_all_recordings(config.user_email, config.start_date, config.end_date)

    # res = zoom.get_all_recordings(config.user_email, start_date)
    # zoom.write_recording_to_file(res, config.file_name)
    # zoom.fetch_recordings_and_upload_to_s3()
    # # print("recordings: ", res)

    # print("SCRIPT EXECUTED SUCCESSFULLY: Upload complete!")


