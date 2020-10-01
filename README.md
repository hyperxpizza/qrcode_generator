# QR code generator
This is a simple bottle app to generate qr codes

## Can I see it anywhere?
https://qrcode.kernel-panic.pl

## How to run?
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## Run with Docker
```bash
sudo docker build qrcode-generator:1.0.0 .
sudo docker run -p 8080:8080 qrcode-generator:1.0.0
```