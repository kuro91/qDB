#!/usr/bin/perl -w

# Questo file libreria contiene alcune funzioni che vengono utilizzate nel sito
#====================================================================================
#
# Path che identifica il namespace dei file xml
# Variabile contenente la path del sito
sub nspath {
	my $path = "http://www.localhost";
	return $path;
}
#====================================================================================
#
# Funzione &username_esistente()
#
# ricrea la pagina html di registrazione
#
#
sub username_esistente()
{
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
		<script lenguage="text/javascript" src="../js/registration_control.js"></script>
	</head>
	<body onload="controlli()"  >
	<div id="main">
		<div id="header">
			<h1 id="logo" class="shiftsx">Libreria di Valyria</h1>
		</div>
		<div id="path">
			<span>Ti trovi in > Warning</span>
		</div>
		<div id="corpo">
			<div class="display" >
				<h2>Attenzione</h2>
				<hr />
				<p>L'username inserito è gia in uso, torni alla pagina <a href="../public_html/registrazione.html" alt="pagina di registrazione">REGISTRAZIONE</a> per inserirne uno nuovo!</p>
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

#====================================================================================
#
# Funzione &gia_loggato()
#
# crea una pagina html che avverte l'utente che è gia loggato
#
#
sub email_presente()
{

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
		<script lenguage="text/javascript" src="../js/registration_control.js"></script>
	</head>
	<body onload="controlli()"  >
	<div id="main">
		<div id="header">
			<h1 id="logo" class="shiftsx">Libreria di Valyria</h1>
		</div>
		<div id="path">
			<span>Ti trovi in > Warning</span>
		</div>
		<div id="corpo">
			<div class="display" >
				<h2>Attenzione</h2>
				<hr />
				<p>Lei ha gia effettuato la registrazione al sito, quindi la invitiamo a tornare alla <a href="../public_html/index.html" alt="pagina iniziale del sito">HOME</a> o effettuare l'<a href="../public_html/accesso.html" alt="pagina di accesso">ACCESSO</a> per continuare la sua navigazione GRAZIE!</p>
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
#====================================================================================
# Funzione &leggiPost()
#
# Legge lo standard input (in questo caso metodo POST di una for)
# e restituisce un hash contenente i dati.
#
sub leggi_post()
{	
	my($buffer, $nome, $valore, @coppia, %DATI);
	
	read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    #
    # Suddivide la richiesta in un array di coppie «nome=valore».
    #
    @coppia = split ('&', $buffer);
    #
    # Elabora ogni coppia contenuta nell'array.
    #
    foreach my $elemento (@coppia)
      {
        #
        # Scompone la coppia.
        #
        ($nome, $valore) = split ('=', $elemento);
        #
        # Trasforma «+» in spazio.
        #
        $valore =~ tr/+/ /;
        #
        # Trasforma «%hh» nel carattere corrispondente.
        #
        $nome   =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        $valore =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        #
        # Aggiunge la coppia decodificata in un hash.
        #
        $DATI{$nome} = $valore;
      }
      # Restituisce l'hash delle coppie ( nome => valore )
      return (%DATI);
}
#====================================================================================
#====================================================================================
# dato che è una libreria deve ritornare un valore di tipo true
1;
#
#====================================================================================
