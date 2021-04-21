// npm install --save rss-parser
let Parser = require('rss-parser');
let parser = new Parser();

function Update () {
  (async () => {
    let feed = await parser.parseURL('https://hypixel.net/forums/skyblock-patch-notes.158/index.rss');
    var latest_update = feed.items[0].title;
    var loop = true;
    while (loop) {
      feed = await parser.parseURL('https://hypixel.net/forums/skyblock-patch-notes.158/index.rss');
      if (feed.items[0].title === latest_update) {
      } else {
          loop = false;
          console.log(feed.items[0].title)
      }
    }
  })();
}

