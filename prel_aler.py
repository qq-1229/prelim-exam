from flask import Flask, jsonify, request
app = Flask(__name__)

hearts = [
    {
        "heart_id" : "001",
        "date" : ["10-01-22"],
        "heart_rate" : [ "120"]
    },
    {
        "heart_id" : "002",
        "date" : ["11-02-22"],
        "heart_rate" : [ "90"]
    }
]
@app.route ('/hearts', methods=['GET'])
def getHearts():
    return jsonify(hearts)
@app.route('/hearts', methods=['POST'])
def addheart():
    heart = request.get_json()
    hearts.append(heart)
    return {'id': len(hearts)},200

@app.route('/hearts/<int:index>', methods=['DELETE'])
def deleteHeart(index):
    hearts.pop(index)
    return 'heart id was deleted successfully' , 200

if __name__ ==  '__main__':
    app.run()