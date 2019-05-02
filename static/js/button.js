// SOUND WAVE BUTTON jQuery
jQuery(function($) {
    $('#btn-play').on('click', function() {
      var $el = $(this)
      
      $el.toggleClass('toggler');
      console.log($el.attr('id'));
      
      $el.attr('id', 'btn-pause')
      $el.attr('value', 'Pause')
      $el.find('i').toggleClass('fa fa-play fa fa-pause');
      });
    
    $('#btn-play2').on('click', function() {
      var $el = $(this)
      
      $el.toggleClass('toggler');
      console.log($el.attr('id'));
      
      $el.attr('id', 'btn-pause2')
      $el.attr('value', 'Pause')
      $el.find('i').toggleClass('fa fa-play fa fa-pause');
      });
  });
  
  jQuery(function($) {
      $('#btn-pause').on('click', function() {
        var $el = $(this)
        console.log($el.attr('id'));
        
      $el.attr('id', 'btn-play')
      $el.attr('value', 'Play')
      $el.find('i').toggleClass('fa fa-play fa fa-play');
      });
      
      $('#btn-pause2').on('click', function() {
        var $el = $(this)
        console.log($el.attr('id'));
        
      $el.attr('id', 'btn-play2')
      $el.attr('value', 'Play')
      $el.find('i').toggleClass('fa fa-play fa fa-play');
      });
    });