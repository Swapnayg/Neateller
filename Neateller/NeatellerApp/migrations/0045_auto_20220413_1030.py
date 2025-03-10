# Generated by Django 3.2.10 on 2022-04-13 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeatellerApp', '0044_auto_20220413_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment_transaction',
            options={'verbose_name': 'Payment Transactions', 'verbose_name_plural': 'Payment Transactions'},
        ),
        migrations.AlterField(
            model_name='about_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 251173), null=True),
        ),
        migrations.AlterField(
            model_name='about_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 251173), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 252173), null=True),
        ),
        migrations.AlterField(
            model_name='addon_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 252173), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 256174), null=True),
        ),
        migrations.AlterField(
            model_name='advance_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 256174), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 249173), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_categorie',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 249173), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 248173), null=True),
        ),
        migrations.AlterField(
            model_name='apartment_unit',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 248173), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 254174), null=True),
        ),
        migrations.AlterField(
            model_name='choice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 254174), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 249173), null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 249173), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 244173), null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 244173), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 249174), null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updated_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 249174), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 257174), null=True),
        ),
        migrations.AlterField(
            model_name='date_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 257174), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 251173), null=True),
        ),
        migrations.AlterField(
            model_name='description_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 251173), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 256174), null=True),
        ),
        migrations.AlterField(
            model_name='internaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 256174), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 255174), null=True),
        ),
        migrations.AlterField(
            model_name='localaddre_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 255174), null=True),
        ),
        migrations.AlterField(
            model_name='material_perhour',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 254174), null=True),
        ),
        migrations.AlterField(
            model_name='material_perhour',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 254174), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 253174), null=True),
        ),
        migrations.AlterField(
            model_name='offer_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 253174), null=True),
        ),
        migrations.AlterField(
            model_name='payment_transaction',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 258174), null=True),
        ),
        migrations.AlterField(
            model_name='payment_transaction',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 258174), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 245173), null=True),
        ),
        migrations.AlterField(
            model_name='popupbuilders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 245173), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 245173), null=True),
        ),
        migrations.AlterField(
            model_name='productcoupons',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 245173), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 246173), null=True),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 246173), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 247173), null=True),
        ),
        migrations.AlterField(
            model_name='productratings',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 247173), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 252173), null=True),
        ),
        migrations.AlterField(
            model_name='randochoice_service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 252173), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 248173), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 248173), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 250173), null=True),
        ),
        migrations.AlterField(
            model_name='service_section',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 250173), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 247173), null=True),
        ),
        migrations.AlterField(
            model_name='servicecategories',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 247173), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 243173)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 243173)),
        ),
        migrations.AlterField(
            model_name='usersaddress',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 257174), null=True),
        ),
        migrations.AlterField(
            model_name='usersaddress',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 10, 30, 46, 257174), null=True),
        ),
    ]
