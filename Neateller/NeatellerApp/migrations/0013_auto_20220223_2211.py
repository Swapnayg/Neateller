# Generated by Django 3.2.10 on 2022-02-23 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeatellerApp', '0012_auto_20220223_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='randochoice_service',
            name='multiple',
            field=models.BooleanField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='about_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 128721), null=True),
        ),
        migrations.AlterField(
            model_name='about_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 128721), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 130721), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 130721), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 134721), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 134721), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 126720), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 126720), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 126720), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 126720), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 131721), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 131721), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 127721), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 127721), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 122720), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 122720), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 127721), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 127721), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 134721), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 134721), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 129721), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 129721), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 133721), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 133721), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 133721), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 133721), null=True),
        ),
        migrations.AlterField(
            model_name='material_perhour',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 132721), null=True),
        ),
        migrations.AlterField(
            model_name='material_perhour',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 132721), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 131721), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 131721), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 123720), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 123720), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 123720), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 123720), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 124720), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 124720), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 125720), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 125720), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 130721), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 130721), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 125720), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 125720), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 128721), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 128721), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 125720), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 125720), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 121720)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 23, 22, 11, 20, 121720)),
        ),
    ]
