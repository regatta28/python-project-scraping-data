from bs4 import BeautifulSoup
import requests
from csv import writer

# response = requests.get("index.html")


# soup = BeautifulSoup(response.text, "html.parser")
html_doc= """



<!DOCTYPE html>

<html lang="en">

<head>

	<meta charset="utf-8">

	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>WebDevSav-Software developer</title>

	<link rel="stylesheet" href="bootstrap-4.3.1-dist/bootstrap-4.3.1-dist/css/bootstrap.min.css">

	<link rel="stylesheet" href="style.css">


	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">

</head>



<body data-spy="scroll" data-target="#navbarResponsive">



<!--- Start Home Section-->



<div id="home">

<!--- Navigation --->

<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">

	<a class="navbar-brand" href="#">WebDevSav</a>

	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"><span class="navbar-toggler-icon"></span></button>

	<div class="collapse navbar-collapse" id="navbarResponsive">

		<ul class="navbar-nav ml-auto">

			<li class="nav-item">

				<a class="nav-link" href="#home">Home</a>

			</li>

			<li class="nav-item">

				<a class="nav-link" href="#course">Course</a>

			</li>

			<li class="nav-item">

				<a class="nav-link" href="#features">Features</a>

			</li>

			<li class="nav-item">

				<a class="nav-link" href="#resources">Resources</a>

			</li>

			<li class="nav-item">

				<a class="nav-link" href="#client">Clients</a>

			</li>

			<li class="nav-item">

				<a class="nav-link" href="#contact">Contact</a>

	</div>

</nav>



<!---- End Navigation ---->



<!--- Start Landing Page Section ---->



<div class="landing">

	<div class="home-wrap">

		<div class="home-inner">



		</div>

	</div>

</div>



<div class="caption text-center">

	<h1>Welcome to WebDevSav</h1>

	<h3>Designing and maintaining Websites</h3>

	<a class="btn btn-outline-light btn-lg" href="#course">Get Started</a>

</div>





<!--- End Landing Page Section ---->



</div>



<!---- End Home Section-->



<!--- Start Course Section-->



<div id="course" class="offset">



    <div class="col-12 narrow text-center">

		<h1>WebDevSav by R.S</h1>

		<p class="lead">Designing sleek & user friendly responsive websites. Backend development for database storage and access.</p>

		<a class="btn btn-secondary btn-md" href="https://github.com/regatta28">Visit Github Portfolio</a>

	</div>



</div>



<!---- End Course Section-->



<!--- Start features Section-->



<div id="features" class="offset">



	<!---- Start Jumbotron ---->



	<div class="jumbotron">

		<div class="narrow">

			<div class="col-12 text-center">

				<h3>Features</h3>

				<div class="heading-underline"></div>

			</div>

			<div class="row text-center">

				<div class="col-md-4">

					<div class="feature">

						<i class="fas fa-play-circle fa-4x" data-fa-transform="shrink-3 up-5"></i>

						<h3 class="heading">Custom Bootstrap</h3>

						<p class="paragraph">Smooth, user friendly, responsive UX design</p>

					</div>

				</div>

			<div class="col-md-4">

				<div class="feature">

					<i class="fas fa-sliders-h fa-4x" data-fa-transform="shrink-4.5 up-4.5"></i>

					<h3 class="heading">JavaScript</h3>

					<p class="paragraph">Animated, interactive websites for user stimulation</p>

				</div>

			</div>

			<div class="col-md-4">

				<div class="feature">

					<i class="fab fa-wpforms fa-4x" data-fa-transform="shrink-3 up-5"></i>

					<h3  class="heading">Backend Development</h3>

					<p class="paragraph">Cloud computing services, using data to grow your business</p>

				</div>

			</div>



			</div>

			<!--- End Row -->

		</div>

	<!----  End Narrow  -->



	</div>

	<!---- End Jumbotron ---->



</div>



<!---- End Features Section-->



<!--- Start Resources Section-->



<div id="resources" class="offset">



	<div class="fixed-background">



		<div class="row dark">



			<div class="col-12 text-center">

				<h3 class="heading">Built with care</h3>

				<div class="heading-underline"></div>

			</div>



			<div class="col-md-4 text-center">

				<h3>HtML5</h3>

				<div class="feature">

					<i class="fas fa-code fa-3x"></i>

				</div>

				<p class="lead">Built with the latest, HTML5</p>

			</div>

			<div class="col-md-4 text-center">

				<h3>CSS 3</h3>

				<div class="feature">

					<i class="fab fa-css3 fa-3x"></i>

				</div>

				<p class="lead">Built with the latest, CSS 3</p>

			</div>

			<div class="col-md-4 text-center">

				<h3>Bootstrap 4</h3>

				<div class="feature">

					<i class="fas fa-bold fa-3x"></i>

				</div>

				<p class="lead">Built with the latest, Bootstrap 4</p>

			</div>

		</div>

	<!----  End Row Dark ---->



		<div class="fixed-wrap">

			<div class="fixed">



			</div>

		</div>



	</div>

<!---- End Fixed Background  -->



</div>



<!---- End Resources Section-->



<!--- Start Clients Section-->



<div id="client" class="offset">



<!--- Start Jumbotron ---->



<div class="jumbotron">



	<div class="col-12 text-center">

		<h3 class="heading">Clients</h3>

		<div class="heading-underline"></div>

	</div>

	<div class="row">

		<div class="col-md-6 clients">

			<div class="row">

				<div class="col-md-4">

					<img src="img/client1.png">

				</div>

				<div class="comments col-md-8">

					<blockquote>

						<i class="fas fa-quote-left"></i>

						WebDevSav are a very supportive company to work with. I can pick up the phone at any time to talk and the interactions are always simple and productive. 

					</blockquote>

					<hr class="clients-hr"><cite>&#8212; Eric, Small Business Owner</cite>

				</div>

			</div>

		</div>

		<div class="col-md-6 clients">

			<div class="row">

				<div class="col-md-4">

					<img src="img/client2.png">

				</div>

				<div class="comments col-md-8">

					<blockquote>

						<i class="fas fa-quote-left"></i>

						WebDevSav have been a massively important aspect of my business as managing the day to day and website all at once can be challenging at times. I could always rely on WebDevSav to be a rock of support.

					</blockquote>

					<hr class="clients-hr"><cite>&#8212; Rachel, Professional Photographer</cite>

				</div>

			</div>

		</div>



	</div>

<!----  End Row ---->

</div>

<!---  End Jumbotron ----->

<div class="col-12 narrow text-center">

	<p class="lead">Want to learn more about WebDevSav?</p>

	<a class="btn btn-secondary btn-md" href="https://github.com/regatta28">Visit Github Portfolio</a>

</div>

</div>



<!---- End Clients Section-->



<!--- Start Contact Section-->



<div id="contact" class="offset">



<footer>

	<div class="row justify-content-center">

		<div class="col-md-5 text-center">

				<a class="navbar-brand" href="#">WebDevSav</a>

				<p>At our core is a collection of design and development solutions that represent everything your business needs to compete in the modern marketplace.</p>

				<strong>Contact Info</strong>

				<p>(888) 888-8888<br>email@email.com</p>

				<a href="" target="_blank"><i class="fab fa-facebook-square"></i></a>

				<a href="" target="_blank"><i class="fab fa-twitter-square"></i></a>

				<a href="" target="_blank"><i class="fab fa-instagram"></i></a>

		</div>

		<hr class="socket">

		&copy;WebDevSav

	</div>



</footer>



</div>



<!---- End contact Section-->



<!--- Script Source Files -->

<script src="js/jquery-3.3.1.min.js"></script>

<script src="bootstrap-4.3.1-dist/bootstrap-4.3.1-dist/js/bootstrap.min.js"></script>

<script src="https://use.fontawesome.com/releases/v5.5.0/js/all.js"></script>

<!--- End of Script Source Files -->



</body>

</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")

posts = soup.find_all(class_='feature')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ('Heading', 'Paragraph')
    csv_writer.writerow(headers)

    for post in posts:
        heading = post.find(class_="heading")
        paragraph = post.find(class_="paragraph")

        csv_writer.writerow([heading, paragraph])