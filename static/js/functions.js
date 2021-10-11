// Runs analyseDHE from web.py
$(function() {
  $('#dhe').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/dhe',
        function(data) {
      //do nothing
    });
    return false;
  });
});

// Runs analyseHE from web.py
$(function() {
  $('#he').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/he',
        function(data) {
      //do nothing
    });
    return false;
  });
});

// Runs analyseEFF from web.py
$(function() {
  $('#eff').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/eff',
        function(data) {
      //do nothing
    });
    return false;
  });
});



