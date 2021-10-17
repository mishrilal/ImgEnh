// Input Image
$(document).ready(function(){
    $('#uploadImage').submit(function(event){
        if($('#uploadFile').val()){
            event.preventDefault();
            $('#upload-form').hide();
            $('#upload-btn').hide();
            // $('#progress-bar').show();
            $('#loader-icon').show();
            $('#targetLayer').hide();
            $(this).ajaxSubmit({
                target: '#targetLayer',
                beforeSubmit:function(){
                    $('.progress-bar').width('0%');
                },
                uploadProgress: function(event, position, total, percentageComplete)
                {
                    $('.progress-bar').animate({
                        width: percentageComplete + '%'
                    }, {
                        duration: 1000
                    });
                },
                success:function(data){
                    $('#loader-icon').hide();
                    $('#targetLayer').append(data.htmlresponse).show();
                },
                resetForm: true
            });
        }
        return false;
    });
});

// Runs analyseDHE from web.py
$(function() {
  $('#dhe').on('click', function(e) {
    e.preventDefault();
      $('#process-icon').show();
      $('#displayLayer').hide();
      clearBox('displayLayer');

      $.getJSON('/dhe',
        function(data) {
        console.log("in function");
        $('#process-icon').hide();
        $('#displayLayer').append(data.htmlresponse).show();
      });
    return false;
  });
});

// Runs analyseHE from web.py
$(function() {
    console.log("in Main Function");
  $('#he').on('click', function(e) {
      console.log("Above Function")
      e.preventDefault();
      $('#process-icon').show();
      $('#displayLayer').hide();
      clearBox('displayLayer');

      $.getJSON('/he',
        function(data) {
        console.log("in function");
        $('#process-icon').hide();
        $('#displayLayer').append(data.htmlresponse).show();
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

function clearBox(elementID) {
    var div = document.getElementById(elementID);
    while(div.firstChild) {
        div.removeChild(div.firstChild);
    }
}