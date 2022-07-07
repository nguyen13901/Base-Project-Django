# Generated by Django 3.2.3 on 2022-06-30 03:43

from django.contrib.auth.base_user import BaseUserManager
from django.db import migrations, models


from api_account.constant import RoleData, UserData


def initial_role_data(apps, schema_editor):
    account_model = apps.get_model("api_account", "Account")
    role_model = apps.get_model("api_account", "Role")

    user_role = role_model.objects.filter(name="USER").first()
    accounts = []

    for user in UserData.users:
        accounts.append(account_model(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            is_staff=False,
            username=user['email'].split('@')[0],
            avatar=None,
            email=user["email"],
            address=user['address'],
            phone=user['phone'],
            age=user['age'],
            password=BaseUserManager().make_random_password(),
            role=user_role,
        ))

    account_model.objects.bulk_create(accounts)


class Migration(migrations.Migration):
    dependencies = [
        ('api_account', '0003_migrate_admin'),
    ]

    operations = [
        migrations.RunPython(initial_role_data, migrations.RunPython.noop)
    ]
