  $(document).ready(function(){
    $('.sidenav').sidenav();
  });

  $('.carousel.carousel-slider').carousel({
      fullWidth: true,
      indicators: true
   });


   // move next carousel
   $('.moveNextCarousel').click(function(e){
      e.preventDefault();
      e.stopPropagation();
      $('.carousel').carousel('next');
   });

   // move prev carousel
   $('.movePrevCarousel').click(function(e){
      e.preventDefault();
      e.stopPropagation();
      $('.carousel').carousel('prev');
   });

   $(document).ready(function(){
    $('.datepicker').datepicker({
    	format: 'yyyy-mm-dd'
    });
  });
   $('.datepicker').click(function() {
    pickr.pickadate('open');
  });

     $(document).ready(function(){
    $('select').formSelect();
  });
      $(document).ready(function(){
    $('.tabs').tabs();
  });
