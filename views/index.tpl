<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>QRcode Generator</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>QR code Generator</h1>
    <form action="/qr" method="post">
        <h3>Data:</h3> 
        <input type="text" name="data" value="" required> <br>
        <h3>Box size: </h3> 
        <input type="number" name="box_size" required>
        <h3>Border: </h3> 
        <input type="number" name="border" required>
        <h3>Method: </h3>
        <input type="radio" name="method" value="Basic" required> Basic
        <input type="radio" name="method" value="Fragment" required> Fragment
        <input type="radio" name="method" id="Whatever" required> Else <br>
        <h3>File format: </h3>
        <input type="radio" name="format" value=".svg" required>SVG
        <input type="radio" name="format" value=".png" required>PNG <br>
        <input type="submit" value="Create!" id="submit">
    </form>
</body>
</html>