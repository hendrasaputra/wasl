// SPDX-License-Identifier: GPL-3.0-or-later
// Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
//
// Responsive assertions, run in the page console (or by a headless driver).
// Same discipline as the data: measure, do not eyeball.
//   copy this file's contents into the console at each viewport, or call
//   waslResponsiveCheck() after resizing.
function waslResponsiveCheck() {
  const fail = [], ok = [];
  const t = (name, cond, detail = '') => (cond ? ok : fail).push(name + (cond ? '' : '  <-- ' + detail));
  const vis = s => { const e = document.querySelector(s); return e && !e.hidden && e.offsetParent !== null; };
  const H = s => vis(s) ? Math.round(document.querySelector(s).getBoundingClientRect().height) : 0;

  scrollTo(0, 0);
  const phone = matchMedia('(max-width: 760px)').matches;
  // The bio pages have their own shell. Everything below that touches the tree page's
  // furniture is gated on `tree`, so one checker covers both without pretending the
  // missing elements passed.
  const tree = !!document.getElementById('tree');
  const sheet = tree && matchMedia('(max-width: 1100px)').matches;
  // The front door (index.html) shows one person and their thread. Its assertions are gated
  // on #thread, the tree explorer's (tree.html) on #tree, so one checker covers both.
  const thread = !!document.getElementById('thread');
  if (thread) {
    // the front page: the people to start from must be reachable within two screens
    location.hash = ''; render();
    const first = document.querySelector('#groups .card');
    t('front page offers a person within two screens', first && first.getBoundingClientRect().top < innerHeight * 2,
      first ? Math.round(first.getBoundingClientRect().top) + 'px' : 'no cards');
    t('front page search is the one search', document.querySelectorAll('#q').length === 1
      && document.querySelector('#hs #q') !== null);
    // a person: the name, the thread and the first source must all be there
    location.hash = 'p.muhammad'; render();
    const name = document.querySelector('.crown .name');
    t('person name sits in the first screen', name && name.getBoundingClientRect().top < innerHeight);
    t('thread nodes are native links', [...document.querySelectorAll('.thread .node')]
      .every(a => a.tagName === 'A' && a.getAttribute('href')));
    t('the person is the large bead on the thread', !!document.querySelector('.thread li.me .node'));
    t('every link on the thread carries its sources', document.querySelectorAll('.thread .edge').length >= 5);
    document.querySelector('.thread .edge').click();
    t('a link opens its quotations in place', !!document.querySelector('.thread .edgeq .cl .q'));
    t('the brief is shown for a person who has one', !!document.querySelector('.brief p'));
    t('the first group of sources is open', !!document.querySelector('.books details[open] .cl'));
    const small = [...document.querySelectorAll('.thread .node, .pill, .chip, #q, .cta')]
      .filter(e => e.offsetParent && e.getBoundingClientRect().height < 44)
      .map(e => (e.id || e.className) + ':' + Math.round(e.getBoundingClientRect().height));
    if (phone) t('every person control clears 44px', !small.length, small.slice(0, 6).join(' '));
    if (!phone && innerWidth > 900) {
      const th = document.querySelector('#thread').getBoundingClientRect(), lf = document.querySelector('#life').getBoundingClientRect();
      t('thread sits beside the life on a wide screen', lf.left > th.right - 2 && Math.abs(lf.top - th.top) < 40);
    }
  }
  if (tree) {
    const pseudo = [...document.querySelectorAll('[data-go]')]
      .filter(el => el.tagName !== 'A' || !el.getAttribute('href'));
    t('person navigation uses native links', !pseudo.length,
      pseudo.slice(0, 3).map(el => el.outerHTML.slice(0, 80)).join(' '));
  }

  // 1. nothing may push the page sideways
  const ovf = document.documentElement.scrollWidth - document.documentElement.clientWidth;
  t('no horizontal page overflow', ovf === 0, ovf + 'px');

  // 2. chrome must not eat the screen - a phone budget, not a desktop one
  const chrome = H('header') + H('.bar') + H('.bar2') + H('#crumb');
  if (phone && tree) t('chrome above the first name < 200px', chrome < 200, chrome + 'px');

  // 2b. Who's who is the only route to a named person that does not require typing one, so it
  // must be reachable without opening anything first. It lived in .bar2 - which folds away on
  // a phone - so on a small screen it sat behind a button labelled 'Filter', which is to say
  // nowhere. Assert the button itself, not just that the markup contains it.
  const db = document.querySelector('#dirbtn');
  const dbr = db && db.getBoundingClientRect();
  if (tree) t("Who's who is reachable without opening a panel",
    !!db && db.offsetParent !== null && dbr.width > 0 && dbr.height >= (phone ? 44 : 24),
    db ? `${Math.round(dbr.width)}x${Math.round(dbr.height)}, offsetParent=${!!db.offsetParent}` : 'missing');

  // 2c. The biography pages have their own shell, so they need their own assertions. Skipped
  // silently on the tree page, where none of these elements exist.
  const sum = document.getElementById('sum');
  if (sum) {
    const first = document.querySelector('#sum .prose .sl');
    t('the brief starts within one screen', first.getBoundingClientRect().top < innerHeight,
      Math.round(first.getBoundingClientRect().top) + 'px');
    // WCAG 2.2 AA asks 24x24 for a pointer target. The page superscript is 16x13 and is
    // grown by an ::after overlay, so measure the overlay, not the glyph.
    const sp = document.querySelector('.sp');
    if (sp) {
      const a = getComputedStyle(sp, '::after');
      const w = sp.getBoundingClientRect().width - parseFloat(a.left) - parseFloat(a.right);
      const h = sp.getBoundingClientRect().height - parseFloat(a.top) - parseFloat(a.bottom);
      t('page marks clear a 24px pointer target', w >= 24 && h >= 24,
        `${Math.round(w)}x${Math.round(h)}`);
    }
    // A page number that repeats the one before it is noise in running prose.
    const marks = [...document.querySelectorAll('.sp')].map(a => a.textContent);
    t('no page mark repeats the one before it',
      !marks.some((m, i) => i && m === marks[i - 1]));
    // The note describes the Arabic entry, so it must sit with it rather than above the brief.
    const note = document.querySelector('.note');
    t('the entry note sits below the brief, with what it describes',
      !note || (sum.compareDocumentPosition(note) & Node.DOCUMENT_POSITION_FOLLOWING) !== 0);
  }

  // 3. the citations must be reachable without scrolling past the tree
  if (sheet) {
    // the sheet animates in over 280ms; measuring mid-transition is a race, not a finding
    const panelEl = document.querySelector('#panel');
    const prev = panelEl.style.transition;
    panelEl.style.transition = 'none';
    document.querySelector('summary[data-id]').click();
    panelEl.getBoundingClientRect();          // force layout with the transition disabled
    const open = document.body.classList.contains('sheet-open');
    const r = document.querySelector('#panel').getBoundingClientRect();
    t('tapping a name opens the sheet', open);
    t('sheet exposes modal dialog semantics', panelEl.getAttribute('role') === 'dialog'
      && panelEl.getAttribute('aria-modal') === 'true');
    t('sheet sits within the viewport', r.bottom <= innerHeight + 2 && r.top < innerHeight,
       `top ${Math.round(r.top)} bottom ${Math.round(r.bottom)} vh ${innerHeight}`);
    t('sheet spans the width', Math.abs(r.width - innerWidth) < 2, Math.round(r.width) + '');
    document.querySelector('#sheetclose').click();
    t('sheet closes', !document.body.classList.contains('sheet-open'));
    t('closed sheet leaves the accessibility tree', panelEl.getAttribute('aria-hidden') === 'true');
    panelEl.style.transition = prev;
  }

  // 4. touch targets - only meaningful where there is a touch
  const ctrls = [...document.querySelectorAll('.bar button, .chip, .seg button, #q, #sheetclose')]
    .filter(e => e.offsetParent && e.id !== 'bandhelp' && e.id !== 'aboutbtn');
  const small = ctrls.filter(e => e.getBoundingClientRect().height < 44)
                     .map(e => (e.id || e.className) + ':' + Math.round(e.getBoundingClientRect().height));
  if (phone && tree) t('every control clears 44px', !small.length, small.join(' '));

  // 5. iOS zooms the page on focus below 16px and never zooms back
  if (phone && (tree || thread)) t('search input is 16px or larger',
     parseFloat(getComputedStyle(document.querySelector('#q')).fontSize) >= 16);

  // 5b. on a wide screen the panel must sit BESIDE the tree, not under it - the bug that
  // started this work was the columns view being added as a third child of a 2-column grid
  if (tree && !sheet) {
    const st = document.querySelector('#stage').getBoundingClientRect();
    const pr = document.querySelector('#panel').getBoundingClientRect();
    t('panel sits beside the tree', pr.x > st.x + st.width - 6 && Math.abs(pr.y - st.y) < 200,
       `stage ${Math.round(st.x)}+${Math.round(st.width)}, panel ${Math.round(pr.x)}`);
    t('no sheet chrome on desktop',
       getComputedStyle(document.querySelector('#sheetbar')).display === 'none');
  }

  // 6. one column at a time on a phone
  if (phone && tree) {
    document.querySelector('#vCols').click();
    const c = document.querySelector('#cols .col');
    t('columns fill the width', c && c.getBoundingClientRect().width >=
      document.documentElement.clientWidth - 2,
      c ? `${Math.round(c.getBoundingClientRect().width)}px of ${document.documentElement.clientWidth}px` : 'missing');
    t('column rows use native buttons',
      [...document.querySelectorAll('.ci')].every(el => el.tagName === 'BUTTON'));
    document.querySelector('#vTree').click();
  }

  // 7. the folded chrome must actually unfold
  if (phone && tree) {
    document.querySelector('#filterbtn').click();
    t('filters open on demand', vis('.bar2'));
    document.querySelector('#filterbtn').click();
    document.querySelector('#aboutbtn').click();
    t('about opens on demand', vis('#about'));
    document.querySelector('#aboutbtn').click();
  }

  if (tree) {
    // 8. indentation: bounded, and still strictly monotonic. The diminishing scale is only safe
    //    because every child stays right of its parent - if a band ever flattened that, the tree
    //    would start lying about who descends from whom.
    const openState = [...document.querySelectorAll('#tree details')].map(d => d.open);
    document.querySelectorAll('#tree details').forEach(d => d.open = true);
    let bad = 0, pairs = 0;
    document.querySelectorAll('#tree details').forEach(d => {
      const ps = d.querySelector(':scope > summary');
      const kd = d.querySelector(':scope > .kids:not(.linear)');
      if (!ps || !kd) return;
      const cs = kd.querySelector(':scope > details > summary');
      if (!cs) return;
      pairs++;
      if (cs.getBoundingClientRect().left <= ps.getBoundingClientRect().left) bad++;
    });
    t('every child indents right of its parent', bad === 0, `${bad} of ${pairs} pairs`);
    const tre = document.querySelector('#tree');
    const tl = tre.getBoundingClientRect().left;
    const maxIndent = Math.max(...[...document.querySelectorAll('#tree summary')]
      .map(s => s.getBoundingClientRect().left - tl));
    // What matters is not the indent in pixels but whether a name still has room to be read at
    // the deepest point. A raw px budget was the wrong proxy: it punishes a zoomed-down tree that
    // is in fact more readable, and it rewards shrinking text that nobody can read.
    const room = tre.clientWidth - maxIndent;
    const pct = Math.round(100 * room / tre.clientWidth);
    t('a name still has half the width at the deepest node', pct >= 45,
       `${Math.round(room)}px of ${tre.clientWidth}px (${pct}%)`);
    t('deepest indent is bounded', maxIndent <= (phone ? 300 : 360), Math.round(maxIndent) + 'px');
    document.querySelectorAll('#tree details').forEach((d, i) => d.open = openState[i]);
  }

  console.log(`${innerWidth}x${innerHeight}  ${ok.length} ok, ${fail.length} failed`);
  fail.forEach(f => console.log('  FAIL ' + f));
  return { w: innerWidth, h: innerHeight, chrome, passed: ok.length,
           failed: fail.length, errors: fail };
}
if (typeof module !== 'undefined') module.exports = { waslResponsiveCheck };
if (new URLSearchParams(location.search).has('responsive-check')) {
  try {
    const result = waslResponsiveCheck();
    document.documentElement.dataset.responsiveFailed = result.failed;
    if (result.errors.length)
      document.documentElement.dataset.responsiveError = result.errors.join(' | ');
  } catch (error) {
    document.documentElement.dataset.responsiveFailed = 'runtime-error';
    document.documentElement.dataset.responsiveError = String(error.message || error);
    console.error(error);
  }
}
