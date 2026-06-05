/**
 * Plate on Gmail's table: tall shaded window, solid yellow orb + logo in center.
 * Everything around the orb is transparent/semi-shaded so Gmail shows through.
 */
(function (global) {
  var LAUNCH_PATH = '/launch.html';
  var PLATE_PATH = '/email-plate.html';
  var WINDOW_NAME = 'axon_plate';

  function popupSize() {
    var sw = (global.screen && global.screen.width) || 1200;
    var sh = (global.screen && global.screen.height) || 800;
    return {
      width: Math.min(560, Math.round(sw * 0.92)),
      height: Math.min(Math.round(sh * 0.88), sh - 40),
      left: Math.max(0, Math.round((sw - Math.min(560, sw * 0.92)) / 2)),
      top: Math.max(0, Math.round((sh - Math.min(Math.round(sh * 0.88), sh - 40)) / 2))
    };
  }

  function buildLaunchUrl(params, origin) {
    var base = (origin || (global.location && global.location.origin) || '') + LAUNCH_PATH;
    var q = new URLSearchParams();
    q.set('src', (params && params.src) || 'email');
    if (params && params.biz) q.set('biz', params.biz);
    if (params && params.logo) q.set('logo', params.logo);
    return base + '?' + q.toString();
  }

  function buildPlateUrl(params, origin) {
    var base = (origin || (global.location && global.location.origin) || '') + PLATE_PATH;
    var q = new URLSearchParams();
    q.set('src', (params && params.src) || 'email');
    q.set('popup', '1');
    if (params && params.biz) q.set('biz', params.biz);
    if (params && params.logo) q.set('logo', params.logo);
    return base + '?' + q.toString();
  }

  function popupFeatures() {
    var s = popupSize();
    return (
      'popup=yes,width=' + s.width +
      ',height=' + s.height +
      ',left=' + s.left +
      ',top=' + s.top +
      ',toolbar=no,menubar=no,location=no,status=no,resizable=no,scrollbars=no'
    );
  }

  function centeredPopupFeatures() {
    var sw = (global.screen && global.screen.width) || 1200;
    var sh = (global.screen && global.screen.height) || 800;
    var w = Math.min(560, Math.round(sw * 0.92));
    var h = Math.min(Math.round(sh * 0.88), sh - 40);
    return (
      'popup=yes,width=' + w +
      ',height=' + h +
      ",left='+(screen.width-" + w + ")/2" +
      ",top='+(screen.height-" + h + ")/2" +
      ',toolbar=no,menubar=no,location=no,status=no,resizable=no,scrollbars=no'
    );
  }

  function openEmailOrb(params, origin) {
    return global.open(buildPlateUrl(params || {}, origin), WINDOW_NAME, popupFeatures());
  }

  function javascriptHyperlink(params, origin) {
    var url = buildPlateUrl(params || {}, origin).replace(/'/g, '%27');
    return "javascript:void(window.open('" + url + "','" + WINDOW_NAME + "'," + centeredPopupFeatures() + '))';
  }

  function httpsHyperlink(params, origin) {
    return buildLaunchUrl(params || {}, origin);
  }

  global.AxonEmailOrb = {
    LAUNCH_PATH: LAUNCH_PATH,
    PLATE_PATH: PLATE_PATH,
    buildLaunchUrl: buildLaunchUrl,
    buildPlateUrl: buildPlateUrl,
    openEmailOrb: openEmailOrb,
    javascriptHyperlink: javascriptHyperlink,
    httpsHyperlink: httpsHyperlink
  };
})(typeof window !== 'undefined' ? window : this);
