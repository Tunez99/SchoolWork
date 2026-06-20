
<?php

  class Admin
  {
    private static $PROTECTED_VALUES = array();
    private static $initialized      = false;

    public static function authenticate ()
    {
      if ( !Admin::isLoggedIn() )
      {
        $_SESSION['redirect'] = $_SERVER['REQUEST_URI'];
        header( 'Location: /[redacted].php' );
        exit;
      }
    }
    public static function initialize ()
    {
      if ( Admin::$initialized )
      {
        return;
      }

      Admin::$PROTECTED_VALUES['admin-cookie']   = '[REDACTEDVALUE]';
      Admin::$PROTECTED_VALUES['admin-password'] = '[REDACTEDVALUE]';
      Admin::$PROTECTED_VALUES['admin-username'] = '[REDACTEDVALUE]';
      Admin::$PROTECTED_VALUES['dev-root']       = '[REDACTEDVALUE]';

      session_start();
      Admin::$initialized = true;
    }

    public static function isDevServer ( $dev_root = null )
    {
      if ( is_null( $dev_root ) )
      {
        $dev_root = Admin::$PROTECTED_VALUES['dev-root'];
      }

      return strpos( __FILE__, $dev_root ) !== false;
    }

    public static function isLoggedIn ()
    {
      return isset( $_SESSION[Admin::$PROTECTED_VALUES['admin-cookie']] );
    }

    public static function setAdminStatus ( $status )
    {
      session_destroy();
      session_start();

      if ( $status )
      {
        $_SESSION[Admin::$PROTECTED_VALUES['admin-cookie']] = time();
      }
    }

    public static function verifyLogin ( $username, $password )
    {
      return $username == Admin::$PROTECTED_VALUES['admin-username'] && $password == Admin::$PROTECTED_VALUES['admin-password'];
    }
  }

  Admin::initialize();

?>