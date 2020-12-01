// move the code-block captions to under the code blocks
function addBodyId() {
  url = window.location.href.split("#")[0]
  pagename = url.slice(url.lastIndexOf("/")+1)

  if (pagename.endsWith(".html")) {
    pagename = pagename.slice(0, pagename.lastIndexOf(".html"))
  }

  console.log("addBodyId()> pagename: " + pagename)

  node = document.getElementsByTagName("body")[0]
  node.id = pagename
}

// move the code-block captions to under the code blocks
function fixCaptions() {
  captions = $(".code-block-caption")
  for(i = 0; i < captions.length; i++) {
      cap=captions[i]
      sib = cap.nextElementSibling
      cap.remove()
      sib.append(cap)
  }
}

document.addEventListener("DOMContentLoaded", fixCaptions);
document.addEventListener("DOMContentLoaded", addBodyId);

