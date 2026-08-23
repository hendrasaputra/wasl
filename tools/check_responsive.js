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
  const sheet = matchMedia('(max-width: 1100px)').matches;

  // 1. nothing may push the page sideways
  const ovf = document.documentElement.scrollWidth - document.documentElement.clientWidth;
  t('no horizontal page overflow', ovf === 0, ovf + 'px');

  // 2. chrome must not eat the screen - a phone budget, not a desktop one
  const chrome = H('header') + H('.bar') + H('.bar2') + H('#crumb');
  if (phone) t('chrome above the first name < 200px', chrome < 200, chrome + 'px');

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
    t('sheet sits within the viewport', r.bottom <= innerHeight + 2 && r.top < innerHeight,
       `top ${Math.round(r.top)} bottom ${Math.round(r.bottom)} vh ${innerHeight}`);
    t('sheet spans the width', Math.abs(r.width - innerWidth) < 2, Math.round(r.width) + '');
    document.querySelector('#sheetclose').click();
    t('sheet closes', !document.body.classList.contains('sheet-open'));
    panelEl.style.transition = prev;
  }

  // 4. touch targets - only meaningful where there is a touch
  const ctrls = [...document.querySelectorAll('.bar button, .chip, .seg button, #q, #sheetclose')]
    .filter(e => e.offsetParent && e.id !== 'bandhelp' && e.id !== 'aboutbtn');
  const small = ctrls.filter(e => e.getBoundingClientRect().height < 44)
                     .map(e => (e.id || e.className) + ':' + Math.round(e.getBoundingClientRect().height));
  if (phone) t('every control clears 44px', !small.length, small.join(' '));

  // 5. iOS zooms the page on focus below 16px and never zooms back
  if (phone) t('search input is 16px or larger',
     parseFloat(getComputedStyle(document.querySelector('#q')).fontSize) >= 16);

  // 5b. on a wide screen the panel must sit BESIDE the tree, not under it - the bug that
  // started this work was the columns view being added as a third child of a 2-column grid
  if (!sheet) {
    const st = document.querySelector('#stage').getBoundingClientRect();
    const pr = document.querySelector('#panel').getBoundingClientRect();
    t('panel sits beside the tree', pr.x > st.x + st.width - 6 && Math.abs(pr.y - st.y) < 200,
       `stage ${Math.round(st.x)}+${Math.round(st.width)}, panel ${Math.round(pr.x)}`);
    t('no sheet chrome on desktop',
       getComputedStyle(document.querySelector('#sheetbar')).display === 'none');
  }

  // 6. one column at a time on a phone
  if (phone) {
    document.querySelector('#vCols').click();
    const c = document.querySelector('#cols .col');
    t('columns fill the width', c && c.getBoundingClientRect().width >= innerWidth - 2);
    document.querySelector('#vTree').click();
  }

  // 7. the folded chrome must actually unfold
  if (phone) {
    document.querySelector('#filterbtn').click();
    t('filters open on demand', vis('.bar2'));
    document.querySelector('#filterbtn').click();
    document.querySelector('#aboutbtn').click();
    t('about opens on demand', vis('#about'));
    document.querySelector('#aboutbtn').click();
  }

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
  const budget = phone ? 240 : 320;
  t(`deepest indent under ${budget}px`, maxIndent <= budget, Math.round(maxIndent) + 'px');
  document.querySelectorAll('#tree details').forEach((d, i) => d.open = openState[i]);

  console.log(`${innerWidth}x${innerHeight}  ${ok.length} ok, ${fail.length} failed`);
  fail.forEach(f => console.log('  FAIL ' + f));
  return { w: innerWidth, h: innerHeight, chrome, passed: ok.length, failed: fail };
}
if (typeof module !== 'undefined') module.exports = { waslResponsiveCheck };
