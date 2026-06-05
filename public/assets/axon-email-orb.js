/**
 * Axon Email Orb — opens a chromeless popup so the orb appears to sit on top of Gmail.
 * Gmail only allows links/images; the conversation runs on Axon (never inside Google).
 */
(function (global) {
  var POPUP_PATH = '/ai-talk-popup.html';
  var WIDTH = 400;
  var HEIGHT = 580;
  var WINDOW_NAME = 'AxonAI';

  function buildPopupUrl(params, origin) {
    var base = (origin || (global.location && global.location.origin) || '') + POPUP_PATH;
    var q = new URLSearchParams();
    if (params && params.biz) q.set('biz', params.biz);
    if (params && params.tagline) q.set('tagline', params.tagline);
    if (params && params.logo) q.set('logo', params.logo);
    if (params && params.chat) q.set('chat', params.chat);
    var s = q.toString();
    return s ? base + '?' + s : base;
  }

  function popupFeatures() {
    var left = Math.max(0, Math.round(((global.screen && global.screen.width) || 1200) - WIDTH) / 2);
    var top = Math.max(0, Math.round(((global.screen && global.screen.height) || 800) - HEIGHT) / 2);
    return (
      'width=' + WIDTH +
      ',height=' + HEIGHT +
      ',left=' + left +
      ',top=' + top +
      ',toolbar=no,menubar=no,location=no,status=no,resizable=yes,scrollbars=no'
    );
  }

  function centeredPopupFeatures() {
    return (
      'width=' + WIDTH +
      ',height=' + HEIGHT +
      ",left='+(screen.width-" + WIDTH + ")/2" +
      ",top='+(screen.height-" + HEIGHT + ")/2" +
      ',toolbar=no,menubar=no,location=no,status=no,resizable=yes,scrollbars=no'
    );
  }

  function openEmailOrb(params, origin) {
    var url = buildPopupUrl(params || {}, origin);
    return global.open(url, WINDOW_NAME, popupFeatures());
  }

  /** For pasting on a Gmail image hyperlink — centers on the reader's screen at click time. */
  function javascriptHyperlink(params, origin) {
    var url = buildPopupUrl(params || {}, origin).replace(/'/g, '%27');
    return (
      "javascript:void(window.open('" +
      url +
      "','" +
      WINDOW_NAME +
      "'," +
      centeredPopupFeatures() +
      '))'
    );
  }

  function httpsHyperlink(params, origin) {
    return buildPopupUrl(params || {}, origin);
  }

  global.AxonEmailOrb = {
    POPUP_PATH: POPUP_PATH,
    WIDTH: WIDTH,
    HEIGHT: HEIGHT,
    buildPopupUrl: buildPopupUrl,
    openEmailOrb: openEmailOrb,
    javascriptHyperlink: javascriptHyperlink,
    httpsHyperlink: httpsHyperlink
  };
})(typeof window !== 'undefined' ? window : this);
