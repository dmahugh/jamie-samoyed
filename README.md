# Jamie Samoyed

This repo contains the source code for the [Jamie Samoyed site](http://jamiesamoyed.azurewebsites.net/), a simple photo album deployed as a web app on Microsoft Azure. The site is built on [Bottle](http://bottlepy.org/docs/dev/index.html), a lightweight WSGI framework for Python.

I use this site as a starter for other Bottle projects. To stand up an instance you can create an empty Azure web app and then link it to this GitHub repo, or you can click on this button and follow the instructions:

[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

The photo albums are populated by metadata in JSON files (/static/json), and the photos are stored in the /static/photos folder. A rudimentary API is included, and there are a few examples on the [API](/api) page. Here's an example of what's returned by the /api/album endpoint, for example:

![/api/album example](/static/images/api-getalbum.png)

You can follow Jamie & Alice on [Facebook](https://www.facebook.com/JamieSamoyed/), and they have an archive of over 10,000 photos on [Flickr](https://www.flickr.com/photos/dogerino/).

![Jamie & Alice](https://raw.githubusercontent.com/dmahugh/jamie-samoyed/master/static/images/homepage.jpg)
