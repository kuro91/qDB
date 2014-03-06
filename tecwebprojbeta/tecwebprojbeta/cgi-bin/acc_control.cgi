#!/usr/bin/perl -w

# file che controlla l'accesso utente
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


# leggo i dati dal POST e li inserisco nell'hash DATI
my %DATI = &leggi_post();

if(!%DATI){
	print redirect("../public_html/index.html");
}

# creo e inizializzo le variabili con i dati del POST
my $uemail = $DATI{'useremail'};
my $pass = $DATI{'password'};

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
my @useremail = $root->getElementsByTagName('useremail');

# controllo che l'username fornito non sia presente nell'array
# variabile di controllo
my $trovato = 0;

# controllo che l'useremail della form registrazione sia presente nel file
for my $u (@useremail){
	$u = $u->to_literal();
	if($uemail eq $u){ # l'useremail è gia presente
		$trovato = 1;
		last;
	}
}

if($trovato){
	# se è presente controllo la password
	# prelevo il valore della password dal file xml dal nodo con useremail = a quella passata dal form
	my $pwd = $doc->findvalue("/utenti/utente[useremail=\"$uemail\"]/password");
	
	
	# confronto le password
	if($pass == $pwd){
		# prelevo il valore della username e il tipo dal file xml dal nodo con useremail = a quella passata dal form
		my $nkn = $doc->findvalue("/utenti/utente[useremail=\"$uemail\"]/username");
		my $tpo = $doc->findvalue("/utenti/utente[useremail=\"$uemail\"]/tipo");
		
		# controllo se la sessione esiste gia
		my $session = CGI::Session->load() or die $!;

		if($session->is_expired || $session->is_empty){
			# sessione non esiste quindi la creo
			my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
			
			
			# aggiungo i parametri utente alla sessione
			$session->param("username", $nkn);
			$session->param("useremail", $uemail);
			$session->param("tipo", $tpo);
			
			# creo il cookie
			my $cookie1 = CGI::Cookie->new(-name => $session->name, -value => $session->id);
			my $cookie2 = CGI::Cookie->new(-name => "LDV", -value => $nkn);
			print header(-cookie => [$cookie1,$cookie2]);
			
			# creo una pagina accesso effettuato
			print "Content-type:text/html; charset=UTF-8\n\n";

			print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="it" xml:lang="it" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>conferma accesso - Libreria di Valyria</title>
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
			<span>Ti trovi in > Conferma accesso</span>
		</div>
		<div id="corpo">
			<div class="display" >
				<h2>Accesso Confermato</h2>
				<hr />
				<p>Congratulazioni <strong>$nkn</strong>, accesso effettuato con successo. Torna alla  <a href="../public_html/index.html" alt="">HOME</a> per continuare la navigazione.</p>
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
		else{
			# in questo caso la sessione esiste
			# controllo l'esistenza del cookie
			my %cookie = CGI::Cookie->fetch;
			my $cook = $cookie{'LDV'};
			
			# se il cookie non è presente lo creo
			if(!defined $cook){
				# ricreo il cookie se mancante
				my $cookie3 = CGI::Cookie->new(-name => "LDV", -value => $nkn);
				print header(-cookie => $cookie3);				
			}
			
			# creo una pagina accesso già effettuato
			print "Content-type:text/html; charset=UTF-8\n\n";

			print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="it" xml:lang="it" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>warning - Libreria di Valyria</title>
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
			<span>Ti trovi in >Warning</span>
		</div>
		<div id="corpo">
			<div class="display" >
				<h2>Warning</h2>
				<hr />
				<p> <strong>$nkn</strong>, lei ha già effettuato l'accesso. Si consiglia di mantenere attivi i cookies per il corretto funzionamento del sito. Torna alla  <a href="../public_html/index.html" alt="">HOME</a> per continuare la navigazione.</p>
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

}
