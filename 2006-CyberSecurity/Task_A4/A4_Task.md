A4 Discover a vulnerable website.

in this module I aimed to find a vulnerable website and identify potential security weaknesses.

My initial approach was searching for data leaks through archived websites via the Internet Archive (Wayback Machine). 

I began with analysing a heavily archived site hosted on Newgrounds. The goal was to search for potential exposed end points and backend functionality.

During this process, I identified multiple code snippets with endpoints and features;

"/checkvalidation"
"/passport"
"/passport/signup"
"/passport/forgot-password"

Also finding client side parameters.
croptool.setUserParams({
    user_id: 7311090,
    user: "zenmonster06"
})

However, this ended in no clear vulnerability. 

Due to limited success and my findings from PHP links and end point requests. I decided to leverage google, to find exposed end points using php.

Using the following search prompt:

"inurl:page.php?id=" "copyright 200"

I found this website. 

https://www[redacted].com/source.view.php?page=./classes/Admin.php

This indicated that the site was loading files based on php requests, which is a common vulnerability. 

This website has been redacted for ethical reasons.

<?php
  require 'headers.php';
  require './classes/Navigation.php';
  require './classes/Page.php';
?>

Through accessing the Admin.php file, i was able to observe sensitive information directly in the code:

Admin::$PROTECTED_VALUES['admin-cookie']   = '[REDACTEDVALUE]';
Admin::$PROTECTED_VALUES['admin-password'] = '[REDACTEDVALUE]';
Admin::$PROTECTED_VALUES['admin-username'] = '[REDACTEDVALUE]';
Admin::$PROTECTED_VALUES['dev-root']       = '[REDACTEDVALUE]';


This clearly displays a serious vulnerability to PHP injection due to:

Exposed/hardcoded credentials, passwords, session information and interal application structure. 

If a threat decided to act apon these findings, they could potentially gain unauthorised admin access.

********** IMPORTANT INFORMATION
The vulnerable file was publicly accessible without authentication. Upon discovery, no attempt was made to use the credentials or interact further with the live system.

All analysis was limited to observation and documentation, in line with ethical cybersecurity practices.




