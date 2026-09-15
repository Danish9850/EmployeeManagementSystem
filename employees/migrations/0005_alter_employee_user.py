
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def assign_existing_employees_to_mohammad(apps, schema_editor):
    User = apps.get_model("auth", "User")

    Employee = apps.get_model("employees", "Employee")

    
    owner = User.objects.filter(username="Mohammad").first()

    if owner is None:
        raise RuntimeError(
            "User 'Mohammad' was not found. "
            "Migration stopped to protect existing employee data."
        )

    Employee.objects.filter(user__isnull=True).update(user=owner)


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0004_employee_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [

        migrations.RunPython(
            assign_existing_employees_to_mohammad,
            migrations.RunPython.noop,
        ),

        migrations.AlterField(
            model_name="employee",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]