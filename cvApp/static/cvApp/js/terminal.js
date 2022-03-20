$(document).ready(function(){
	$('.minimize').on('click', function(){minimize();});
	$('.close').on('click', function(){minimize();});
	$('.maximize').on('click', function(){maximize();});
});

function minimize(){
    var container = document.getElementById('MainContainer');
    container.className = "";
	$('body').attr("class","minimized");
    $('#myModal').removeClass('is-visible')
}

function maximize(pk){
    $.ajax({
          type: 'GET',
          url: '/api/review/',
          data: {'review_id': pk},
          success: function(response){
            let reviewData = JSON.parse(response.data)[0].fields;
            var terminalTitle = document.getElementById('terminal-title');
            var terminalDescription = document.getElementById('terminal-description');
            terminalDescription.innerHTML = `«${reviewData.review_text}»`;
            terminalTitle.innerHTML = reviewData.title;
            var container = document.getElementById('MainContainer');
	        $('body').attr("class","maximized");
            container.className = "is-blurred";
            $('#myModal').addClass('is-visible');
          },
          error: function(){
            console.log(error);
          }
        });
}