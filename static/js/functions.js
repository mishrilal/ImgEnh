$(function() {
    $('#upload').click(function(){
        var fd = new FormData($('#file')[0]);
        fd.stopPropogation();
        $.ajax({
            type: 'POST',
            url: '/',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                // Hide Upload Img Block and Display Image
                document.getElementById("first").style.display ='block';
                document.getElementById("uploadForm").style.display='none';
            },
        });
    });
});

// Runs analyseDHE from web.py
$(function() {
  $('#dhe').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/dhe',
        function(data) {
      //do nothing
    });
    showDImg()
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
    showDImg()
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
                    $('#targetLayer').show();
                    $('#targetLayer').append(data.htmlresponse);
                },
                resetForm: true
            });
        }
        return false;
    });
});

const myFunction = () => {
  document.getElementById("first").style.display ='block';
  document.getElementById("uploadForm").style.display='none';
}

const showDImg = () => {
    document.getElementById("downloadImg").style.display='block';
}
