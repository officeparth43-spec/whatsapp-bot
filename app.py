import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Environment Variable માંથી API Key લેશે
GEMINI_API_KEY = os.environ.get("import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Environment Variable માંથી API Key લેશે
GEMINI_API_KEY = os.environ.get(import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Environment Variable માંથી API Key લેશે
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_latest_knowledge_base():
    """data.txt ફાઈલમાંથી તાજો ડેટા વાંચવા માટે"""
    try:
        if os.path.exists("data.txt"):
            with open("data.txt", "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        print("Error reading data.txt:", e)
    return ""

@app.route('/', methods=['POST', 'GET'])
def reply():
    if request.method == 'GET':
        return "Server is running!", 200
    
    data = request.get_json(silent=True) or {}
    
    # ઓટો-રિપ્લાય એપ જે મેસેજ મોકલે તે મેળવવો
    incoming_msg = data.get('query', {}).get('message', '') or data.get('message', '')
    
    if not incoming_msg:
        return jsonify({"reply": ""})
    
    # દર વખતે સવાલ આવે ત્યારે data.txt માંથી તાજો ડેટા વાંચવો
    knowledge_base = get_latest_knowledge_base()
    
    system_instruction = f"""
તમે એક મદદગાર એસિસ્ટન્ટ છો. 
નીચે આપેલી માહિતીમાંથી જ સામેવાળાના પ્રશ્નનો સાચો અને ટૂંકો જવાબ આપો:
{knowledge_base}

જો આપેલી માહિતીમાં જવાબ ન હોય, તો ફક્ત 'માફ કરશો, આ અંગે મારી પાસે માહિતી નથી.' લખવું.
"""

    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        response = model.generate_content(incoming_msg)
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "માફ કરશો, પ્રોસેસ કરવામાં ભૂલ થઈ છે."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))"")
genai.configure(api_key=GEMINI_API_KEY)

def get_latest_knowledge_base():
    """data.txt ફાઈલમાંથી તાજો ડેટા વાંચવા માટે"""
    try:
        if os.path.exists("data.txt"):
            with open("data.txt", "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        print("Error reading data.txt:", e)
    return ""

@app.route('/', methods=['POST', 'GET'])
def reply():
    if request.method == 'GET':
        return "Server is running!", 200
    
    data = request.get_json(silent=True) or {}
    
    # ઓટો-રિપ્લાય એપ જે મેસેજ મોકલે તે મેળવવો
    incoming_msg = data.get('query', {}).get('message', '') or data.get('message', '')
    
    if not incoming_msg:
        return jsonify({"reply": ""})
    
    # દર વખતે સવાલ આવે ત્યારે data.txt માંથી તાજો ડેટા વાંચવો
    knowledge_base = get_latest_knowledge_base()
    
    system_instruction = f"""
તમે એક મદદગાર એસિસ્ટન્ટ છો. 
નીચે આપેલી માહિતીમાંથી જ સામેવાળાના પ્રશ્નનો સાચો અને ટૂંકો જવાબ આપો:
{knowledge_base}

જો આપેલી માહિતીમાં જવાબ ન હોય, તો ફક્ત 'માફ કરશો, આ અંગે મારી પાસે માહિતી નથી.' લખવું.
"""

    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        response = model.generate_content(incoming_msg)
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "માફ કરશો, પ્રોસેસ કરવામાં ભૂલ થઈ છે."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))")
genai.configure(api_key=GEMINI_API_KEY)

def get_latest_knowledge_base():
    """data.txt ફાઈલમાંથી તાજો ડેટા વાંચવા માટે"""
    try:
        if os.path.exists("data.txt"):
            with open("data.txt", "r", encoding="utf-8") as f:
                return f.read()
    except Exception as e:
        print("Error reading data.txt:", e)
    return ""

@app.route('/', methods=['POST', 'GET'])
def reply():
    if request.method == 'GET':
        return "Server is running!", 200
    
    data = request.get_json(silent=True) or {}
    
    # ઓટો-રિપ્લાય એપ જે મેસેજ મોકલે તે મેળવવો
    incoming_msg = data.get('query', {}).get('message', '') or data.get('message', '')
    
    if not incoming_msg:
        return jsonify({"reply": ""})
    
    # દર વખતે સવાલ આવે ત્યારે data.txt માંથી તાજો ડેટા વાંચવો
    knowledge_base = get_latest_knowledge_base()
    
    system_instruction = f"""
તમે એક મદદગાર એસિસ્ટન્ટ છો. 
નીચે આપેલી માહિતીમાંથી જ સામેવાળાના પ્રશ્નનો સાચો અને ટૂંકો જવાબ આપો:
{knowledge_base}

જો આપેલી માહિતીમાં જવાબ ન હોય, તો ફક્ત 'માફ કરશો, આ અંગે મારી પાસે માહિતી નથી.' લખવું.
"""

    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        response = model.generate_content(incoming_msg)
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "માફ કરશો, પ્રોસેસ કરવામાં ભૂલ થઈ છે."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
