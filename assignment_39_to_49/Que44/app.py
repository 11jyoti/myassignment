from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data
    data = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    
    # Return data as JSON
    return jsonify(data)

if _name_ == '_main_':
    app.run(debug=True)