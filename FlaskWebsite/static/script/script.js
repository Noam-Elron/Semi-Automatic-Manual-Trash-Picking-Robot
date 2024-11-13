$(document).ready(function() {
    $( "div[name='button']" ).on('click', function() {
      $.ajax({
        url: '/clicks',
        type: 'post',
        data: {
          direction: $(this).attr("id")
        },
        success: function(response){
          $(".text1").text(response);
        }
      
      
      })
    })
  })