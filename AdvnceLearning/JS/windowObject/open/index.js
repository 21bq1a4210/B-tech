console.log("Hello console");
let windowObjectReference = null; // global variable
const windowFeatures = "left=100, top=100, width=320, height=320";
function openRequestedTab(url, windowName) {
  if (windowObjectReference === null || windowObjectReference.closed) {
    windowObjectReference = window.open(url, windowName, windowFeatures);
  } else {
    windowObjectReference.focus();
  }
}

const link = document.querySelector("a[target='OpenWikipediaWindow']");
link.addEventListener(
  "click",
  (event) => {
    openRequestedTab(link.href);
    event.preventDefault();
  },
  false,
);

let previousURL;
function openRequestedSingleTab(url){
    if (windowObjectReference === null || windowObjectReference.closed){
        windowObjectReference = window.open(url, "SingleSecondaryWindowName", windowFeatures);
        /* if the resource to load is different,
       then we load it in the already opened secondary window and then
       we bring such window back on top/in front of its parent window. */
       windowObjectReference.focus();
    } else {
        windowObjectReference.focus();
    }
    previousURL = url;
    /* explanation: we store the current url in order to compare url
     in the event of another call of this function. */
}

const links = document.querySelectorAll("a[target='SingleSecondaryWindowName']",);
for (const link of links){
    link.addEventListener("click",
    (event) => {
        openRequestedSingleTab(link.href);
        event.preventDefault();
    },
    false,
    );
}