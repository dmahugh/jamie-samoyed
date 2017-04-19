% from datetime import datetime
% from routes import get_albums

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Jamie Samoyed</title>
    <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/css/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand">Jamie Samoyed</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/about">About</a></li>
                    % albumdict = albumdict if 'albumdict' in locals() else get_albums()
                    % for album in albumdict:
                    <li><a href="/album/{{ album }}">{{ albumdict[album]['name'] }}</a></li>
                    % end
                    <li><a href="/api">API</a></li>
                    <li><a href="/sysinfo">sysinfo</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p class="copyright">Photos &copy; 2010-2017 Doug Mahugh. All Rights Reserved.</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
