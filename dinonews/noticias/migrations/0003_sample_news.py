from django.db import migrations


def create_examples(apps, schema_editor):
    Noticia = apps.get_model('noticias', 'Noticia')
    examples = [
        {
            'titulo': 'Descubren huellas de dinosaurios en Chile',
            'fecha_publicacion': '2025-11-10',
            'texto': 'Un equipo de paleontólogos encontró huellas de un gran carnívoro en la región de Magallanes.',
        },
        {
            'titulo': 'Nueva especie de dinosaurio con plumas',
            'fecha_publicacion': '2024-06-21',
            'texto': 'Se ha descrito una especie emplumada que vivió en lo que hoy es Mongolia.',
        },
        {
            'titulo': 'Construyen réplica de esqueleto de T-Rex',
            'fecha_publicacion': '2023-09-05',
            'texto': 'Un museo en España inauguró la réplica más grande jamás hecha de Tyrannosaurus rex.',
        },
    ]
    for data in examples:
        if not Noticia.objects.filter(titulo=data['titulo']).exists():
            Noticia.objects.create(**data)


def noop(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_create_admin'),
    ]

    operations = [
        migrations.RunPython(create_examples, noop),
    ]
