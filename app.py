from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Dial

app = Flask(__name__)

# Zorg ervoor dat de rootroute correct werkt (om 404 te vermijden)
@app.route("/", methods=["GET"])
def home():
    return "Flask app is up and running!"

# Voeg de doorverbinden route toe
@app.route("/doorverbinden", methods=["POST"])
def doorverbinden():
    print(f"Ontvangen POST-aanroep: {request.json}")  # Voeg dit toe voor debugging
    response = VoiceResponse()
    response.say("Een ogenblikje, ik verbind u nu door naar een medewerker.", language='nl-NL')
    response.dial("0031884114114", caller_id="+3197010252180")
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
