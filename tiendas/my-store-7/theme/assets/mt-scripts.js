/* MT — custom scripts (vanilla, one file for every page) */
(function () {
  var root = (window.Shopify && window.Shopify.routes && window.Shopify.routes.root) || '/';

  function money(cents, currency) {
    try {
      return new Intl.NumberFormat(document.documentElement.lang || 'en', { style: 'currency', currency: currency || 'USD' }).format(cents / 100);
    } catch (e) {
      return (cents / 100).toFixed(2);
    }
  }

  function initReveal() {
    var els = document.querySelectorAll('.mt-reveal');
    if (!els.length) return;
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      els.forEach(function (el) { el.classList.add('mt-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('mt-visible'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  function initGallery(scope) {
    var main = scope.querySelector('[data-mt-main-img]');
    if (!main) return;
    scope.querySelectorAll('[data-mt-thumb]').forEach(function (btn) {
      btn.addEventListener('click', function () { showMedia(scope, btn.getAttribute('data-mt-thumb')); });
    });
  }

  function showMedia(scope, mediaId) {
    var main = scope.querySelector('[data-mt-main-img]');
    var btn = scope.querySelector('[data-mt-thumb="' + mediaId + '"]');
    if (!main || !btn) return;
    main.src = btn.getAttribute('data-src');
    main.srcset = '';
    scope.querySelectorAll('[data-mt-thumb]').forEach(function (b) { b.classList.toggle('is-active', b === btn); });
  }

  function initQty(scope) {
    scope.querySelectorAll('[data-mt-qty]').forEach(function (wrap) {
      var input = wrap.querySelector('input');
      wrap.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function () {
          var v = parseInt(input.value, 10) || 1;
          v = b.hasAttribute('data-plus') ? v + 1 : Math.max(1, v - 1);
          input.value = v;
        });
      });
    });
  }

  function initCountdown(scope) {
    var el = scope.querySelector('[data-mt-countdown]');
    if (!el) return;
    var cutoff = parseInt(el.getAttribute('data-cutoff'), 10) || 15;
    var timer = el.querySelector('[data-mt-timer]');
    var weekdayText = el.querySelector('[data-mt-weekday]');
    var weekendText = el.querySelector('[data-mt-weekend]');
    function tick() {
      var now = new Date();
      var day = now.getDay();
      var end = new Date(now); end.setHours(cutoff, 0, 0, 0);
      var weekend = day === 0 || day === 6;
      if (!weekend && now >= end) {
        // after cutoff: count to tomorrow's cutoff (or Monday)
        end.setDate(end.getDate() + (day === 5 ? 3 : 1));
      }
      if (weekend) {
        if (weekdayText) weekdayText.hidden = true;
        if (weekendText) weekendText.hidden = false;
        return;
      }
      var diff = Math.max(0, end - now);
      var h = Math.floor(diff / 3600000), m = Math.floor(diff % 3600000 / 60000), s = Math.floor(diff % 60000 / 1000);
      if (timer) timer.textContent = h + 'h ' + (m < 10 ? '0' : '') + m + 'm ' + (s < 10 ? '0' : '') + s + 's';
    }
    tick();
    setInterval(tick, 1000);
  }

  function initProduct(scope) {
    var dataEl = scope.querySelector('[data-mt-variants]');
    if (!dataEl) return;
    var variants = JSON.parse(dataEl.textContent);
    var currency = scope.getAttribute('data-currency');
    var lowStock = parseInt(scope.getAttribute('data-low-stock'), 10) || 0;
    var idInput = scope.querySelector('[data-mt-variant-id]');
    var priceEl = scope.querySelector('[data-mt-price]');
    var wasEl = scope.querySelector('[data-mt-was]');
    var offEl = scope.querySelector('[data-mt-off]');
    var atc = scope.querySelectorAll('[data-mt-atc]');
    var stockLow = scope.querySelector('[data-mt-stock-low]');
    var stockOk = scope.querySelector('[data-mt-stock-ok]');
    var stockCount = scope.querySelector('[data-mt-stock-count]');
    var stockBar = scope.querySelector('[data-mt-stock-bar]');
    var stickyPrice = document.querySelector('[data-mt-sticky-price]');
    var labels = scope.querySelectorAll('[data-mt-opt-current]');

    function selected() {
      var vals = [];
      scope.querySelectorAll('[data-mt-option]').forEach(function (group) {
        var pos = parseInt(group.getAttribute('data-mt-option'), 10);
        var sel = group.querySelector('select');
        var checked = group.querySelector('input:checked');
        vals[pos] = sel ? sel.value : (checked ? checked.value : null);
      });
      return vals;
    }

    function update() {
      var vals = selected();
      var v = variants.find(function (x) { return x.options.every(function (o, i) { return vals[i] == null || o === vals[i]; }); });
      labels.forEach(function (l) { var p = parseInt(l.getAttribute('data-mt-opt-current'), 10); l.textContent = vals[p] || ''; });
      if (!v) {
        atc.forEach(function (b) { b.disabled = true; b.textContent = b.getAttribute('data-unavailable'); });
        return;
      }
      idInput.value = v.id;
      if (priceEl) priceEl.textContent = money(v.price, currency);
      if (stickyPrice) stickyPrice.textContent = money(v.price, currency);
      if (wasEl) {
        var onSale = v.compare > v.price;
        wasEl.hidden = !onSale; if (offEl) offEl.hidden = !onSale;
        if (onSale) {
          wasEl.textContent = money(v.compare, currency);
          if (offEl) offEl.textContent = '-' + Math.round((1 - v.price / v.compare) * 100) + '%';
        }
      }
      atc.forEach(function (b) {
        b.disabled = !v.available;
        b.textContent = v.available ? b.getAttribute('data-label') : b.getAttribute('data-soldout');
      });
      if (stockLow && stockOk) {
        var low = v.tracked && v.available && v.qty > 0 && v.qty <= lowStock;
        stockLow.hidden = !low; stockOk.hidden = low;
        if (low) {
          if (stockCount) stockCount.textContent = v.qty;
          if (stockBar) stockBar.style.width = Math.max(8, Math.round(v.qty / lowStock * 100)) + '%';
        }
      }
      if (v.media) showMedia(scope, String(v.media));
      if (window.history && window.history.replaceState) {
        var url = new URL(window.location.href); url.searchParams.set('variant', v.id);
        window.history.replaceState({}, '', url.toString());
      }
      scope.dispatchEvent(new CustomEvent('mt:variant', { detail: v }));
    }

    scope.querySelectorAll('[data-mt-option] input, [data-mt-option] select').forEach(function (el) {
      el.addEventListener('change', update);
    });
    update();
  }

  function initBundle(box) {
    var currency = box.getAttribute('data-currency');
    var pct = parseFloat(box.getAttribute('data-pct')) || 20;
    var btn = box.querySelector('[data-mt-bundle-add]');
    var msg = box.querySelector('[data-mt-bundle-msg]');
    var totalNow = box.querySelector('[data-mt-bundle-now]');
    var totalWas = box.querySelector('[data-mt-bundle-was]');
    var pdp = box.closest('[data-mt-product]');

    function priceOf(sel) {
      if (!sel) return 0;
      var opt = sel.options ? sel.options[sel.selectedIndex] : sel;
      return parseInt(opt.getAttribute('data-price'), 10) || 0;
    }
    function currentMainPrice() {
      var mainSel = box.querySelector('[data-mt-bundle-main]');
      if (mainSel) return priceOf(mainSel);
      return parseInt(box.getAttribute('data-main-price'), 10) || 0;
    }
    function recalc() {
      var sum = currentMainPrice();
      box.querySelectorAll('[data-mt-bundle-select]').forEach(function (s) { sum += priceOf(s); });
      if (totalWas) totalWas.textContent = money(sum, currency);
      if (totalNow) totalNow.textContent = money(Math.round(sum * (1 - pct / 100)), currency);
    }
    box.querySelectorAll('select').forEach(function (s) { s.addEventListener('change', recalc); });
    if (pdp) {
      pdp.addEventListener('mt:variant', function (e) {
        box.setAttribute('data-main-price', e.detail.price);
        box.setAttribute('data-main-id', e.detail.id);
        recalc();
      });
    }
    recalc();

    if (!btn) return;
    btn.addEventListener('click', function () {
      var items = [];
      var mainSel = box.querySelector('[data-mt-bundle-main]');
      var mainId = mainSel ? mainSel.value : box.getAttribute('data-main-id');
      if (mainId) items.push({ id: parseInt(mainId, 10), quantity: 1 });
      box.querySelectorAll('[data-mt-bundle-select]').forEach(function (s) { items.push({ id: parseInt(s.value, 10), quantity: 1 }); });
      btn.disabled = true;
      var label = btn.textContent;
      btn.textContent = btn.getAttribute('data-loading') || '…';
      fetch(root + 'cart/add.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ items: items })
      }).then(function (r) {
        if (!r.ok) return r.json().then(function (j) { throw new Error(j.description || j.message || 'Error'); });
        window.location.href = root + 'cart';
      }).catch(function (err) {
        btn.disabled = false; btn.textContent = label;
        if (msg) msg.textContent = err.message;
      });
    });
  }

  function initSticky() {
    var bar = document.querySelector('[data-mt-sticky]');
    var target = document.querySelector('[data-mt-atc-main]');
    if (!bar || !target || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      bar.classList.toggle('is-visible', !entries[0].isIntersecting && entries[0].boundingClientRect.top < 0);
    }).observe(target);
    var btn = bar.querySelector('button');
    if (btn) btn.addEventListener('click', function () { target.click(); });
  }

  function init() {
    initReveal();
    document.querySelectorAll('[data-mt-product]').forEach(function (p) {
      initGallery(p); initQty(p); initCountdown(p); initProduct(p);
    });
    document.querySelectorAll('[data-mt-bundle]').forEach(initBundle);
    initSticky();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  document.addEventListener('shopify:section:load', init);
})();
