// Script che controlla la form di registrazione

//funzione che cancella il testo delle form al focus
function delTextFocus(el){
	if(el.value == el.defaultValue){
		el.value="";
	}
}

//funzione che va a riempire i campi della form con esempi
function controlli(){

	//array delli controlli
	var controll = [["form_username", "Username"],
					["form_useremail", "User e-mail"],
					["form_password", "Password"]];
					
	//Inserimento aiuti
	for (i = 0; i < 3; i++){
		var elem = document.getElementById(controll[i][0]);
		elem.defaultValue = controll[i][1];
		elem.style.color = "#515151";
	}
	
	//document.getElementById("form_useremail").focus();
	//document.getElementById("form_useremail").select();
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//funzione per il controllo della correttezza dei campi nella registrazione utenti
function form_control()
{

// Variabili associate ai campi del modulo
var username = document.getElementById("form_username").value;
var useremail = document.getElementById("form_useremail").value;
var pass = document.getElementById("form_password").value;

     
//creo le espressioni regolari
var name_re = /^([a-zA-Z0-9\_\*\-\+\!\?\,\:\;\.\xE0\xE8\xE9\xF9\xF2\xEC\x27])+$/;
var user_re = /^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
var pass_re = /^([a-zA-Z0-9\_\*\-\+\!\?\,\:\;\.\xE0\xE8\xE9\xF9\xF2\xEC\x27])+$/;


//array degli id span
var vettore = ["uname", "uemail", "pass"];

//se settati svuoto gli span di errore
for (i=0; i<3; i++) {
	if (document.getElementById(vettore[i]) != "") {
		document.getElementById(vettore[i]).innerHTML = "";
	}
}

//Effettua il controllo sul campo username
if ((username == "") || (username == "undefined") || (username == "Username")) {
	document.getElementById("uname").innerHTML = "Il campo è obbligatorio.";
    document.getElementById("form_username").focus();
    document.getElementById("form_username").select();
    return false;
}
else if (!name_re.test(username)) {
   	document.getElementById("uname").innerHTML = "Inserire il campo in modo corretto.";
  	document.getElementById("form_username").focus();
   	document.getElementById("form_username").select();
   	return false;

}//Effettua il controllo sul campo useremail
else if ((useremail == "") || (useremail == "undefined") || (useremail == "User e-mail")) {
	document.getElementById("uemail").innerHTML = "Il campo è obbligatorio.";
    document.getElementById("form_useremail").focus();
    document.getElementById("form_useremail").select();
    return false;
}
else if (!user_re.test(useremail)) {
   	document.getElementById("uemail").innerHTML = "Inserire il campo in modo corretto.";
  	document.getElementById("form_useremail").focus();
   	document.getElementById("form_useremail").select();
   	return false;
}//Effettua il controllo sul campo password
else if ((pass == "") || (pass == "undefined") || (pass == "Password")) {
    document.getElementById("pass").innerHTML = "Il campo è obbligatorio.";
    document.getElementById("form_password").focus();
    document.getElementById("form_password").select();
    return false; 
}
else if (!pass_re.test(pass)) {
   	document.getElementById("pass").innerHTML = "Inserire il campo in modo corretto.";
   	document.getElementById("form_password").focus();
   	document.getElementById("form_password").select();
   	return false;
}//Finiti i controlli se tutto ok invio i dati
else {
  	var form = document.getElementById("registrazione");
  	form.action = "../cgi-bin/reg_control.cgi";// qui ci va l'indirizzo del file cgi che gestirà l'accesso
	form.submit();
}
}