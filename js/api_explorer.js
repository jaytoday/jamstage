$(function(){

$address_bar = $('#address_bar');
$address_input = $address_bar.find('.input:first').find('input');

$nav_apis = $('.nav-api');
$method_groups = $('.api-methods');
$methods = $('.nav-method');
$descriptions = $('.description');
$address_submit = $address_bar.find('a#submit');


$address_submit.click(function(){

  $api_responses = $('#api_response').find('.response_container');
  $api_responses.filter('.show').hide(500);
  setTimeout(refreshResponse, 1000);
});


$methods.click(function(){
   $(this).siblings().removeClass('clicked');
  $(this).addClass('clicked'); 
  $address_bar.find('span.path').text($(this).attr('id'));
  $descriptions.filter('[id=' + $(this).attr('id') + ']')
    .siblings().hide().end()
    .show();

  $address_input.attr('value', '?' + $(this).attr('query'));
   $address_submit.click(); 
  
});

$nav_apis.click(function(){

  $(this).siblings().removeClass('clicked');
  $(this).addClass('clicked');
  
  var $this_group = $method_groups.filter('[id=' + $(this).attr('id') + ']');
  
  $this_group.siblings().hide().removeClass('show');
  
  var $clicked_method = $this_group.find('.nav-method.clicked:first');
  if ($clicked_method.length > 0)
     $clicked_method.click(); 
  else $this_group.find('.nav-method:first').click();
  $this_group.show().addClass('show');
  
  });
  
setTimeout(function(){ $nav_apis.filter(':first').click();  }, 50);





function refreshResponse(){
  

  $this_method = $('.api-methods.show:first').find('.nav-method.clicked:first');
  
  
  
  $this_response = $('#api_response').find('.response_container').filter('[id=' + $this_method.attr('id') + ']');

  
  $this_response.addClass('show').show(500);
}




});


