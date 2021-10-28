// Input Image
$(document).ready(function(){
    $('#uploadImage').submit(function(event){
        if($('#uploadFile').val()){
            event.preventDefault();
            disableDownloadBtn();
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
                    $('#Enhancement-btn').show()
                },
                resetForm: true
            });
        }
        return false;
    });
});


$(function() {
    // Runs analyseHE from web.py
  $('#he').on('click', function(e) {
      e.preventDefault();
      disableDownloadBtn();
      $('#instructions').hide();
      $('#process-icon').show();
      $('#displayLayer').hide();
      $('#download-btn').hide();
      clearBox('displayLayer');

      $.getJSON('/he',
        function(data) {
        $('#instructions').hide();
        $('#process-icon').hide();
        $('#displayLayer').append(data.htmlresponse).show();
         $('#download-btn').show();
        enableDownloadBtn();
      });

      return false;
  });


  // Runs analyseDHE from app.py
  $('#dhe').on('click', function(e) {
    e.preventDefault();
    disableDownloadBtn();
    $('#instructions').hide();
    $('#process-icon').show();
    $('#displayLayer').hide();
    $('#download-btn').hide();
    clearBox('displayLayer');

    $.getJSON('/dhe',
    function(data) {
        $('#instructions').hide();
        $('#process-icon').hide();
        $('#displayLayer').append(data.htmlresponse).show();
         $('#download-btn').show();
        enableDownloadBtn();
    });
    return false;
  });


// Runs analyseEFF from app.py
  $('#eff').on('click', function(e) {
    e.preventDefault();
    disableDownloadBtn();
    $('#instructions').hide();
    $('#process-icon').show();
    $('#displayLayer').hide();
    $('#download-btn').hide();
    clearBox('displayLayer');

    $.getJSON('/eff',
    function(data) {
        $('#instructions').hide();
        $('#process-icon').hide();
        $('#displayLayer').append(data.htmlresponse).show();
        $('#download-btn').show();
        enableDownloadBtn();
    });
    return false;
  });
});


function clearBox(elementID) {
    let div = document.getElementById(elementID);
    while(div.firstChild) {
        div.removeChild(div.firstChild);
    }
}

function disableDownloadBtn() {
    document.getElementById("download-btn").disabled = true;
}

function enableDownloadBtn() {
    document.getElementById("download-btn").disabled = false;
}