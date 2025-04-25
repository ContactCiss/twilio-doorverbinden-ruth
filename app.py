from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Dial

app = Flask(__name__)

@app.route("/doorverbinden", methods=['POST'])
def doorverbinden():
    # accepteer form-data van Twilio
    response = VoiceResponse()
    response.say("Een ogenblikje, ik verbind u nu door naar een collega.", language="nl-NL", voice="Polly.Ruben")
    response.dial("+31630608057")
    return str(response), 200, {'Content-Type': 'application/xml'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

