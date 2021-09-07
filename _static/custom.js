try {
  var session = window.sessionStorage || {};
} catch (e) {
  var session = {};
}

// remove href attribute from .missing-term
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> removing missing-term hrefs...");

  orphans = $("a.term-missing");
  for(i = 0; i < orphans.length; i++) {
    orphans[i].removeAttribute("href");
  }
});

// add In: and Out: before cell_input and cell_output
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> adding cell labels...");

  prompt_in = jQuery("<div>").html("In:").addClass("prompt").addClass("prompt-in");
  prompt_out = jQuery("<div>").html("Out:").addClass("prompt").addClass("prompt-out");

  prompt_in.insertBefore(".cell_input");
  prompt_out.insertBefore(".cell_output");
});

// make the name of the .html file the body tags id attribute
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> setting body ID...");

  url = window.location.href.split("#")[0];
  pagename = url.slice(url.lastIndexOf("/")+1);

  if (pagename.endsWith(".html")) {
    pagename = pagename.slice(0, pagename.lastIndexOf(".html"));
  }

  console.log("python-class> pagename:", pagename);

  node = document.getElementsByTagName("body")[0];
  node.id = pagename;
});

// move the code-block captions to under the code blocks
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> fixing captions...");

  captions = $(".code-block-caption")
  for(i = 0; i < captions.length; i++) {
      cap=captions[i]
      sib = cap.nextElementSibling
      cap.remove()
      sib.append(cap)
  }
});

// add "full-width" class to literal-block-wrappers that contain a full-width div
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> fixing full width...");

  var divs = $("div.full-width");

  for(var i = 0; i < divs.length; i+=1) {
    var div = divs[i];
    var parent = div.parentElement;

    if (!parent) {
      continue;
    }

    if (parent.classList.contains("literal-block-wrapper")) {
      parent.classList.add("full-width");
    }
  }
});

// set the platform value in session.platform
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> setting session.platform...");

  var platform = window.navigator.platform;
  if (platform.indexOf('Win') != -1 ) {
    platform = "Windows";
  } else if (platform.indexOf("Mac") != -1 ) {
    platform = "MacOS";
  } else if (platform.indexOf("Linux") != -1 ) {
    platform = "Linux";
  } else {
    platform = "unknown";
  }

  session.platform = platform;
});

// select the tab for the relevant platform
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> selecting OS tab...");

  if ($("button.sphinx-tabs-tab").length == 0 || session.platform == "unknown") {
    console.log("python-class>", "exiting: no sphinx tabs on this page or platform is unknown");
    return;
  }

  if (session.platform != "unknown") {
    elms = $("button.sphinx-tabs-tab:contains('"+session.platform+"')");
    if (elms.length == 0) {
      console.log("python-class>", "exiting: no sphinx tabs found for platform", session.platform);
      return;
    }

    console.log("python-class>", "selecting tab for platform:", session.platform);
    tab = elms[0];
    deselectTabList(tab);
    selectTab(tab);
  }
});
