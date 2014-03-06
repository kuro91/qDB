// scripr che controlla i cookies nella pagina index
//=======================================================================
//=======================================================================
// funzione che legge il cookie con nome nomeCookie
function leggiCookie(nomeCookie)
{
  if (document.cookie.length > 0)
  {
    var inizio = document.cookie.indexOf(nomeCookie + "=");
    if (inizio != -1)
    {
      inizio = inizio + nomeCookie.length + 1;
      var fine = document.cookie.indexOf(";",inizio);
      if (fine == -1) fine = document.cookie.length;
      return unescape(document.cookie.substring(inizio,fine));
    }else{
       return false;
    }
  }
  return false;
}
//=======================================================================
// funzione che mostra il bottone d'accesso se non c'è il cookie desiderato
// altrimenti mostra il nome dell'utente e il bottone logout
function cookie_control()
{
	if(navigator.cookieEnabled){ // i cookie sono attivi
		var username = leggiCookie('LDV');
	
		if(username){
			var elem_acces = document.getElementById("acces");
	
			elem_acces.style.display = "none";
	
			document.getElementById("loggato").innerHTML = "<p>Benvenuto <strong>" + username + "</stong> </p><a href=\"../cgi-bin/logout_control.cgi\">Logout</a>";
		}
	}
	else{ // i cookie non sono attivi
		window.alert("Per una navigazione corretta abilitare i cookies!"); // crea pop-up di avvertimento
	}
}
