from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name']
    count = request.form['count']
    address = request.form['address']
    phone = request.form['phone']

    doc = {'name': name, 'count':count, 'address':address, 'phone':phone}
    print(doc)
    db.orders.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문의 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders_table = list(db.orders.find({},{'_id':False}))
# 여길 채워나가세요!
    return jsonify({'result': 'success', 'orders': orders_table})
#how to add github??

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)