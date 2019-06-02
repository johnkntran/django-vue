from django.db import migrations, models
from django.apps import apps
from stocks.models import Stock, Portfolio


def populate_data(apps, schema_editor):
    ford = Stock.objects.create(
        name='Ford',
        symbol='F',
        exchange='NYSE',
        price=1293.46,
        active=True,
    )
    wayfair = Stock.objects.create(
        name='Wayfair',
        symbol='W',
        exchange='NASDAQ',
        price=745.82,
        active=True,
    )
    kellogg = Stock.objects.create(
        name='K',
        symbol='Kellogg',
        exchange='NYSE',
        price=89.51,
        active=True,
    )
    visa = Stock.objects.create(
        name='V',
        symbol='Visa',
        exchange='NASDAQ',
        price=235.47,
        active=True,
    )
    marvel = Stock.objects.create(
        name='Marvel',
        symbol='MVL',
        exchange='NYSE',
        price=7.75,
        active=False,
    )
    shiny_stars = Portfolio.objects.create(name='Shiny Stars', slug='@ShinyStars')
    unknown_hits = Portfolio.objects.create(name='Unknown Hits', slug='@UnknownHits')
    shiny_stars.stocks.add(visa)
    shiny_stars.stocks.add(marvel)
    shiny_stars.stocks.add(ford)
    unknown_hits.stocks.add(kellogg)
    unknown_hits.stocks.add(wayfair)


def reverse(apps, schema_editor):
    Stock.objects.all().delete()
    Portfolio.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_code=reverse)
    ]
