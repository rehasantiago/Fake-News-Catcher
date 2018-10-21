<!DOCTYPE html>
<html>
<head>
	<title>home</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  <link href='http://fonts.googleapis.com/css?family=Lobster+Two' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:500">
  <link rel="stylesheet" type="text/css" href="css/home.css">
  <script type="text/javascript" src="js/search.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script>
	$(document).ready(function() {
		$('.search').click(function() {
				$('.search').addClass('active');
				$('.line-1').css({
						'transform': 'rotate(45deg)',
						'left': '0px'
				});
				$('.line-2').css({
						'height':'40px',
						'opacity':'1'
				});
		});
		$('.line-1, .line-2').click(function() {
				$('.search').removeClass('active').val('');
				$('.line-1').css({
						'transform': 'rotate(-45deg)',
						'left': '45px'
				});
				$('.line-2').css({
						'height':'0px',
						'opacity':'0'
				});

		});
});
</script>

</head>
<body>

		<div id="particles-js" style="z-index: -1;" ></div>
		<script src="http://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script> <!-- stats.js lib --> <script src="http://threejs.org/examples/js/libs/stats.min.js"></script>

		<style type="text/css">
		
	/* ---- reset ---- */ 
	canvas{ 
		display: block;
	 	vertical-align: bottom; 
	 	}
	  /* ---- particles.js container ---- */ 
	#particles-js{ 
	  	position:absolute; 
	  	width: 100%; 
	  	height: 100%; 
	  	}
	  
	   /* ---- stats.js ---- */ 
	.count-particles{ background: #000022; position: absolute; top: 48px; left: 0; width: 80px; color: #13E8E9; font-size: .8em; text-align: left; text-indent: 4px; line-height: 14px; padding-bottom: 2px; font-family: Helvetica, Arial, sans-serif; font-weight: bold; } 

	.js-count-particles{ 
		font-size: 1.1em; 
	} 

	#stats, .count-particles{ 
		-webkit-user-select: none; 
		margin-top: 5px; 
		margin-left: 5px; 
	} 

	#stats{ 
		border-radius: 3px 3px 0 0; 
		overflow: hidden; 
	} 

	.count-particles{ 
		border-radius: 0 0 3px 3px; 
	}

		</style>

		<script type="text/javascript">
			particlesJS("particles-js", {"particles":{"number":{"value":265,"density":{"enable":true,"value_area":2004.2650760819035}},"color":{"value":"#000000"},"shape":{"type":"circle","stroke":{"width":0,"color":"#000000"},"polygon":{"nb_sides":5},"image":{"src":"img/github.svg","width":100,"height":100}},"opacity":{"value":1,"random":false,"anim":{"enable":false,"speed":9.176472499005207,"opacity_min":0.0974492654761615,"sync":false}},"size":{"value":3,"random":true,"anim":{"enable":false,"speed":40,"size_min":0.1,"sync":false}},"line_linked":{"enable":true,"distance":150,"color":"#02fc1e","opacity":0.9620472365193137,"width":2},"move":{"enable":true,"speed":6,"direction":"none","random":false,"straight":false,"out_mode":"out","bounce":false,"attract":{"enable":false,"rotateX":600,"rotateY":1200}}},"interactivity":{"detect_on":"canvas","events":{"onhover":{"enable":true,"mode":"repulse"},"resize":true},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1}},"bubble":{"distance":400,"size":40,"duration":2,"opacity":8,"speed":3},"repulse":{"distance":200,"duration":0.4},"push":{"particles_nb":4},"remove":{"particles_nb":2}}},"retina_detect":true});
		</script>

		
	<!--particle ends here-->

	<div class="container-fluid" style="z-index: +1; margin-top: 5%;" id="fluid_1">
		<h1>Fake News Catcher.com</h1><br>
			<main style="position: absolute; text-align: center;" id="search-box">
				<input type="text" class="search" id="search" style= "z-index: +1"/>
				<div class="line-1"></div>
				<div class="line-2"></div><br>
			</main><br><br><br><br><br>
			<a href="#" id="stylish-btn">Check</a>

		<style type="text/css">
			/*search-animation*/
	@import url('https://fonts.googleapis.com/css?family=Roboto:500');

		::selection {
	    background: #16a085;
	    color: black;
	}

	.line-1 {
	    width: 0.313em;
	    height: 2.500em;
	    background: black;
	    margin: auto;
	    position: relative;
	    left: 2.813em;
	    top: -1.250em;
	    transform: rotate(-45deg);
	    transition: .5s;
	    transition-timing-function: cubic-bezier(1,0,.3,1);
	    cursor: pointer;
	}

	.line-2 {
	    width: 0.313em;
	    background: black;
	    margin: auto;
	    transform: rotate(-45deg);
	    position: relative;
	    left: 0;
	    top: -2.500em;
	    opacity: 0;
	    transition: .5s ease-in-out;
	    transition-timing-function: cubic-bezier(1,0,.3,1);
	    cursor: pointer;
	}

	.search {
		font-weight: 600;
	    color: black;
	    font-family: 'Roboto', sans-serif;
	    font-size: 110%;
	    width: 5em;
	    height: 5em;
	    line-height: 6em;
	    border: 0.313em solid black;
	    border-radius: 6.250em;
	    cursor: default;
	    transition: .7s;
	    transition-timing-function:cubic-bezier(1,-0.5,0,1.5);
	    text-align: left;
	    box-sizing: border-box;
	    outline: none;
	    background-color: white;
	    padding-left: 4%;
	    padding-right: 4%;
	}


	.active {
		margin-top: 2%;
		margin-bottom: 2%;
	    width: 32em;
	    border: 0.313em solid black;
	    border-radius: 1.250em;
	}

	#search-box{
		position: absolute;
		left: 50%;
		top: 18%;
		transform: translate(-50%, -50%);
	}

	@media only screen and (min-width: 1024px){
		#search-box{
		position: absolute;
		left: 50%;
		top: 37%;
		transform: translate(-50%, -50%);
		}

		.search {
		font-weight: 600;
	    color: black;
	    font-family: 'Roboto', sans-serif;
	    font-size: 110%;
	    width: 5em;
	    height: 5em;
	    border: 0.313em solid black;
	    border-radius: 6.250em;
	    cursor: default;
	    transition: .7s;
	    transition-timing-function:cubic-bezier(1,-0.5,0,1.5);
	    text-align: left;
	    box-sizing: border-box;
	    outline: none;
	    background-color: white;
	    padding-left: 4%;
	    padding-right: 4%;
	}

		.active {
	    width: 32em;
	    height: 4em;
	    border: 0.313em solid black;
	    border-radius: 1.250em;
	    margin-top: 6%;
	}

	}
		</style>
	</div>
	<script>
		$('#stylish-btn').click(function(){
			var input = $('#search').val();
		$.post('link.php',{input:input},function(data,status){
			$('#output').html(data);
		});
	});
	</script>
	<div id='output' class="container" style="margin-top: 13%; font-family: 'Roboto'; font-size: 120%; ">
		
	</div>

</body>
</html>