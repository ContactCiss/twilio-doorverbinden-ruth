from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Dial, Say

app = Flask(__name__)

@app.route("/doorverbinden", methods=["POST"])
def doorverbinden():
    response = VoiceResponse()
    response.say("Een ogenblikje, ik verbind u nu door naar een medewerker.", language='nl-NL')
    response.dial("0031884114114", caller_id="+31907010252180")
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
