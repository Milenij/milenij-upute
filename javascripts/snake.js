/*
 * Easter egg: type "snake" or "zmija" into the search box to play a snake game.
 *
 * Everything lives in this one file (game, styles, controls). To remove it, delete
 * this file and the "javascripts/snake.js" line under extra_javascript in mkdocs.yml.
 *
 * Controls: arrow keys or WASD, swipe on phones. Space = pause / new game, Esc = close.
 */
(function () {
  "use strict";
  if (window.__mileniSnake) return; // load once, also with instant navigation
  window.__mileniSnake = true;

  var TRIGGERS = ["snake", "zmija"];
  var GRID = 20; // cells per side
  var START_SPEED = 140; // ms per step
  var MIN_SPEED = 70;
  var BEST_KEY = "milenij-snake-best";

  var overlay, canvas, ctx, scoreEl, bestEl, msgEl;
  var snake, dir, queue, food, score, best, timer, speed, state; // state: ready | run | pause | over

  /* ---------- styles ---------- */
  var css =
    ".snake-overlay{position:fixed;inset:0;z-index:1000;display:flex;align-items:center;" +
    "justify-content:center;padding:16px;background:rgba(0,0,0,.55);backdrop-filter:blur(3px)}" +
    ".snake-panel{box-sizing:border-box;width:min(440px,100%);min-width:0;padding:16px;border-radius:.8rem;" +
    "background:var(--md-default-bg-color);color:var(--md-default-fg-color);" +
    "box-shadow:0 10px 40px rgba(0,0,0,.4);font-family:var(--md-text-font-family)}" +
    ".snake-head{display:flex;flex-wrap:wrap;align-items:center;gap:4px 12px;margin-bottom:12px;font-size:.8rem}" +
    ".snake-head strong{font-size:1rem;color:#5279af;margin-right:auto}" +
    ".snake-close{border:0;background:none;color:inherit;font-size:1.4rem;line-height:1;cursor:pointer;padding:0 4px}" +
    ".snake-canvas{display:block;width:100%;min-width:0;max-width:100%;aspect-ratio:1;border-radius:.6rem;touch-action:none;" +
    "background:var(--md-code-bg-color)}" +
    ".snake-msg{min-height:1.4em;margin-top:10px;text-align:center;font-size:.75rem;" +
    "color:var(--md-default-fg-color--light)}";

  function addStyles() {
    if (document.querySelector("style[data-snake]")) return;
    var s = document.createElement("style");
    s.setAttribute("data-snake", "");
    s.textContent = css;
    document.head.appendChild(s);
  }

  /* ---------- trigger from the search box ---------- */
  // Start only once the word has stayed "snake" for a moment (or on Enter), so someone
  // typing a longer search that begins with it isn't interrupted halfway.
  var WAIT = 700; // ms
  var pending;

  function isSearch(t) { return t && t.matches && t.matches(".md-search__input"); }
  function isTrigger(t) { return TRIGGERS.indexOf(t.value.trim().toLowerCase()) !== -1; }

  document.addEventListener("input", function (e) {
    if (!isSearch(e.target)) return;
    clearTimeout(pending);
    if (isTrigger(e.target)) {
      var t = e.target;
      pending = setTimeout(function () { if (isTrigger(t)) launch(t); }, WAIT);
    }
  }, true);

  document.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && isSearch(e.target) && isTrigger(e.target)) {
      e.preventDefault();
      e.stopImmediatePropagation(); // don't open the first search result
      clearTimeout(pending);
      launch(e.target);
    }
  }, true);

  function launch(t) {
    t.value = "";
    t.dispatchEvent(new Event("input", { bubbles: true })); // clear the results list
    t.blur();
    var toggle = document.getElementById("__search");
    if (toggle && toggle.checked) {
      toggle.checked = false;
      toggle.dispatchEvent(new Event("change"));
    }
    open();
  }

  /* ---------- open / close ---------- */
  function open() {
    if (overlay) return;
    addStyles();
    overlay = document.createElement("div");
    overlay.className = "snake-overlay";
    overlay.innerHTML =
      '<div class="snake-panel" role="dialog" aria-modal="true" aria-label="Zmija">' +
      '<div class="snake-head"><strong>🐍 Zmija</strong>' +
      '<span>Bodovi: <b class="snake-score">0</b></span>' +
      '<span>Rekord: <b class="snake-best">0</b></span>' +
      '<button class="snake-close" type="button" aria-label="Zatvori">×</button></div>' +
      '<canvas class="snake-canvas" width="400" height="400"></canvas>' +
      '<div class="snake-msg"></div></div>';
    document.body.appendChild(overlay);

    canvas = overlay.querySelector("canvas");
    ctx = canvas.getContext("2d");
    scoreEl = overlay.querySelector(".snake-score");
    bestEl = overlay.querySelector(".snake-best");
    msgEl = overlay.querySelector(".snake-msg");

    best = 0;
    try { best = parseInt(localStorage.getItem(BEST_KEY), 10) || 0; } catch (e) { /* storage blocked */ }
    bestEl.textContent = best;

    overlay.querySelector(".snake-close").addEventListener("click", close);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    canvas.addEventListener("touchstart", onTouchStart, { passive: true });
    canvas.addEventListener("touchend", onTouchEnd);
    canvas.addEventListener("click", function () { if (state !== "run") start(); });
    window.addEventListener("keydown", onKey, true);

    reset();
    overlay.querySelector(".snake-close").focus();
  }

  function close() {
    clearInterval(timer);
    window.removeEventListener("keydown", onKey, true);
    if (overlay) overlay.remove();
    overlay = null;
  }

  /* ---------- game ---------- */
  function reset() {
    clearInterval(timer);
    var mid = Math.floor(GRID / 2);
    snake = [{ x: mid, y: mid }, { x: mid - 1, y: mid }, { x: mid - 2, y: mid }];
    dir = { x: 1, y: 0 };
    queue = [];
    score = 0;
    speed = START_SPEED;
    scoreEl.textContent = 0;
    placeFood();
    state = "ready";
    msgEl.textContent = "Strelice / WASD ili povucite prstom za početak";
    draw();
  }

  function start() {
    if (state === "over") reset();
    state = "run";
    msgEl.textContent = "Razmak = pauza · Esc = zatvori";
    clearInterval(timer);
    timer = setInterval(step, speed);
  }

  function pause() {
    clearInterval(timer);
    state = "pause";
    msgEl.textContent = "Pauza – razmak za nastavak";
  }

  function placeFood() {
    do {
      food = { x: rand(GRID), y: rand(GRID) };
    } while (snake.some(function (p) { return p.x === food.x && p.y === food.y; }));
  }

  function rand(n) { return Math.floor(Math.random() * n); }

  function turn(x, y) {
    var last = queue.length ? queue[queue.length - 1] : dir;
    if (last.x === -x && last.y === -y) return; // no turning back into yourself
    if (last.x === x && last.y === y) return;
    if (queue.length < 3) queue.push({ x: x, y: y });
    if (state !== "run") start();
  }

  function step() {
    if (queue.length) dir = queue.shift();
    var head = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };
    var hitWall = head.x < 0 || head.y < 0 || head.x >= GRID || head.y >= GRID;
    // The tail moves away this step, so touching it is allowed
    var hitSelf = snake.slice(0, -1).some(function (p) { return p.x === head.x && p.y === head.y; });
    if (hitWall || hitSelf) return gameOver();

    snake.unshift(head);
    if (head.x === food.x && head.y === food.y) {
      score++;
      scoreEl.textContent = score;
      if (snake.length === GRID * GRID) return gameOver(true);
      placeFood();
      if (speed > MIN_SPEED) { // a little faster with every bite
        speed -= 3;
        clearInterval(timer);
        timer = setInterval(step, speed);
      }
    } else {
      snake.pop();
    }
    draw();
  }

  function gameOver(won) {
    clearInterval(timer);
    state = "over";
    if (score > best) {
      best = score;
      bestEl.textContent = best;
      try { localStorage.setItem(BEST_KEY, best); } catch (e) { /* storage blocked */ }
    }
    draw();
    msgEl.textContent = (won ? "Pobjeda! " : "Kraj igre! ") +
      "Razmak ili dodir za novu igru";
  }

  /* ---------- drawing ---------- */
  function color(name, fallback) {
    var v = getComputedStyle(document.body).getPropertyValue(name).trim();
    return v || fallback;
  }

  function roundRect(x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
    ctx.fill();
  }

  function draw() {
    var c = canvas.width / GRID;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // faint checkerboard
    ctx.fillStyle = color("--md-default-fg-color--lightest", "rgba(0,0,0,.07)");
    for (var y = 0; y < GRID; y++) {
      for (var x = (y % 2); x < GRID; x += 2) ctx.fillRect(x * c, y * c, c, c);
    }

    // food
    ctx.fillStyle = "#ff9100";
    ctx.beginPath();
    ctx.arc(food.x * c + c / 2, food.y * c + c / 2, c * 0.38, 0, Math.PI * 2);
    ctx.fill();

    // snake: head in full Milenij blue, body a little lighter
    snake.forEach(function (p, i) {
      ctx.fillStyle = i === 0 ? "#3d6299" : "#5279af";
      roundRect(p.x * c + 1, p.y * c + 1, c - 2, c - 2, c * 0.3);
    });

    // two eyes, side by side across the direction of travel
    var h = snake[0];
    ctx.fillStyle = "#fff";
    [-1, 1].forEach(function (side) {
      var ex = h.x * c + c / 2 + (dir.x ? dir.x * c * 0.15 : side * c * 0.18);
      var ey = h.y * c + c / 2 + (dir.y ? dir.y * c * 0.15 : side * c * 0.18);
      ctx.beginPath();
      ctx.arc(ex, ey, c * 0.09, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  /* ---------- controls ---------- */
  var KEYS = {
    ArrowUp: [0, -1], ArrowDown: [0, 1], ArrowLeft: [-1, 0], ArrowRight: [1, 0],
    w: [0, -1], s: [0, 1], a: [-1, 0], d: [1, 0],
    W: [0, -1], S: [0, 1], A: [-1, 0], D: [1, 0]
  };

  function onKey(e) {
    if (!overlay) return;
    // Keep the site's own shortcuts (search, previous/next page) out of the game
    e.stopImmediatePropagation();
    if (e.key === "Escape") { e.preventDefault(); return close(); }
    if (e.key === " " || e.key === "Enter") {
      if (e.target && e.target.closest && e.target.closest(".snake-close") && e.key === "Enter") return close();
      e.preventDefault();
      return state === "run" ? pause() : start();
    }
    if (e.key === "Tab") return; // keep focus inside the dialog reachable
    var k = KEYS[e.key];
    if (k) { e.preventDefault(); turn(k[0], k[1]); }
  }

  var touchX, touchY;
  function onTouchStart(e) {
    touchX = e.touches[0].clientX;
    touchY = e.touches[0].clientY;
  }
  function onTouchEnd(e) {
    if (touchX === undefined) return;
    var dx = e.changedTouches[0].clientX - touchX;
    var dy = e.changedTouches[0].clientY - touchY;
    touchX = undefined;
    if (Math.max(Math.abs(dx), Math.abs(dy)) < 20) return; // a tap, handled by click
    e.preventDefault();
    if (Math.abs(dx) > Math.abs(dy)) turn(dx > 0 ? 1 : -1, 0);
    else turn(0, dy > 0 ? 1 : -1);
  }
})();
