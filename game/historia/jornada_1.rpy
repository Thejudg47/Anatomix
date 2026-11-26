# ==============================================================================
# JORNADA 1 — El lenguaje del cuerpo
# Modalidad: introductoria
# Objetivo de aprendizaje: posición anatómica, planos, términos direccionales,
# regiones y niveles de organización.
# ==============================================================================

label jornada_1:
    $ save_name = "Jornada 1 - El lenguaje del cuerpo"
    jump j1_escena_1


# ------------------------------------------------------------------------------
# ESCENA 1. Afuera de la universidad — mañana (J01-S01)
# ------------------------------------------------------------------------------
label j1_escena_1:
    scene bg universidad_manana with fade
    # TODO AUDIO: Ambiente exterior (autos a distancia, conversaciones, pájaros)
    pause 1.0

    p "Hoy empieza algo que llevo mucho tiempo imaginando. También empieza todo lo que todavía no sé."

    yo "Hola. Soy [nombre_jugador] y hoy comienzo la carrera de Medicina. La materia que más me impone este semestre es Anatomía."

    p "Mi papá siempre dice que conocer el cuerpo es aprender a mirar con atención. Ojalá yo pueda aprender a hacerlo."

    # TODO SFX: Sonido de notificación de bienvenida de la universidad
    "{i}(Suena una notificación de bienvenida de la universidad en tu teléfono. Revisas tu horario.){/i}"

    yo "Aula 204… Bueno. Primer paso."

    jump j1_escena_2


# ------------------------------------------------------------------------------
# ESCENA 2. Aula — primera clase (J01-S02)
# ------------------------------------------------------------------------------
label j1_escena_2:
    scene bg aula_dia with dissolve
    # TODO AUDIO: Susurros de aula, sillas, pasos, marcador en pizarra

    show alejandro explica at right with dissolve
    # TODO PROPS: Pizarra con frase "Anatomía: describir para comprender"

    alejandro "Buenos días. Antes de memorizar nombres, necesitamos aprender a describir con precisión. La anatomía tiene un lenguaje común; nos permite hablar del cuerpo sin depender de “por aquí” o “por allá”."

    p "Un lenguaje nuevo. Eso sí puedo aprenderlo, palabra por palabra."

    alejandro "Empezaremos por la posición anatómica. No es una postura casual: es el punto de referencia para describir estructuras y relaciones."

    # TODO UI: Superponer esquema neutro del cuerpo en panel de cuaderno

    alejandro "También veremos planos y términos de dirección. No busco que repitan una lista sin contexto. Quiero que puedan explicar dónde está una estructura con respecto a otra."

    yo "¿Y si confundo derecha e izquierda al observar una imagen?"

    alejandro "Entonces volvemos al punto de referencia, revisamos la orientación y lo intentamos otra vez. En anatomía, comprobar es parte del trabajo."

    hide alejandro with dissolve
    jump j1_escena_3


# ------------------------------------------------------------------------------
# ESCENA 3. Pasillo y acceso a Quizatomy (J01-S03)
# ------------------------------------------------------------------------------
label j1_escena_3:
    scene bg pasillo_dia with dissolve
    # TODO AUDIO: Pasos que se detienen, sonido breve al encender la tablet

    "{i}(Al salir del aula, revisas la tablet entregada para la materia. En la pantalla aparece el icono de Quizatomy.){/i}"

    show tibi saludo at center with zoomin

    tibi "¡Hola! Soy Tibi Perone. Te acompañaré en Quizatomy. No voy a contestar por ti, pero sí puedo ayudarte a fijarte en las pistas."

    yo "¿Y si no sé ninguna?"

    tibi "Empezamos con una, luego conectamos otra. La idea es que practiques cómo recordar y cómo orientarte."

    yo "Está bien. Vamos con la primera."

    tibi "Elige un ejercicio y observa el cuerpo completo antes de acercarte a los detalles."

    # [BLOQUE DE JUEGO: orientación anatómica, planos y asociación de términos]
    call quizatomy_j1_placeholder

    hide tibi with dissolve
    jump j1_escena_4


# ------------------------------------------------------------------------------
# ESCENA 4. Cierre de jornada — habitación (J01-S04)
# ------------------------------------------------------------------------------
label j1_escena_4:
    scene bg habitacion_tarde with fade
    # TODO AUDIO: Ambiente interior tranquilo, sonido de hojas y lápiz

    "{i}(Guardas la tablet sobre el escritorio y preparas una pequeña pila de flashcards.){/i}"

    p "Hoy aprendí que describir con claridad requiere un punto de referencia. Mañana voy a probar si puedo recordar los términos sin mirar mis apuntes."

    # TODO SFX: Notificación suave de Quizatomy
    tibi "(Notificación) Repaso opcional disponible: términos de orientación anatómica."

    p "No tengo que terminarlo todo esta noche. Pero puedo dejar preparado el primer paso."

    # TODO: Conectar con jump jornada_2 cuando esté programada
    "{b}Fin de la Jornada 1.{/b}"
    return


# ------------------------------------------------------------------------------
# MARCADOR TEMPORAL DEL MINIJUEGO DE QUIZATOMY (JORNADA 1)
# ------------------------------------------------------------------------------
label quizatomy_j1_placeholder:
    window hide
    centered "{size=34}{color=#4a382e}[ BLOQUE DE JUEGO: QUIZATOMY — JORNADA 1 ]\n\nOrientación anatómica, planos y asociación de términos.\n(Aquí se abrirá la interfaz interactiva con retroalimentación explicativa){/color}{/size}"
    window show
    return