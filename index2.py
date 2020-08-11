import cgi,cgitb
frm=cgi.FieldStorage()
msg=frm.getvalue('msg')
print''' Content-type:text/html\r\n\r\n
<!-- 
Credit : LearnDesign(Youtube Channel)
Channel Link : https://goo.gl/5pskoC
Email : help.learndesign@gmail.com
 -->

<!DOCTYPE html>
<html>
<head>
	<title>Online Store Website</title>
	<!-- Font Awesome, Style -->
	<link rel="stylesheet" type="text/css" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css">
	<link rel="stylesheet" type="text/css" href="css/style.css">
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
					<li><a href="#">Home</a></li>
					<li><a href="#">Company Profile</a></li>
					<li><a href="#">Payment Accept</a></li>
					<li><a href="#">Delivery</a></li>
					<li><a href="#">Contact Us</a></li>
				</ul>
			</div>

			<!-- Top Right -->
			<div class="topright">
				<ul>
					<li><a href="#"><i class="fas fa-phone"></i> +000(546)454545</a></li>
					<li><a href="#"><i class="fas fa-user"></i> My Profile <i class="fas fa-caret-down"></i></a>
						<ul class="myprofile-dropdown">
							<li><a href="#">My Order</a></li>
							<li><a href="#">My Wishlist</a></li>
							<li><a href="#">Pending Request</a></li>
							<li><a href="#">Delivered Order</a></li>
						</ul>
					</li>
				</ul>
			</div>
		</div>
	</div>
	<!-- Topbar End -->


	<!-- Header Start -->
	<div class="header">
		<div class="container">
			<div class="logo">
				<img src="images/logo.png">
			</div>
			<div class="searchbar">
				<form>
					<input type="search" class="searchField" placeholder="Search for products & brands">
				</form>
			</div>
			<div class="headerright">
				<ul>
					<li><a href="#"><i class="fas fa-heart"></i> Wishlist</a></li>
					<li><a href="#"><i class="fas fa-shopping-cart"></i> Cart</a></li>
					<li><a href="#" class="signBtn">Login & Register</a></li>
				</ul>
			</div>
		</div>
	</div>
	<!-- Header End -->


	<!-- Product Content Start -->
	<div class="productContent">
		<div class="container">
			<div class="productCategories">
				<ul>
					<li><a href="#">Electronics <i class="fas fa-caret-right"></i></a>
						<div class="megamenu">
							<ul>
								<h3>Mobiles <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Samsung</a></li>
								<li><a href="#">Realme</a></li>
								<li><a href="#">Mi</a></li>
								<li><a href="#">Nokia</a></li>
								<li><a href="#">LG</a></li>
								<li><a href="#">Intex</a></li>
								<li><a href="#">Apple</a></li>
								<li><a href="#">Vivo</a></li>
								<li><a href="#">Asus</a></li>
								<li><a href="#">Gionee</a></li>
								<li><a href="#">Pixel</a></li>
							</ul>
							<ul>
								<h3>Mobile Accessories <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Mobile Charger</a></li>
								<li><a href="#">Mobile Cover</a></li>
								<li><a href="#">Power Bank</a></li>
								<li><a href="#">Memory Card</a></li>
								<li><a href="#">Data Cable</a></li>
								<li><a href="#">Screenguard</a></li>
								<li><a href="#">Headphones</a></li>
							</ul>
							<ul>
								<h3>Computer Accessories <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">External Hard Disk</a></li>
								<li><a href="#">Pendrive</a></li>
								<li><a href="#">Laptop Skins</a></li>
								<li><a href="#">Laptop Bags</a></li>
								<li><a href="#">Mouse</a></li>
								<li><a href="#">Keyboard</a></li>
							</ul>
						</div>
					</li>
					<li><a href="#">TV & Multimedia <i class="fas fa-caret-right"></i></a>
						<div class="megamenu">
							<ul>
								<h3>Tvs Brand <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Samsung</a></li>
								<li><a href="#">LG</a></li>
								<li><a href="#">Sony</a></li>
								<li><a href="#">Micromax</a></li>
								<li><a href="#">Mi</a></li>
								<li><a href="#">Thomson</a></li>
							</ul>
							<ul>
								<h3>Tvs Brand <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Samsung</a></li>
								<li><a href="#">LG</a></li>
								<li><a href="#">Sony</a></li>
								<li><a href="#">Micromax</a></li>
								<li><a href="#">Mi</a></li>
								<li><a href="#">Thomson</a></li>
							</ul>
							<ul>
								<h3>Tvs Brand <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Samsung</a></li>
								<li><a href="#">LG</a></li>
								<li><a href="#">Sony</a></li>
								<li><a href="#">Micromax</a></li>
								<li><a href="#">Mi</a></li>
								<li><a href="#">Thomson</a></li>
							</ul>
							<ul>
								<h3>Tvs Brand <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Samsung</a></li>
								<li><a href="#">LG</a></li>
								<li><a href="#">Sony</a></li>
								<li><a href="#">Micromax</a></li>
								<li><a href="#">Mi</a></li>
								<li><a href="#">Thomson</a></li>
							</ul>
						</div>
					</li>
					<li><a href="#">Home & Furniture <i class="fas fa-caret-right"></i></a>
						<div class="megamenu">
							<ul>
								<h3>Washing Machine <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
							<ul>
								<h3>Washing Machine <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
							<ul>
								<h3>Washing Machine <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
							<ul>
								<h3>Washing Machine <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
						</div>
					</li>
					<li><a href="#">Automobiles<i class="fas fa-caret-right"></i></a>
						<div class="megamenu">
							<ul>
								<h3>Sports & Books <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
							<ul>
								<h3>Sports & Books <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
							<ul>
								<h3>Sports & Books <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
							<ul>
								<h3>Sports & Books <i class="fas fa-caret-right"></i></h3>
								<li><a href="#">Fully Automatic Front</a></li>
								<li><a href="#">Semi Automatic Top</a></li>
								<li><a href="#">Fully Automatic Top</a></li>
							</ul>
						</div>
					</li>


					<

				</ul>
			</div>


			<!-- Slider Start -->
			<div class="productSlider">
				<div id="sliderShuffle" class="sliderInner">
					<img src="images/1.jpg" />
					<img src="images/2.jpg" />
				</div>
				<div class="cycle-control">
					<span id="next"><i class="fas fa-angle-right"></i></span>
					<span id="prev"><i class="fas fa-angle-left"></i></span>
				</div>
			</div>
			<!-- Slider End -->

			<div class="offer-card">
				<img src="images/img1.jpg">
			</div>
			<div class="offer-card">
				<img src="images/img2.jpg">
			</div>
			<div class="offer-card">
				<img src="images/img3.jpg">
			</div>
		</div>
	</div>
	<!-- Product Content End -->


	<!-- Banner Start -->
	<div class="banner">
		<div class="container">
			<img src="images/banner.jpg" alt="Banner">
		</div>
	</div>
	<!-- Banner End -->


	<!-- Product Area Start -->
	<div class="product-area">
		<div class="container">
			<h3>Top Selling Products</h3>

			<div class="col-3">
				<a href="#">
					<img src="images/product-img1.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 999</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

			<div class="col-3">
				<a href="#">
					<img src="images/product-img2.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 255</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

			<div class="col-3">
				<a href="#">
					<img src="images/product-img3.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 444</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

			<div class="col-3">
				<a href="#">
					<img src="images/product-img4.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 598</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>


			<div class="col-3">
				<a href="#">
					<img src="images/product-img4.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 999</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

			<div class="col-3">
				<a href="#">
					<img src="images/product-img3.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 255</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

			<div class="col-3">
				<a href="#">
					<img src="images/product-img1.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 444</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

			<div class="col-3">
				<a href="#">
					<img src="images/product-img2.jpg" alt="">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 598</button>
					</div>
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

			<h3>New 2019 Fresh Stock</h3>
			<div class="col-3">
				<a href="#">
					<img src="images/product-img5.jpg">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 49</button>
					</div>	
					<button class="productViewBtn">View Product</button>
				</a>
			</div>
			<div class="col-3">
				<a href="#">
					<img src="images/product-img6.jpg">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 49</button>
					</div>	
					<button class="productViewBtn">View Product</button>
				</a>
			</div>
			<div class="col-3">
				<a href="#">
					<img src="images/product-img7.jpg">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 49</button>
					</div>	
					<button class="productViewBtn">View Product</button>
				</a>
			</div>
			<div class="col-3">
				<a href="#">
					<img src="images/product-img8.jpg">
					<div class="caption">
						<big>Code : GA00006488</big>
						<h4>Apple Macbook Pro MQ032 14.5' Inter
						Core i7 5550U 8GB DDR3</h4>
						<button class="price"><i class="fas fa-dollar-sign"></i> 49</button>
					</div>	
					<button class="productViewBtn">View Product</button>
				</a>
			</div>

		</div>
	</div>
	<!-- Product Area End -->

	<!-- Popular Store Start -->
	<div class="popularStores">
		<div class="container">
			<h3>Popular Stores</h3>			
			<div class="popularStoresInner">
				<a href="#">Dolorsite</a>
				<a href="#">Nostrum</a>
				<a href="#">Dignissimos</a>
				<a href="#">Temporibus</a>
				<a href="#">Distinction</a>
				<a href="#">Voluptam</a>
				<a href="#">Similique</a>
				<a href="#">Placeat</a>
				<a href="#">Dismiss</a>
			</div>
		</div>
	</div>
	<!-- Popular Store End -->


	<!-- Greatest Offer News Start -->
	<div class="news">
		<div class="container">
			<h3>Greatest Offer News</h3>
			<div class="owl-carousel">
				<div class="item"><img src="images/product-img9.jpg"></div>
				<div class="item"><img src="images/product-img10.jpg"></div>
				<div class="item"><img src="images/product-img11.jpg"></div>
				<div class="item"><img src="images/product-img12.jpg"></div>
				<div class="item"><img src="images/product-img10.jpg"></div>
			</div>
		</div>
	</div>
	<!-- Greatest Offer News End -->


	<!-- Support Section start-->
	<div class="support">
		<div class="container">
			<a href="#">
				<img src="images/icon1.png">
				<h5>Fast Delivery</h5>
			</a>
			<a href="#">
				<img src="images/icon2.png">
				<h5>Support 24 Hours</h5>
			</a>
			<a href="#">
				<img src="images/icon3.png">
				<h5>Easy Payment Method</h5>
			</a>
			<a href="#">
				<img src="images/icon4.png">
				<h5>Sell on e-store</h5>
			</a>
		</div>
	</div>
	<!-- Support Section end-->


	<!-- Other Information start -->
	<div class="otherInfo">
		<div class="container">
			<h3 class="otherInfoHandle">Consectetur adipisicing elit exercitationem</h3>
			<div class="otherInfoBody">
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui exercitationem, iste necessitatibus ex ea quaerat itaque numquam neque ad velit, aspernatur sunt culpa placeat iusto dolore molestias, porro ab perspiciatis.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto voluptatibus perspiciatis, dolor inventore dicta ut pariatur cupiditate blanditiis deleniti necessitatibus suscipit magnam, reiciendis tenetur ratione, doloribus vero hic minima asperiores.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum repellat pariatur totam voluptas quos asperiores cupiditate, nesciunt quis unde doloremque nostrum beatae ex, ut. Adipisci cum reprehenderit asperiores perferendis amet.</p>
			</div>
		</div>
	</div>
	<!-- Other Information end -->


	<!-- Footer Start -->
	<div class="footer">
		<div class="container">
			<div class="col-3">
				<p><big>Address UK:</big><br>Adipisci cum reprehenderit asperiores perferendis amet.</p>
				<p><big>Address US:</big><br>Ipsum repellat pariatur totam voluptas asperiores</p>
				<p><big>Address UAE:</big><br>Reprehenderit asperiores perferendis asperiores.</p>
			</div>
			<div class="col-3">
				<ul>
					<li><a href="#">Contact Anywhere</a></li>
					<li><a href="#">Easy payment Method</a></li>
					<li><a href="#">Fast Shipping</a></li>
					<li><a href="#">Our New Brand</a></li>
					<li><a href="#">Catalog</a></li>
				</ul>
			</div>
			<div class="col-3">
				<ul>
					<li><a href="#">About us</a></li>
					<li><a href="#">Jobs</a></li>
					<li><a href="#">Corpoprative Clients</a></li>
					<li><a href="#">Our Partner</a></li>
					<li><a href="#">Terms of use</a></li>
					<li><a href="#">Advertise with us</a></li>
					<li><a href="#">Compare bank</a></li>
				</ul>
			</div>
			<div class="col-3">
				<ul>
					<li><a href="#">Warranty</a></li>
					<li><a href="#">Check in</a></li>
					<li><a href="#">How to place order</a></li>
					<li><a href="#">Exchange and return</a></li>
					<li><a href="#">Installation</a></li>
					<li><a href="#">Quality of services</a></li>
				</ul>
			</div>
		</div>
	</div>
	<!-- Footer End -->


	<div class="copyright">
		<div class="container">
			<h5>&copy; 2019 eshopstore.com | Creator by johnsom</h5>
		</div>
	</div>


	<!-- Login Signup Form Start -->
	<div class="loginBox">
		<div class="closeBtn"><i class="fas fa-times"></i></div>
		<div class="loginForm">
			<h3>Login Form</h3>
			<form name="frm" method="post" action="userlogin.py">>
				<input class="textField" type="text" placeholder=" Email">
				<input class="textField" type="password" placeholder="Password">
				<input class="submitBtn" type="submit" value="Login">
			</form>
		</div>'''
		print '''<div class="registerForm">
			<h3>Register Form</h3>
			<form name="frm" method="post" action="user.py">
				 <tr>
        			<td>&nbsp</td>
            		<td>New seller?</td>
            		<td><input type="submit" name="ok" value="click here"></td>

        </tr>
			</form>
		</div>
	</div>'''
	<!-- Login Signup Form End -->


	print '''<!-- Product View Box / Quick Product View Start -->
	<div class="productViewBox">
		<h3>Apple Macbook Pro MQ032 14.5' Inter Core i7 5550U 8GB DDR3</h3>
		<div class="productViewBox-closeBtn"><i class="fas fa-times"></i></div>
		<div class="productViewBoxImg">
			<img src="images/img1.jpg">
		</div>
		<div class="productViewBoxDetail">
			<h5><b>Price : </b> <i class="fas fa-dollar-sign"></i> 598</h5>
			<h5><b>Brand : </b> Apple</h5>
			<h5><b>Warranty : </b> 12 Months</h5>
			<h5><b>Delivery of the city : </b> Free</h5>
			<h5><b>Payment : </b> COD, Visa, Mastercard, Debit, Credit, Installation</h5>
			<h5><b>Availability : </b> in Stock</h5>
			<h5><b>Product Code : </b> GA000006488</h5>
			<a href="#" class="addtocart"><i class="fas fa-heart"></i> Add to Cart</a>
			<a href="#" class="writereview"><i class="fas fa-pen"></i> Write a review</a>
			<a href="#" class="buynow"><i class="fas fa-shopping-cart"></i> Buy Now</a>
		</div>
	</div>
	<!-- Product View Box / Quick Product View End -->



<!-- Jquery V.3.3.1 -->
<script src="js/jquery-3.3.1.min.js"></script>
<script src="js/jquery.cycle.js"></script>
<script src="js/owl.carousel.min.js"></script>
<script>
	$("#sliderShuffle").cycle({
		next: '#next',
		prev: '#prev'
	});

	$('.owl-carousel').owlCarousel({
		items:4,
		loop:true,
		margin:15,
		autoplay:true,
		autoplayTimeout:3000, //3 Second
		nav:true,
		responsiveClass:true,
		responsive:{
			0:{
				items:1,
				nav:true
			},
			600:{
				items:3,
				nav:true
			},
			1000:{
				items:4,
				nav:true
			}
		}

	});

	$(function(){
		$(".topbar ul li").click(function(){
			$(".topbar ul li").not(this).find("ul").slideUp();
			$(this).find("ul").slideToggle();
		});
		$(".topbar ul li ul li, productCategories ul li .megamenu").click(function(e){
			e.stopPropagation();	
		});
		$(".productCategories ul li").click(function(){
			$(".productCategories ul li").not(this).find(".megamenu").hide();
			$(this).find(".megamenu").toggle();
		});
		$(".otherInfoBody").hide();
		$(".otherInfoHandle").click(function(){
			$(".otherInfoBody").slideToggle();
		});
		$(".signBtn").click(function(){
			$("body").css("overflow", "hidden");
			$(".loginBox").slideDown();
		});
		$(".closeBtn").click(function(){
			$("body").css("overflow", "visible");
			$(".loginBox").slideUp();
		});
		$(".productViewBtn").click(function(e){
			e.preventDefault();
			$("body").css("overflow", "hidden");
			$(".productViewBox").slideDown();
		});
		$(".productViewBox-closeBtn").click(function(){
			$("body").css("overflow", "visible");
			$(".productViewBox").slideUp();
		});
	});
</script>
</body>
</html>
'''