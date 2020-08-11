import cgi,cgitb
frm=cgi.FieldStorage()
msg=frm.getvalue('msg')
print''' Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html>

	<style type="text/css">

		@keyframes a_mail{

			0%{transform: translateX(-100px); opacity: 0}
 			100%{transform: translateX(0px); opacity: 1}
		}

		@keyframes a_pass{

			0%{transform: translateX(100px); opacity: 0}
			100%{transform: translateX(0px); opacity: 1}
		}

		@keyframes button{

			0%{transform: scale(0.2); opacity: 0}
			100%{transform: scale(1); opacity: 1}
		}

		@keyframes content{

			0%{transform: translateY(-200px); opacity: 0}
 			100%{transform: translateY(0px); opacity: 1}
		}

 		@font-face{

	 		font-family: unisans;
			src: url(UniSans.ttf);

		}

		body{

 			font-family: unisans, ariel, verdana, Geneva, Verdana, sans-serif;
			background-color: rgb(146, 212, 190);
			background: radial-gradient(rgb(206, 252, 250),rgb(86, 152, 140));
			color: rgb(69, 161, 130);
			height: 100%;
			background-image: url(bg.jpg);
			background-size: 100%;
		}

		#wrapper{

			max-width: 300px;
			min-height: 200px;
 			margin: auto;
			margin-top: 150px;
    	}

		#title_section{

 			background-color: rgb(69, 161, 130);
 			height: 30px;
 			color: white;
 			text-align: center;
 			font-size: 20px;
 			padding-top: 10px;
 			box-shadow: 0px 5px 6px #000;
		}

		#content_section{

 			background-color: #ffffff88;
 			height: 210px;
 			padding: 1em;
 			text-align: center;
 			border-bottom-right-radius: 80px;
 		}

		.textbox{

 			border: none;
			padding: 8px;
 			border-radius: 30px;
  			width: 300px;
  			height: 15px;
 			margin-left: -25px;
 			transition: 0.5s cubic-bezier(0.68, -2, 0.265, 1.55);
 			color: rgb(39, 131, 90);
 		}

 		.textbox:focus{

 			font-size: 16px;
 			height: 25px;
 			color: black;
 			box-shadow: 0px 5px 10px #666;
 		}

		#button{

			font-family: unisans, ariel, verdana, Geneva, Verdana, sans-serif;
  			border-radius: 30px;
 			background-color: rgb(69, 161, 130);
 			color: white;
 			width: 320px;
 			border: none;
 			height: 40px;
 			margin-left: -25px;
 			box-shadow: 0px 5px 10px #333;
 			font-size: 18px;
 			cursor: pointer;
		}

		#email_label{

			margin-top: -40px;
			position: relative;
			z-index: -1;
 			background-color: #000;
			text-align: left;
			padding: 10px;
			border-radius: 30px;
			transition: 0.5s cubic-bezier(0.68, -2, 0.265, 1.55);
			opacity: 0;
		}

		#email:focus ~ #email_label{

			margin-left: -120px;
			opacity: 1;
		}

		#Password_label{

			margin-top: -40px;
			position: relative;
			z-index: -1;
 			background-color: #000;
			text-align: left;
			padding: 10px;
			border-radius: 30px;
			transition: 0.5s cubic-bezier(0.68, -2, 0.265, 1.55);
			opacity: 0;
		}

		#Password:focus ~ #password_label{

			margin-left: -120px;
			opacity: 1;
		}

	</style>

	<head>
		<title>Login page</title>
	</head>

	<body>

		<div id="wrapper">

			<div id="title_section">
				ADMIN LOGIN
			</div>

			<div id="content_section"  style="animation: content 1s ease;">

				<br/>
				<form name="frm" method="post" action="a_logcode.py">

					<input id="a_mail" name="a_mail" class="textbox" type="mail" placeHolder="Enter Your E-mail" name="a_mail" style="animation: email 1.5s cubic-bezier(0.68, -2, 0.265, 1.55);" />
					<div id="email_label">Email-id</div>
					<br/>
					<input id="a_pass" name="a_pass" class="textbox" type="password" placeHolder="Enter your Password" name="a_pass" style="animation: password 1.5s cubic-bezier(0.68, -2, 0.265, 1.55);"/>
					<div id="Password_label">Password</div>
					<br/>
					<input id="button" type="submit" value="login" style="animation: button 1s cubic-bezier(0.68, -2, 0.265, 1.55);"/>



				</form>

			</div>
		</div>'''
if msg:
    print msg+"<br>"
print '''</body>
</html>
'''


