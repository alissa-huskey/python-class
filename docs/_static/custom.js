try {
  var session = window.sessionStorage || {};
} catch (e) {
  var session = {};
}

// add relative URL base
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> setting relative URL base...");

  url = document.location.href;

  if (url.includes("github.io/alissa-huskey")) {
    // get the slash after github.io/alissa-huskey/
    base = url.substring(0, url.indexOf("/", 32));
  } else {
    base = document.location.origin;
  }

  console.log("python-class> base URL: " + base);

  elm = $("head").add("base")
  elm.attr["href"] = base
});

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

  prompt_in = jQuery("<div>").html("").addClass("prompt").addClass("prompt-in");
  prompt_out = jQuery("<div>").html("").addClass("prompt").addClass("prompt-out");

  prompt_in.insertBefore(".cell_input");
  prompt_out.insertBefore(".cell_output");
});

// add page name as body id and parent directory names as body classes
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> setting body ID...");

  url = window.location.href.split("#")[0];
  parts = url.split('/');

  parts.splice(0, 3); // remove http://domain.com
  pagename = parts.pop(); // remove pagename.html

  // remove python-class
  if (parts[0] == "python-class") {
    parts.shift();
  }

  if (pagename.endsWith(".html")) {
    pagename = pagename.slice(0, pagename.lastIndexOf(".html"));
  }

  console.log("python-class> body id:", pagename);
  body = $('body')
  body.attr('id', pagename)

  for(i = 0; i < parts.length; i++) {
    console.log("python-class> body class:", parts[i]);
    body.addClass(parts[i])
  }
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

// add "header-link" to a.header-link parent p tag
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class> fixing header links...");

  $("a.header-link").parents('p').addClass("header-link");
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

// attach player object to <asciinema-player> tags
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class:asciinema> adding asciinema players...");

  elements = $('asciinema-player');

  if (elements.length == 0) {
    console.log("python-class:asciinema> No <asciinema-player> tags found");
    return;
  }
  console.log("python-class:ascinema>", elements.length, "elements");

  for (var i = 0; i < elements.length; i++) {
    elm = elements[i];
    console.log("python-class:ascinema>", "element:", elm);

    attrs = elm.attributes
    options = {}

    // collect the attributes into an object
    for (var x = 0; x < attrs.length; x++) {
      a = attrs[x];
      options[a.name] = a.value;
    }

    console.log("python-class:ascinema>", "attrs:", options);
    AsciinemaPlayer.create(elm.getAttribute("src"), elm, options);
  }
});

// move source code links to top of the section so that the div is before the section header
window.addEventListener("DOMContentLoaded", (e) => {
  console.log("python-class:source-code> moving source code links to top of section...");

  var elements = $('div.source-code');

  console.log("python-class:source-code>", elements.length, "elements");

  if (elements.length == 0) {
    return;
  }

  for (var i = 0; i < elements.length; i++) {
    var elm = elements[i];
    console.log("python-class:source-code>", "source code links:", elm);

    var section = elm.parentElement;
    section.removeChild(elm);
    section.prepend(elm);
  }
});
