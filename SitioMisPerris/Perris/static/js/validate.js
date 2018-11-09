function valrut() {
	var rut = document.getElementById("id_rut").value;
	rut = rut.replace(/\./g,"");
	rut = rut.replace(/-/g,"");
	ruts = rut.substring(0,8);
	rutv = rut.substring(8,9);
	if(rut.length > 0){
	if(rut.length == 9){
			document.getElementById("id_rut").style.borderColor = "green";
			if(isNaN(ruts)){
				rut.value = ""
				document.getElementById("id_rut").focus();
				document.getElementById("id_rut").value = null;
				document.getElementById("id_rut").style.borderColor = "red";
				alert('el run solo puede contener numeros');
				}else{
					if(isNaN(rutv)){
						if(rutv.toUpperCase() != 'K'){
							document.getElementById("id_rut").focus();
							document.getElementById("id_rut").value = null;
							document.getElementById("id_rut").style.borderColor = "red";
							alert('numero verificador malo');
						}
					}else{
						document.getElementById("id_rut").style.borderColor = "green";
					}
				}
	}else{
		rut.value = ""
		document.getElementById("id_rut").focus();
		document.getElementById("id_rut").value = null;
		document.getElementById("id_rut").style.borderColor = "red";
		alert('el rut debe tener un largo de 9 caracteres(sin puntos ni guion)');

	//alert(rut);
	}
	}
}
function valmail(){
	var mail = document.getElementById("id_email").value;
	if(mail.length > 0){
		if(validar_email(mail)){
			document.getElementById("id_email").style.borderColor = "green";
			if(mail.indexOf('@') == -1){
				document.getElementById("id_email").focus();
				document.getElementById("id_email").value = null;
				document.getElementById("id_email").style.borderColor = "red";
				alert('formato de mail no aceptado');
			}else{
				document.getElementById("id_email").style.borderColor = "green";
			}
		}else{
			document.getElementById("id_email").focus();
			document.getElementById("id_email").value = null;
			document.getElementById("id_email").style.borderColor = "red";
			alert('formato de mail no aceptado');
		}
	}
}
function validar_email( email ) 
{
    var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email) ? true : false;
}
function valnombre(){
 	var nombre = document.getElementById("id_nombre").value;
 	if(nombre.length > 0){
	 	if(isNaN(nombre)){
			document.getElementById("id_nombre").style.borderColor = "green";
	 		var nombrediv = nombre.split(" ");
	 		var palnombre = nombrediv.length;
	 		if(palnombre < 2){
	 		document.getElementById("id_nombre").focus();
			document.getElementById("id_nombre").value = null;
			document.getElementById("id_nombre").style.borderColor = "red";
			alert('el nombre debe contener al menos 2 palabras');
	 		}else{
			document.getElementById("id_nombre").style.borderColor = "green";
	 		}
	 	}else{
	 		document.getElementById("id_nombre").focus();
			document.getElementById("id_nombre").value = null;
			document.getElementById("id_nombre").style.borderColor = "red";
			alert('el nombre no puede contener numeros');
	 	}
 	}
}
function valdate(){
	var fecha = document.getElementById("id_fecha").value;
	fecha = fecha.replace(/-/g,"");
	var anio = fecha.substring(0,4);
	var mes = fecha.substring(4,6);
	var dia = fecha.substring(6,8);
	var dia1 = parseInt(dia);
	var mes1 = parseInt(mes);
	var anio1 = parseInt(anio);
	if(fecha != ""){
		if( 0 < dia1 && dia1 < 32 && 0 < mes1 && mes1 < 13 && 1900 < anio1  && anio1< 2019 && fecha.length == 8 ){
			if (1900 < anio1  && anio1< 2002) {
			document.getElementById("id_fecha").style.borderColor = "green";
			}else{
				alert("El año de nacimiento debe ser menor que 2001");
				document.getElementById("id_fecha").focus();
				document.getElementById("id_fecha").value = null;
				document.getElementById("id_fecha").style.borderColor = "red";
			}
		}else{
			alert("Formato de fecha invalido");
			document.getElementById("id_fecha").focus();
			document.getElementById("id_fecha").value = null;
			document.getElementById("id_fecha").style.borderColor = "red";
		}
	}
}
function valtel(){
	var tel = document.getElementById("telefono").value;
	tel = tel.replace(/\+56/g,"");
	if(tel != ""){
		if(tel.length == 9){

			document.getElementById("telefono").style.borderColor = "green";
		}else{
			alert("El telefono debe contener 9 digitos (sin contar +56)");
			document.getElementById("telefono").focus();
			document.getElementById("telefono").value = null;
			document.getElementById("telefono").style.borderColor = "red";
		}
	}
}
function valtodo(){
	var rut = document.getElementById("id_rut").value;
	var mail = document.getElementById("id_email").value;
 	var nombre = document.getElementById("id_nombre").value;
	var fecha = document.getElementById("id_fecha").value;
	var tel = document.getElementById("telefono").value;
	if(rut == null || rut == ""){
		alert("el rut debe ser ingresado");
		document.getElementById("id_rut").focus()
	}else{
		if(mail == null || mail == ""){
			alert("el mail debe ser ingresado");
			document.getElementById("id_email").focus()
		}else{
			if(nombre == null || nombre == ""){
				alert("el nombre debe ser ingresado");
				document.getElementById("id_nombre").focus()
			}else{
				if(fecha == null || fecha == ""){
					alert("el fecha debe ser ingresado");
					document.getElementById("id_fecha").focus()
				}else{
					if(tel == null || tel == ""){
						alert("el telefono debe ser ingresado");
						document.getElementById("telefono").focus()
					}else{
						location.href = "xd.html";
					}
				}
			}
		}
	}
}
function valsel(){
	var region = document.f1.pais.value;
	var ciudad = document.f1.provincia.value;
	var casa = document.f1.casa.value;
	if(region != 0){
		if(ciudad != "-"){
			if(casa != 0){
				location.href = "index.html";
			}else{
				alert("seleccione tipo de vivienda");
			}
		}else{
			alert("seleccione ciudad")
		}
	}else{

			alert("seleccione region")
	}
}



