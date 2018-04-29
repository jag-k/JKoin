<!DOCTYPE html>
<!--c = "V:/home/localhost/www/jkvkbot.com/"-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>{{ text }} - JKs Site</title>
        <meta name="description" content="Блокчейн-криптовалюта JKoin">
        <meta name="keywords" content="Блокчейн, криптовалюта, JKoin, Jag_k">
        <meta name="viewport" content="wdth=device-width, initial-scale=1">

        <!--<link rel="stylesheet" href="jquery-3.1.1.js">-->
        <!--<link rel="stylesheet" href="selectivizr.js">-->

        <link href="/static/image/JKoin2.ico" rel="shortcut icon" tupe="image/x-icon">
        
        <!--Bootstrap-->
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
        
        <link rel="stylesheet" href="static/css/main.css">
        
<!--        http://lorempixel.com/1500/100/-->
    </head>
    <body>
        % include('static/templates/head.tpl')
        <div class="container" id="main_content">
            % include("static/templates/%s.tpl" % text.lower())
        </div>
    </body>
</html>