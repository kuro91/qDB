#!/usr/bin/perl -w

# file che controlla il logout utente
# carico le librerie
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;

# includo la mia libreria funzioni
require ('libreria_funzioni.pl');

# controllo se la sessione esiste gia
my $session = CGI::Session->load() or die $!;

my $name = $session->param('username');
my $sid = $session->name;

# cancellazione della sessione
$session->close();
$session->delete();
$session->flush();

# cancellazione del cookie LDV creato con la sessione
my $cgi = new CGI;
my $cookie1 = $cgi->cookie(-name => 'LDV', -value => '-1', -expires => '-1d');
my $cookie2 = $cgi->cookie(-name => $session->name, -value => '-1', -expires => '-1d');

print header(-cookie => [$cookie1, $cookie2]);

# creo una pagina logout effettuato
print "Content-type:text/html; charset=UTF-8\n\n";

print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="it" xml:lang="it" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>logout - Libreria di Valyria</title>
		<link rel="icon" type="image/png" href="../img/icona_titolo.png" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
		<meta name="keywords" content="Inserisci i contenuti" />
		<meta name="description" content="Inserisci le descrizioni" /> 
		<link href="../style/screen.css" rel="stylesheet" type="text/css" media="screen"/> 
		<link media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)" href="../style/small.css" rel="stylesheet" type="text/css">
	</head>
	<body>
	<div id="main">
		<div id="header">
			<h1 id="logo" class="shiftsx">Libreria di Valyria</h1>
		</div>
		<div id="path">
			<span>Ti trovi in >Logout</span>
		</div>
		<div id="corpo">
			<div class="display" >
				<h2>Logout</h2>
				<hr />
				<p>Arrivederci <strong>$name</strong>, logout effettuato con successo. Torna alla  <a href="../public_html/index.html" alt="">HOME</a> .</p>
			</div>
		</div>
		<div id="footer">
			<p>Copyright 2013-2014</p>
		</div>
	</div>
	</body>
</html>
EOF
