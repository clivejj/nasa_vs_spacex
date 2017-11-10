from flask import Flask, render_template
import urllib2
import json


app=Flask(__name__)

@app.route('/')
def root():
   #was having trouble with urlopen
   #u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=FnzSTFCbbFeP1u1840hNVf8wF0tqw77Hz3GYf70B")
   u = '''
   {
      "copyright": "Robert Gendler", 
      "date": "2017-11-09", 
      "explanation": "Big, beautiful spiral galaxy NGC 1055 is a dominant member of a small galaxy group a mere 60 million light-years away toward the aquatically intimidating constellation Cetus. Seen edge-on, the island universe spans over 100,000 light-years, a little larger than our own Milky Way. The colorful stars in this cosmic close-up of NGC 1055 are in the foreground, well within the Milky Way. But the telltale pinkish star forming regions are scattered through winding dust lanes along the distant galaxy's thin disk. With a smattering of even more distant background galaxies, the deep image also reveals a boxy halo that extends far above and below the central bluge and disk of NGC 1055. The halo itself is laced with faint, narrow structures, and could represent the mixed and spread out debris from a satellite galaxy disrupted by the larger spiral some 10 billion years ago.", 
      "hdurl": "https://apod.nasa.gov/apod/image/1711/NGC1055-ESO-Crop-L1.jpg", 
      "media_type": "image", 
      "service_version": "v1", 
      "title": "NGC 1055 Close-up", 
      "url": "https://apod.nasa.gov/apod/image/1711/NGC1055-ESO-Crop1024_1.jpg"
    }
    '''
   d = json.loads(u)
   #print d
   return render_template("base.html", url = d[u'hdurl'], desc = d[u'explanation'])


if __name__ == '__main__':
   app.debug = True
   app.run()

	
