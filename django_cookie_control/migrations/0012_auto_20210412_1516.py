# Generated by Django 2.2.13 on 2021-04-12 13:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_cookie_control', '0011_auto_20200904_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookiecontrol',
            name='excludedCountries',
            field=django_countries.fields.CountryField(blank=True, help_text='[Pro version only] able the module entirely for visitors outside of the EU. Either add the value all, or a list of 2 letter ISO codes for the countries you wish to disable the module', max_length=758, multiple=True),
        ),
    ]
