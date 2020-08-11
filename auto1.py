print'''
    <!DOCTYPE HTML>
    <html>
    <head> 
    <title>USER POSTS</title>
	<title>Online Store Website</title>
	<!-- Font Awesome, Style -->
	<link rel="stylesheet" type="text/css" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css">
	<style>
	html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	outline: none;
	vertical-align: baseline;
	box-sizing: border-box;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
input{
	box-sizing: border-box;
	outline: none;
}
body {
	line-height: 1;
	font-family: open sans;
	font-size: 14px;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
img{
	max-width: 100%;
}

.container{
	width: 100%;
	margin: 0 auto;
}

/*Topbar Style*/
.topbar{
	display: inline-block;
	width: 100%;
	height: 30px;
	float: left;
	background-color: #ffa800;
	font-size: 12px;
	font-weight: 600;
	position: relative;
}
.topleft{
	float: left;
}
.topcenter{
	float: left;
	text-align: center;
	margin: 0 25px;
}
.topright{
	float: right;
}
.topbar ul{
	line-height: 30px;
}
.topbar ul li{
	list-style-type: none;
	display: inline-block;
	position: relative;
}
.topbar ul li a{
	text-decoration: none;
	display: inline-block;
	color: #fff;
	padding: 0 5px;
	width: 100%;
	text-align: center;
	-webkit-transition: 300ms;
}
.topbar ul li a:hover{
	color: #000;
}
/*Submenu Style*/
.topbar ul li ul{
	position: absolute;
	display: none;
	z-index: 999;
	background-color: #ffa800;
	border-bottom-left-radius: 4px;
	border-bottom-right-radius: 4px;
	border: 1px solid #eea312;
}
.topbar ul li ul li{
	width: 100%;
}
.topbar ul li ul li a{
	padding: 0;
}
.topbar ul li ul.myprofile-dropdown{
	min-width: 120px;
}


/*Header Style*/
.header{
	display: inline-block;
	width: 100%;
	float: left;
	padding: 15px 0;
	border-bottom: 1px solid #00000010;
}
.header .logo{
	float: left;
	width: 20%;
}
.header .searchbar{
	width: 45%;
	float: left;
}
.searchbar .searchField{
	width: 100%;
	height: 35px;
	padding: 15px;
	border-radius: 50px;
	border: 1px solid gainsboro;
}
.header .headerright{
	float: right;
}
.header .headerright ul li{
	display: inline-block;
	padding: 10px 0;
}
.header .headerright ul li a{
	text-decoration: none;
	margin-left: 10px;
	color: #333;
}
.header .headerright ul li .signBtn{
	padding: 8px 13px;
	border-radius: 50px;
	background-color: #ffa800;
	color: #fff;
	font-weight: 600;
}
.size img{
 display: inline-block;
 height: 10 px;
 width: 350px;
}
.space{
 padding-bottom: 16px;
 padding-top: 16px;
 }
 .space h1{
  font-size: 15px;
	padding: 8px 0;
	font-weight: 600;
	line-height: 22px;
	color: #737373;
 }
 .productContent{
	display: inline-block;
	width: 60%;
	float: left;
	padding: 15px 0;
	position: relative;
}
.productContent .productCategories{
	width: 20%;
	float: left;
	padding: 7px 15px;
	border-radius: 8px;
	border: 1px solid #dfdcdc;
}
.productContent .productCategories ul li{
	display: inline-block;
	width: 90%;
	float: left;
	margin: 5px 0 10px;
}
.productContent .productCategories ul li a i.fa-caret-right{
	margin-left: 5px;
	color: #ffb524;
	vertical-align: middle;
	margin-top: -1px;
}
.productContent .productCategories ul li a{
	display: inline-block;
	padding: 5px 0;
	text-decoration: none;
	color: #333;
	font-weight: 600;
}
.megamenu{
	position: absolute;
	width: 70.2%;
	background-color: #fff;
	border: 1px solid gainsboro;
	left: 24.8%;
	top: 2.5%;
	min-height: 372px;
	border-radius: 8px;
	z-index: 9999;
	display: none;	
}
.productContent .productCategories ul li ul{
	max-width: 22%;
	float: left;
	padding: 15px;
}
.productContent .productCategories ul li ul h3{
	font-size: 12px;
	text-transform: uppercase;
	font-weight: 700;
	color: #333;
	margin-bottom: 10px;
}
.productContent .productCategories ul li ul li{
	margin: 0;
	display: inline-block;
	float: left;
}
.productContent .productCategories ul li ul li a{
	color: #333;
	font-size: 14px;
	font-weight: 500;
}
.productContent .productCategories ul li ul li a:hover{
	color: #ffdd05;
}

body{
    margin:0;
    padding:0;
    background:white;
}
.container1{
    width:1400px;
    margin:2% auto;


}
.product{
    background:white;
    width:25%;
    height:600px;
    box-shadow:0 8px 18px rgba(0,0,0,.25);
    border-radius:5px;
    position:relative;
    overflow:hidden;
    float:left;
    display:block;
    padding:10px;
    text-align:center;
    margin:0 22px;

}
.product .img-box{}
.product .img-box img{
    width:100%;
    height:250px;
    margin:auto;
    display:block;

}
.product .details{
    position:absolute;
    width:100%;
    bottom:0;
    background:#60858b;
    padding:20px;
    box-sizing:border-box;
    transition:.35s;
    box-shadow:0 6px 16px rgba(0,0,0,.35);
}
.product:hover .details{
    bottom:150px;
}
.product .details p{
    color:#252525;
    font-size:22px;
}




	</style>
	<link rel="stylesheet" type="text/css" href="css/owl.carousel.min.css">
    </head>
    <body>
	<!-- Topbar Start -->
	<div class="topbar">
		<div class="container">

			<!-- Top Left -->


			<!-- Top Center -->
			<div class="topcenter">
				<ul>

					<li><a href="http://localhost:90/project/laluteam.py">Contact Us</a></li>
				</ul>
			</div>

			<!-- Top Right -->

		</div>
	</div>
	<!-- Topbar End -->


	<!-- Header Start -->
	<div class="header">
		<div class="container">
			<div class="logo">
				<h1><big><strong><em>ADS FACTORY</em></strong></big></h1>
			</div>

			<div class="headerright">
				<ul>

                    <li><a href="http://localhost:90/project/view_data1.html" class="signBtn">Home</a></li>

					<li><a href="http://localhost:90/project/index1.py" class="signBtn">Login/Register</a></li>

				</ul>
			</div>
		</div>
	</div>
	<!-- Header End -->

	 <div class="productContent">
		<div class="container">
			<div class="productCategories">
				<ul>
					<li><a href="http://localhost:90/project/electronics.py">Electronics <i class="fas fa-caret-right"></i></a>
					<div class="megamenu">


						</div>
					</li>

				</ul>
			</div>

			'''
import config, cgi, cgitb

frm = cgi.FieldStorage()
cursor = config.db.cursor()
id = frm.getvalue('User_id')
cursor.execute('SELECT u.*,p.* FROM userdata u INNER JOIN post_table p on u.User_id=p.User_id AND cat_id=1')
result = cursor.fetchall()
if result:

    for j in result:
        print'''<div class="container1">
           <div class="row">
               <div class="col-sm-6 col-md-3">
                   <div class="product">
                       <div class="img-box">
                             <img src="{}">
                        </div>
                        <div class="details">
                                     <p>Seller Name:{} {}<br>
                                        Address:{}<br>
                                        Mobile_no:{}<br>
                                        City:{}<br>
                                        Pin:{}<br>
                                        Product name:{}<br>            
                                        Product key:{}<br>
                                        Product price:{}<br>
                                        Product image:{}<br>
                                        Product brand:{}<br>
                                        </p>
                       </div>                 
                   </div>
             </div>
         </div>
     </div>    

             '''.format(j[13], j[1], j[2], j[3], j[4], j[5], j[6], j[10], j[11], j[12], j[14], j[15])

print '</body>'
print '</html>'