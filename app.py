from bottle import Bottle, run, route, post, template, redirect, request, static_file

app = Bottle()

#static files
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = DIR_PATH + '/static/' 

def create_qr(data):
    import qrcode 
    import qrcode.image.svg
    import random
    from PIL import Image

    filename = str(random.randint(1,1000000))

    if data['format'] == ".png":
        qr = qrcode.QRCode(
            version=1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = data['box_size'],
            border = data['border']
        )
        qr.add_data(data['data'])
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        filename = filename + ".png"
        img.save(DIR_PATH + '/static/qrcodes/' + filename)
        
    else:   
        if data['method'] == "basic":
            factory = qrcode.image.svg.SvgImage
        elif data['method'] == "fragment":
            factory = qrcode.image.svg.SvgFragmentImage
        else:
            factory = qrcode.image.svg.SvgPathImage

        filename = filename + ".svg"
        img = qrcode.make(data['data'], image_factory=factory)
        img.save(DIR_PATH + '/static/qrcodes/' + filename)

    filepath = DIR_PATH + '/static/qrcodes/' + filename
    return('/static/qrcodes/' + filename)
    

@app.route('/')
@app.route('/index')
def index():
    redirect('/qr')

@app.get('/qr')
def qr():
    return template('index.tpl')

@app.post('/qr')
def do_qr():
    data = {
        'data': request.forms.get("data"),
        'format': request.forms.get("format"),
        'method' : request.forms.get("method"),
        'box_size': request.forms.get("box_size"),
        'border': request.forms.get("border")
    }

    qr = create_qr(data)
    print(qr)
    return static_file(qr, root=DIR_PATH)

#static files
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=STATIC_PATH)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=False)