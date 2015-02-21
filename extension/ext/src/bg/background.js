// if you checked "fancy-settings" in extensionizr.com, uncomment this lines

// var settings = new Store("settings", {
//     "sample_setting": "This is how you use Store.js to remember values"
// });

console.log("Hello, world!13")

//example of using a message handler from the inject scripts

chrome.webRequest.onBeforeRequest.addListener(
  function(info) {
    console.log("Url blocked: " + info.url);
    random_link = window.links[Math.floor(Math.random()*window.links.length)].data.url;
    console.log("Redirecting to: " + random_link);
    return {redirectUrl: random_link};
  },
  // filters
  {
    urls: [
      "*://*.facebook.com/*",
      "*://facebook.com/*"
    ],
  },
  // extraInfoSpec
  ["blocking"]);

var getRedditLinks = function() {
    console.log("Starting up!")
    var Snoocore = window.Snoocore;
    var reddit = new Snoocore({
      userAgent: 'noprocrast extension @0.0.1 by /u/godlikesme'
    });

    window.links = []
    links = reddit("/r/GetMotivated/top.json?t=month").get().then(function (data){
        window.links = data.data.children
        console.log(window.links);
    },
    function(error) {
        consoler.log("Snoo error " + error);
    });
};

chrome.runtime.onInstalled.addListener(getRedditLinks)
chrome.runtime.onStartup.addListener(getRedditLinks)
