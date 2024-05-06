const url_servidor= "http://127.0.0.1:5000";

$(document).on('click', '#cerrar-btn', function () {
    var $popup = $('.cont_pantalla_emergente main');
    var $overlay = $('#popup-overlay');
    $popup.remove();
    $overlay.hide();
});

function crearMensaje(titulo, mensaje, redireccion) {
    var $contenedor = $('#mensaje');
    var $overlay = $('#popup-overlay');

    var $popup = $('<div>').addClass('popup').addClass(titulo);
    var $popupTitulo = $('<h2>').text(titulo);
    var $popupMensaje = $('<p>').text(mensaje);
    var $closeButton = $('<button>').text('Cerrar').addClass('close-btn');

    $closeButton.on('click', function () {
        if (redireccion) {
            $popup.remove();
            $overlay.hide();
            window.location.href = redireccion;
        } else {
            $popup.remove();
            $overlay.hide();
        }
    });

    $popup.append($popupTitulo, $popupMensaje, $closeButton);
    $contenedor.append($popup);
    $overlay.show();
}

function BuscarEnTabla(tabla,textoBusqueda){
    //tabla es el id de la tabla a buscar en el html
    $(tabla+' tbody tr').each(function() {
        var coincide = false;
        $(this).find('td').each(function() {
            if ($(this).text().toLowerCase().includes(textoBusqueda)) {
                coincide = true;
                return false; // Sale del bucle each() interno
            }
        });
        if (coincide) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

// Función para agregar asteriscos a campos requeridos
function agregarAsteriscosARequeridos() {
    // Obtener todos los elementos <input> con el atributo 'required'
    const requiredInputs = document.querySelectorAll('input[required]');
    // Iterar sobre cada elemento y agregar un asterisco (*) si no está presente
    requiredInputs.forEach(function(input) {
        // Obtener el elemento <label> asociado al <input> (o crear uno si no existe)
        let label = document.querySelector(`label[for="${input.id}"]`);

        if (!label) {
            // Si no hay un <label> asociado, crear uno
            label = document.createElement('label');
            label.setAttribute('for', input.id);
            input.parentNode.insertBefore(label, input);
        }

        // Agregar el asterisco (*) al final del contenido HTML del <label> si no está presente
        if (!label.innerHTML.includes('<span style="color: red;">*</span>')) {
            label.innerHTML += ' <span style="color: red;">*</span>';
        }
    });
}
// Ejecutar la función después de que se haya cargado todo el contenido
document.addEventListener('DOMContentLoaded', function() {
    agregarAsteriscosARequeridos();

    // También puedes usar MutationObserver para manejar cambios dinámicos en el DOM
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                // Si hay cambios en el DOM, volver a ejecutar la función
                agregarAsteriscosARequeridos();
            }
        });
    });

    // Observar cambios en el DOM (útil para contenido dinámico como pop-ups)
    observer.observe(document.body, { childList: true, subtree: true });
});

