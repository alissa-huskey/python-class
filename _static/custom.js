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

