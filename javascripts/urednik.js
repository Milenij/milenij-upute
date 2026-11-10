/*
 * ✏️ edit button for editors only.
 *
 * The button (Material's content.action.edit) is hidden by CSS for everyone. Open any
 * page with ?urednik at the end of the address once, and this browser remembers it and
 * shows the button on every page. ?urednik=off hides it again.
 *
 * This only hides the button; it isn't protection. Editing itself still needs write
 * access to the GitHub repository.
 */
(function () {
  "use strict";
  var KEY = "milenij-urednik";

  var params = new URLSearchParams(location.search);
  if (params.has("urednik")) {
    var off = params.get("urednik") === "off";
    try {
      if (off) localStorage.removeItem(KEY);
      else localStorage.setItem(KEY, "1");
    } catch (e) { /* storage blocked */ }

    // Remove ?urednik from the address, so it isn't copied along when sharing a link
    params.delete("urednik");
    var query = params.toString();
    history.replaceState(history.state, "", location.pathname + (query ? "?" + query : "") + location.hash);
  }

  var on = false;
  try { on = localStorage.getItem(KEY) === "1"; } catch (e) { /* storage blocked */ }
  // On <html>, which stays in place when Material swaps pages (instant navigation)
  if (on) document.documentElement.setAttribute("data-urednik", "");
  else document.documentElement.removeAttribute("data-urednik");
})();
