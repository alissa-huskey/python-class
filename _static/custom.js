// add In: and Out: before cell_input and cell_output
function addCellLabels() {
  console.log("addCellLabels()>")

  prompt_in = jQuery("<div>").html("In:").addClass("prompt").addClass("prompt-in")
  prompt_out = jQuery("<div>").html("Out:").addClass("prompt").addClass("prompt-out")

  console.log(prompt_in)
  console.log(prompt_out)

  prompt_in.insertBefore(".cell_input")
  prompt_out.insertBefore(".cell_output")
}

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

// add "full-width" class to literal-block-wrappers that contain a full-width div
function fixFullWidth() {
  console.log("fixFullWidth()")

  var divs = $("div.full-width");

  for(var i = 0; i < divs.length; i+=1) {
    var div = divs[i];
    var parent = div.parentElement;

    if (!parent) {
      continue
    }

    if (parent.classList.contains("literal-block-wrapper")) {
      parent.classList.add("full-width");
      console.log("classes:", parent.className)
    }

  }
}

document.addEventListener("DOMContentLoaded", fixCaptions);
document.addEventListener("DOMContentLoaded", addBodyId);
document.addEventListener("DOMContentLoaded", fixFullWidth);
document.addEventListener("DOMContentLoaded", addCellLabels);

