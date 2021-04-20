const { SSL_OP_EPHEMERAL_RSA } = require('node:constants');
let Parser = require('rss-parser');
let parser = new Parser();


(async () => {
  let feed = await parser.parseURL('https://hypixel.net/forums/skyblock-patch-notes.158/index.rss');
  var latest_update = feed.items[0].title;
  var loop = true;
  while (loop) {
    feed = await parser.parseURL('https://hypixel.net/forums/skyblock-patch-notes.158/index.rss');
    if (feed.items[0].title === latest_update) {
        sleep(120)
    } else {
        loop = false;
        console.log(feed.items[0].title)
    }
  }
})();
