$(function(){

$address_bar = $('#address_bar');
$nav_apis = $('.nav-api');
$method_groups = $('.api-methods');
$methods = $('.nav-method');
$descriptions = $('.description');

$methods.click(function(){
   $(this).siblings().removeClass('clicked');
  $(this).addClass('clicked'); 
  $address_bar.find('span.path').text($(this).attr('id'));
  $descriptions.filter('[id=' + $(this).attr('id') + ']')
    .siblings().hide().end()
    .show();
  
});

$nav_apis.click(function(){
  $(this).siblings().removeClass('clicked');
  $(this).addClass('clicked');
  
  var $this_group = $method_groups.filter('#' + $(this).attr('id'));
  
  $this_group.siblings().hide();
  
  var $clicked_method = $this_group.find('.nav-method.clicked:first');
  if ($clicked_method.length > 0)
     $clicked_method.click(); 
  else $this_group.find('.nav-method:first').click();
  $this_group.show();
  
  }).filter(':first').click();  


});
