#!/usr/bin/perl -w

# file che controlla la registrazione utente
# carico le librerie
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use Crypt::SaltedHash; # libreria per la cryptazione password
use URI;

# includo la mia libreria funzioni
require ('libreria_funzioni.pl');

# leggo i dati dal POST e li inserisco nell'hash DATI
my %DATI = &leggi_post();

if(!%DATI){
	print redirect("../public_html/index.html");
}

# creo e inizializzo le variabili con i dati del POST
my $uname = $DATI{'username'};
my $uemail = $DATI{'useremail'};
my $pass = $DATI{'password'};
my $tipo = $DATI{'tipo'};

#===============================================================================
# Cerco nel file utenti.xml se l'utente è gia egistrato o ha inserito un username gia presente
my $file = "../data/utenti.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

# estrazione radice
my $root = $doc->getDocumentElement;

# array degli elementi username
my @username = $root->getElementsByTagName('username');

# controllo che l'username fornito non sia presente nell'array
# variabile di controllo
my $trovato = 0;

# controllo che l'useremail della form registrazione sia presente nel file
for my $u (@username){
	$u = $u->to_literal();
	if($uname eq $u){ # l'useremail è gia presente
		$trovato = 1;
		last;
	}
}

if($trovato){
	&username_esistente();
}
else{
	# array degli elementi username
	my @useremail = $root->getElementsByTagName('useremail');

	# controllo che l'username fornito non sia presente nell'array
	# variabile di controllo
	my $present = 0;

	# controllo che l'useremail della form registrazione sia presente nel file
	for my $u (@useremail){
		$u = $u->to_literal();
		if($uemail eq $u){ # l'useremail è gia presente
			$present = 1;
			last;
		}
	}
	if($present){
		&email_presente();
	}
	else{
		
		# Inserisco il nuovo utente nel file utenti.xml
		my $utente = XML::LibXML::Element->new('utente'); 

		my $nome = XML::LibXML::Element->new('username');
		$nome->appendText( $uname );
		$utente->appendChild($nome);

		
		my $email = XML::LibXML::Element->new('useremail');
		$email->appendText( $uemail );
		$utente->appendChild($email);

		my $password = XML::LibXML::Element->new('password');
		$password->appendText( $pass );
		$utente->appendChild($password);
		
		my $type = XML::LibXML::Element->new('tipo');
		$type->appendText( $tipo );
		$utente->appendChild($type);

		$root->appendChild($utente);
		
# scrittura su file
open(OUT,">$file") or die $!;
print OUT $doc->toString;
close(OUT);
		
# crea una pagina html che conferma la registrazione
print "Content-type:text/html; charset=utf-8\n\n";

print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="it" xml:lang="it" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>congratulazioni - Libreria di Valyria</title>
		<link rel="icon" type="image/png" href="../img/icona_titolo.png" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
		<meta name="keywords" content="Inserisci i contenuti" />
		<meta name="description" content="Inserisci le descrizioni" /> 
		<link href="../style/screen.css" rel="stylesheet" type="text/css" media="screen"/> 
		<link media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)" href="../style/small.css" rel="stylesheet" type="text/css">
		<script lenguage="text/javascript" src="../js/registration_control.js"></script>
	</head>
	<body>
	<div id="main">
		<div id="header">
			<h1 id="logo" class="shiftsx">Libreria di Valyria</h1>
		</div>
		<div id="path">
			<span>Ti trovi in > Congratulazioni</span>
		</div>
		<div id="corpo">
			<div class="display" >
				<h2>Congratulazioni</h2>
				<hr />
				<p>Lei ora è un utente registrato al sito, quindi la invitiamo a tornare alla <a href="../public_html/index.html" alt="pagina iniziale del sito">HOME</a> o effettuare l'<a href="../public_html/accesso.html" alt="pagina di accesso">ACCESSO</a> per continuare la sua navigazione GRAZIE!</p>
			</div>
		</div>
		<div id="footer">
			<p>Copyright 2013-2014</p>
		</div>
	</div>
	</body>
</html>
EOF

	}
}
exit;

