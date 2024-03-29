# Generated by Django 4.2.7 on 2023-11-30 18:37

import json
import random

from django.db import migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model("store", "Category")
    db_alias = schema_editor.connection.alias
    with open('data/categories.json', 'r') as file:
        data = json.load(file)
        for obj in data:
            Category.objects.using(db_alias).create(
                name=obj['category'],
                img_url=obj['img_url']
            )


def create_products(apps, schema_editor):
    Product = apps.get_model("store", "Product")
    Category = apps.get_model("store", "Category")
    db_alias = schema_editor.connection.alias
    with open('data/products.json', 'r') as file:
        data = json.load(file)
        for obj in data:
            Product.objects.using(db_alias).create(
                name=obj['name'],
                description=obj['description'],
                price=obj['price'],
                category=Category.objects.using(db_alias).get(name=obj['category']),
                img_url=obj['img_url'],
                stock_quantity=random.randint(1, 50),
                rate=random.uniform(2.0, 5.0)
            )


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_categories),
        migrations.RunPython(create_products)
    ]
