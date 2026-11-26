# ==========================================
# VARIABLES DEL JUGADOR Y ESTADO
# ==========================================
default nombre_jugador = "Alex"

# ==========================================
# DEFINICIÓN DE PERSONAJES
# ==========================================

# Personaje principal (usa el nombre elegido por el jugador)
define yo = DynamicCharacter("nombre_jugador", color="#c76767")

# Pensamientos en primera persona (sin etiqueta de nombre, en cursiva)
define p = Character(None, what_italic=True, what_color="#5c493e")

# Elenco docente y guía
define alejandro = Character("Dr. Alejandro", color="#3b6978")
define valentina = Character("Dra. Valentina", color="#7c5e99")
define ricardo   = Character("Dr. Ricardo", color="#4f7759")
define tibi      = Character("Tibi", color="#d9823b")
define estudiante = Character("Estudiante del grupo", color="#6e635f")

# ==========================================
# PLACEHOLDERS TEMPORALES (Reemplazar al tener el arte)
# ==========================================
image bg universidad_manana = Composite((1920, 1080), (0, 0), Solid("#d8e6df"), (0, 0), Text("BG: Afuera de la universidad — Mañana", xalign=0.5, yalign=0.2, size=40, color="#4a382e"))
image bg aula_dia           = Composite((1920, 1080), (0, 0), Solid("#ebe3d5"), (0, 0), Text("BG: Aula 204 — Primera clase", xalign=0.5, yalign=0.2, size=40, color="#4a382e"))
image bg pasillo_dia        = Composite((1920, 1080), (0, 0), Solid("#e2dcd2"), (0, 0), Text("BG: Pasillo universitario", xalign=0.5, yalign=0.2, size=40, color="#4a382e"))
image bg habitacion_tarde   = Composite((1920, 1080), (0, 0), Solid("#f2dec4"), (0, 0), Text("BG: Habitación — Tarde", xalign=0.5, yalign=0.2, size=40, color="#4a382e"))

image alejandro explica = Composite((450, 850), (0, 0), Solid("#3b6978aa"), (0, 0), Text("Sprite:\nDr. Alejandro\n(Explicando)", xalign=0.5, yalign=0.5, size=32, color="#ffffff"))
image tibi saludo       = Composite((350, 350), (0, 0), Solid("#f4a261cc"), (0, 0), Text("Tablet:\nTibi Perone\n(Saludando)", xalign=0.5, yalign=0.5, size=28, color="#4a382e"))