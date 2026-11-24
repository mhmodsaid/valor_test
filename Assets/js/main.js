(function () {
  'use strict';

  // ----- mobile navigation -----
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    var setOpen = function (open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? 'Close' : 'Menu';
    };
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  // ----- enquiry form -----
  // If the form action still contains YOUR_FORM_ID (no form service connected yet),
  // fall back to opening the visitor's email app with the enquiry pre-filled.
  var form = document.getElementById('enquiry-form');
  if (!form) return;
  var status = document.getElementById('form-status');

  form.addEventListener('submit', function (e) {
    if (form.querySelector('.hp input').value) { e.preventDefault(); return; } // spam trap

    var usesFallback = form.getAttribute('action').indexOf('YOUR_FORM_ID') !== -1;
    if (usesFallback) {
      e.preventDefault();
      var d = new FormData(form);
      var body = [
        'Name: ' + d.get('name'),
        'Business email: ' + d.get('email'),
        'Company: ' + d.get('company'),
        'Country: ' + d.get('country'),
        'Enquiry type: ' + d.get('type'),
        '',
        d.get('message')
      ].join('\n');
      window.location.href = 'mailto:Info@valor-ksa.com?subject=' +
        encodeURIComponent('Website enquiry: ' + d.get('type')) +
        '&body=' + encodeURIComponent(body);
      status.textContent = 'Your email app should open with the enquiry ready to send. If it does not, write to Info@valor-ksa.com.';
      return;
    }

    // Real endpoint: submit in the background so we can confirm on the page.
    e.preventDefault();
    status.textContent = 'Sending…';
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('bad status');
        form.reset();
        status.textContent = 'Thank you. We have your enquiry and will reply by email.';
      })
      .catch(function () {
        status.textContent = 'The enquiry could not be sent. Please email Info@valor-ksa.com or call +966 56 059 2662.';
      });
  });
})();
