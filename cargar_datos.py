import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dinonews.settings')
django.setup()

from noticias.models import Noticia
from datetime import date

# Crear noticias de ejemplo
noticias_ejemplo = [
    {
        'titulo': 'Descubrimiento de nuevo dinosaurio en Argentina',
        'fecha_publicacion': date(2026, 1, 15),
        'texto': 'Científicos argentinos han descubierto una nueva especie de dinosaurio en la provincia de Chubut. La investigación, realizada por el equipo del Dr. Jorge Acosta, revela características únicas que desafían lo que sabíamos sobre los titanosaurios. Este hallazgo abre nuevas perspectivas en el estudio de la evolución de los dinosaurios herbívoros del Mesozoico. El fósil ha sido datado en 90 millones de años y se encuentra en excelente estado de conservación.'
    },
    {
        'titulo': 'Revelaciones sobre el comportamiento social del Velociraptor',
        'fecha_publicacion': date(2026, 1, 20),
        'texto': 'Nuevas investigaciones del Instituto de Paleontología sugieren que los Velociraptores tenían un comportamiento social complejo. Los análisis de marcas en fósiles indican que cazaban en grupos coordinados, similar a los leones modernos. Este descubrimiento revoluciona nuestra comprensión sobre la inteligencia y los patrones de caza de estos depredadores. Los investigadores encontraron evidencia de comunicación entre individuos, lo que indica un nivel de cognición sorprendentemente alto.'
    },
    {
        'titulo': 'Proteína de dinosaurio extraída de colágeno de 80 millones de años',
        'fecha_publicacion': date(2026, 1, 25),
        'texto': 'Un equipo internacional de científicos ha logrado extraer y analizar proteínas intactas de colágeno de fósiles de dinosaurio con una antigüedad de 80 millones de años. Este hito representa un avance sin precedentes en la paleogenómica. Las proteínas analizadas provienen de un Brachiosaurus y mantienen una estructura molecular que permite a los investigadores entender mejor la estructura ósea de estos gigantes. Este descubrimiento abre la puerta a futuras investigaciones sobre el ADN antiguo.'
    },
    {
        'titulo': 'El Tyrannosaurus Rex probablemente tenía piel de colores vivos',
        'fecha_publicacion': date(2026, 2, 1),
        'texto': 'Modelados en 3D realizados por investigadores de la Universidad de Cambridge sugieren que el Tyrannosaurus Rex puede haber tenido una piel con colores vivos y patrones brillantes. Utilizando datos de aves modernas y análisis de fósiles de piel fosilizada, los científicos crearon visualizaciones que muestran posibles esquemas de coloración. Estos colores podrían haber servido tanto para atracción sexual como para comunicación interespecífica. El estudio desafía la percepción popular de un T-Rex completamente gris o marrón.'
    },
    {
        'titulo': 'Hallazgo de un nuevo nido de huevos de dinosaurio en Mongolia',
        'fecha_publicacion': date(2026, 2, 3),
        'texto': 'Paleontólogos de la Universidad de Ulan Bator han descubierto un nido intacto de huevos de dinosaurio en el desierto de Gobi de Mongolia. El nido contiene 24 huevos de lo que parece ser una especie de Oviraptorosauro. Lo más notable es que se encontraron restos de adultos cerca del nido, sugiriendo que los padres cuidaban los huevos. Este descubrimiento proporciona evidencia sólida sobre el comportamiento reproductivo y paternal de los dinosaurios, similar al de muchas aves modernas.'
    }
]

# Insertar noticias en la base de datos
for noticia_data in noticias_ejemplo:
    noticia, created = Noticia.objects.get_or_create(
        titulo=noticia_data['titulo'],
        defaults={
            'fecha_publicacion': noticia_data['fecha_publicacion'],
            'texto': noticia_data['texto']
        }
    )
    if created:
        print(f"✓ Noticia creada: {noticia.titulo}")
    else:
        print(f"→ Noticia ya existe: {noticia.titulo}")

print("\n¡Noticias de ejemplo cargadas exitosamente!")
