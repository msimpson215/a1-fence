(function (g) {
  var PLATE = '/email-plate.html';
  var NAME = 'axon_plate';
  var W = 236;
  var H = 236;

  function plateUrl(params, origin) {
    var q = new URLSearchParams();
    q.set('src', (params && params.src) || 'email');
    q.set('popup', '1');
    return (origin || g.location.origin) + PLATE + '?' + q;
  }

  function features() {
    var l = Math.round(((g.screen.width || 1200) - W) / 2);
    var t = Math.round(((g.screen.height || 800) - H) / 2);
    return 'popup=yes,width='+W+',height='+H+',left='+l+',top='+t+
      ',toolbar=no,menubar=no,location=no,status=no,resizable=no,scrollbars=no';
  }

  function jsFeatures() {
    return 'popup=yes,width='+W+',height='+H+
      ",left='+(screen.width-"+W+")/2,top='+(screen.height-"+H+")/2"+
      ',toolbar=no,menubar=no,location=no,status=no,resizable=no,scrollbars=no';
  }

  function openEmailOrb(params, origin) {
    return g.open(plateUrl(params, origin), NAME, features());
  }

  function buildPlateUrl(params, origin) {
    return plateUrl(params, origin);
  }

  g.AxonEmailOrb = {
    openEmailOrb: openEmailOrb,
    buildPlateUrl: buildPlateUrl,
    javascriptHyperlink: function (params, origin) {
      var u = plateUrl(params, origin).replace(/'/g, '%27');
      return "javascript:void(window.open('"+u+"','"+NAME+"',"+jsFeatures()+'))';
    }
  };
})(window);
