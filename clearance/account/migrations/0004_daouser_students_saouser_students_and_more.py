# Generated by Django 4.2.4 on 2023-08-13 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_screenuser_student_screenuser_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='daouser',
            name='students',
            field=models.ManyToManyField(related_name='sdept_students', to='account.studentuser'),
        ),
        migrations.AddField(
            model_name='saouser',
            name='students',
            field=models.ManyToManyField(related_name='faculty_students', to='account.studentuser'),
        ),
        migrations.AddField(
            model_name='senateuser',
            name='students',
            field=models.ManyToManyField(related_name='gen_students', to='account.studentuser'),
        ),
        migrations.AddField(
            model_name='uaouser',
            name='students',
            field=models.ManyToManyField(related_name='all_students', to='account.studentuser'),
        ),
        migrations.AlterField(
            model_name='screenuser',
            name='students',
            field=models.ManyToManyField(related_name='screeners', to='account.studentuser'),
        ),
    ]