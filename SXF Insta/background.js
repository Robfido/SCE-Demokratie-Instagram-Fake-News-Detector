chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    runScript();
  /*
    if (changeInfo.status === 'complete' && tab.url && tab.url.includes("https://www.instagram.com/")) {
        chrome.tabs.executeScript(tabId, {file: 'content.js'});
    }
    */
});

/*
chrome.tabs.onUpdated.addListener((tabId, tab) => {
    if (tab.url && tab.url.includes("youtube.com/watch")) {
      const queryParameters = tab.url.split("?")[1];
      const urlParameters = new URLSearchParams(queryParameters);
  
      chrome.tabs.sendMessage(tabId, {
        type: "NEW",
        videoId: urlParameters.get("v"),
      });
    }
  });
  */