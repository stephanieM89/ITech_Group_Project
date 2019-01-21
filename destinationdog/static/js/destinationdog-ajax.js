  $( document ).ready(function() {
      function vote() {
          var dotmid;
          dotmid = $(this).attr("data-dotmid");
          $.get('/destinationdog/like/', {dotmid: dotmid}, function (data) {
              $(`#like_count-${dotmid}`).html(data);
              $(this).hide();
          });
      };

    var votes = $('.likes');
    for(var i = 0; i < votes.length; i++){
        $(votes[i]).click(vote);
    }
  });

