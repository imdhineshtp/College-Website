// address copy functions


$('#yes').bind('change', function () {

    if ($('#yes').is(':checked'))
    {
      $('#id_Address').change(function() {
     $('#id_Permanent_Address').val($(this).val());
    });
    $('#id_Taluk').change(function() {
        $('#id_Per_Taluk').val($(this).val());
    });
    $('#id_State').change(function() {
        $('#id_Per_State').val($(this).val());
    });
    $('#id_Dist').change(function() {
        $('#id_Per_Dist').val($(this).val());
    });
    $('#id_Pin_Code').change(function() {
        $('#id_Per_Pin_Code').val($(this).val());
  });
  }
  
   else{
   $('#id_Address').change(function() {
    $('#id_Permanent_Address').val($('').val());
  });
  $('#id_Taluk').change(function() {
   $('#id_Per_Taluk').val($('').val());
  });
  $('#id_State').change(function() {
   $('#id_Per_State').val($('').val());
  });
  $('#id_Dist').change(function() {
   $('#id_Per_Dist').val($('').val());
  });
  $('#id_Pin_Code').change(function() {
   $('#id_Per_Pin_Code').val($('').val());
  });}
  
  });

//   image preview function
$(function() {
    $("#id_Image").on('change', function() {
      // Display image on the page for viewing
  
      readURL(this, "profile_pic");
  
    });
  });
  
  
  $(function() {
    $("#id_Sign").on('change', function() {
      // Display image on the page for viewing
      readURL(this, "signature");
  
    });
  });
  
  function readURL(input, tar) {
    if (input.files && input.files[0]) { // got sth
      
      $("#"+ tar).removeClass("d-none");
      // Clear image container
      $("#" + tar).removeAttr('src');
  
      $.each(input.files, function(index, ff) // loop each image 
        {
  
          var reader = new FileReader();
  
          // Put image in created image tags
          reader.onload = function(e) {
            $('#' + tar).attr('src', e.target.result);
          }
  
          reader.readAsDataURL(ff);
  
        });
    }
  }
  
  