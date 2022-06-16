# Generated by Django 3.2.13 on 2022-06-16 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('descricao',),
            },
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ('descricao',), 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
    ]