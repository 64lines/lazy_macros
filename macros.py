#!/usr/bin/python
macro_list = {
#---------------------------------
"flex_void_public_function": 
"""
public function {0}(var number:int, var text:String):void
{
}
""",
#---------------------------------
"flex_void_private_function":
"""
private function {0}(var number:int, var text:String):void
{
}
""",
#---------------------------------
"java_void_public_function":
"""
public void {0}(int number, String text)
{
}
""",
#---------------------------------
"java_void_private_function":
"""
private void {0}(int number, String text)
{
}
""",
#---------------------------------
"html_bootstrap_jquery":
"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>{0}</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>{0}</h1>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
""",
#---------------------------------
"bash_user_interface_menu":
"""
#!/bin/bash

# {0}
OPTIONS="Hello Quit"
select opt in $OPTIONS; do
   if [ "$opt" = "Quit" ]; then
	echo done
	exit
   elif [ "$opt" = "Hello" ]; then
	echo Hello World
   else
	clear
	echo bad option
   fi
done
""",
}