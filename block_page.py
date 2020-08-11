print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <title>admin page</title>

    <style>
        {
        margin: 0px;
        padding : 0px;
        box-sizing: border-box;
        }


        body{
       font-family : 'Open Sans';
        }

        a{
        text-decoration :none;
        }

     .header{
        overflow :hidden;
        background-color:#577c7d;
        padding: 20px 10px;
        }
        .header a {
            float: left;
            color: black;
            text-align: center;
            padding: 20px;
            text-decoration: none;
            font-size: 18px;
            line-height: 25px;
            border-radius: 8px;
        }
        .header a:hover {
            background-color: #ddd;
            color: black;
            }
            .header a.active {
                background-color: dodgerblue;
                color: white;
            }
        .header-right {
            float: right;
            }

            #container{
       width : 100%;
       margin: 0 auto;
}

            .content{
        width : auto;
        height: 495px;
        margin-left: 250px;
        background : #faea70;
        padding: 15px;
        }
    .w3-sidebar{
        width: 250px;
        height: 495px;
        float: left;
        background-color: #33a691;
        position : fixed;
        font-size : 20px;
        }



    #adminlogo{
    background : white;
    width: 90px;
    border-radius:100px;
    }
    </style>





</head>
<body>
<div class = "header">
    <center><img src = "01-1User-2-512.png" alt = "admin image" id = "adminlogo"><h2 style="color : white;">ADMIN PANEL</h2></center>

    <div class="header-right">
        <a class="active" href="#home"><b>HOME</b><i class="fa fa-home"></i></a>
        <a  href="#logout"><b>LOG OUT</b></a>

    </div>
</div>
<div id = "container">
    <div class="w3-sidebar  w3-bar-block  w3-card ">
        <a href="#" class="w3-bar-item w3-button">Home</a>
        <a href="#" class="w3-bar-item w3-button">Active Posts</a>
        <a href="#" class="w3-bar-item w3-button">Block Posts</a>

            <div class="w3-dropdown-hover">
                <button class="w3-button">Categories
                <i class="fa fa-caret-down"></i>
                </button>
            <div class="w3-dropdown-content w3-bar-block">
                <a href="#" class="w3-bar-item w3-button">Electronics</a>
                <a href="#" class="w3-bar-item w3-button">Automobile</a>
            </div>
            </div>
        <a href="#" class="w3-bar-item w3-button">Log Out</a>
    </div>
    <div class = "content">
        <center><h1><strong>ALL POSTS</strong></h1></center>
        <center><h2>UPDATE AND DELETE POSTS </h2></center>

'''
import config, cgi

frm = cgi.FieldStorage()
if frm.getvalue('msg'):
    print frm.getvalue('msg')

cursor = config.db.cursor()
cursor.execute('SELECT * FROM std')  # we need dynamic datas so we execute a loop in tbody
# when we take rec ..it takes the result in a list
result = cursor.fetchall()
if result:
    print '''<table cellpadding = "5" cellspacing = "0" border = "1"> 
    <thead>
        <tr>
            <th>NAME</th>
            <th>email</th>
            <th>password</th>
            <th>upgrade</th>
            <th>delete</th>
        </tr>
    </thead>
    <tbody>'''
    for rec in result:
        print '''<tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td><a href = "block.py?id={}"></a></td>
                <td><button>Block</button></td>
            </tr>'''.format(rec[1], rec[2], rec[3],rec[4],rec[5], rec[0])

    print '''</tbody>
    </table>'''
else:
    print"No More Products !!!!"
print '''    </div>
</div>
</body>
</html>'''