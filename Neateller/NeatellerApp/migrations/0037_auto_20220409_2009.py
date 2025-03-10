# Generated by Django 3.2.10 on 2022-04-09 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeatellerApp', '0036_auto_20220409_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 381395), null=True),
        ),
        migrations.AlterField(
            model_name='about_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 381395), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 382396), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 382396), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 387396), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 387396), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 379395), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 379395), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 379395), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 379395), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 384396), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 384396), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 379395), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 380395), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 375395), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 375395), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 380396), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 380396), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 387396), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 387396), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 382396), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 382396), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 386396), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 386396), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 385396), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 385396), null=True),
        ),
        migrations.AlterField(
            model_name='material_perhour',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 385396), null=True),
        ),
        migrations.AlterField(
            model_name='material_perhour',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 385396), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 383396), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 383396), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 375395), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 375395), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 376395), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 376395), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 377395), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 377395), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 377395), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 377395), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 383396), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 383396), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 378395), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 378395), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 380395), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 380395), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 378395), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 378395), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 374395)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 374395)),
        ),
        migrations.AlterField(
            model_name='usersaddress',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 388396), null=True),
        ),
        migrations.AlterField(
            model_name='usersaddress',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 9, 20, 9, 55, 388396), null=True),
        ),
    ]
