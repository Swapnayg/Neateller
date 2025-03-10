# Generated by Django 3.2.10 on 2022-02-23 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeatellerApp', '0009_auto_20220220_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice_service',
            name='choiseserNumber',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='choice_service',
            name='popup',
            field=models.BooleanField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='about_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 76037), null=True),
        ),
        migrations.AlterField(
            model_name='about_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 76037), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 77037), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 77037), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 81037), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 81037), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 74037), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 74037), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 74037), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 74037), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 79037), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 79037), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 75037), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 75037), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 70037), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 70037), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 75037), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 75037), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 82037), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 82037), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 77037), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 77037), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 81037), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 81037), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 80037), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 80037), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 79037), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 79037), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 70037), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 70037), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 71037), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 71037), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 72037), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 72037), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 72037), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 72037), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 78037), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 78037), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 73037), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 73037), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 75037), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 75037), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 73037), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 73037), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 69036)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 21, 46, 22, 69036)),
        ),
    ]
