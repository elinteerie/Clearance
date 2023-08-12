from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission



class Department(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    departments = models.ManyToManyField(Department)
    
    
    def __str__(self) -> str:
        return self.name
    
class DefaultUser(AbstractUser):
    pass
    

class StudentUser(models.Model):
    
    RELIGION_CHOICES = [
    ('Christian', 'Christian'),
    ('Islam', 'Islam'),
    ('Traditional', 'Traditional'),
    ('Others', 'Others'),
    ]

    MARITAL_STATUS_CHOICES = [
    ('Single', 'Single'),
    ('Divorced', 'Divorced'),
    ('Married', 'Married'),
    ('Widow', 'Widow'),]
    
    
    NEXT_OF_KIN_CHOICES = [
    ('Brother', 'Brother'),
    ('Sister', 'Sister'),
    ('Father', 'Father'),
    ('Wife', 'Wife'),
    ('Husband', 'Husband'),
    ('Other', 'Other'),
    ]
    
    def profile_picture_upload_path(self, instance, filename):
        return f'media/{instance.department.name}/{instance.faculty.name}/{instance.username}/{filename}'
    student = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, related_name='student_user')
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_department', null=True, blank=True)
    faculty =  models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='student_faculty', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    state_of_origin = models.CharField(max_length=100, null=True, blank=True)
    local_government = models.CharField(max_length=100, null=True, blank=True)
    permenant_address = models.TextField(null=True, blank=True)
    contact_address = models.TextField(null=True, blank=True)
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, default='Christian')
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_address = models.TextField(null=True, blank=True)
    next_of_kin_relationship = models.CharField(max_length=20, choices=NEXT_OF_KIN_CHOICES, default='Brother')
    next_of_kin_telephone = models.CharField(max_length=50, null=True, blank=True)
    sponsor_name = models.CharField(max_length=100, null=True, blank=True)
    sponsor_address = models.TextField(null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, default='Single')
    signature = models.ImageField(upload_to='media/username/signature/', null=True, blank=True)
    ict_cleared = models.BooleanField(default=False)
    dept_cleared = models.BooleanField(default=False)
    profile_picture = models.FileField(upload_to=profile_picture_upload_path, null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = "StudentUsers"
    
    def __str__(self) -> str:
        return self.username

     
    
class ScreenUser(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='screen_department', null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='screen_department', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='screen_users')
    user_permissions = models.ManyToManyField(Permission, related_name='scrren_users')
    
    class Meta:
        verbose_name_plural = "ScreenUsers"
        
    

class UAOUser(AbstractUser):
    signature = models.FileField(upload_to='media/uao/signature/')
    stamp = models.FileField(upload_to='media/uao/stamp/')
    groups = models.ManyToManyField(Group, related_name='uao_users')
    user_permissions = models.ManyToManyField(Permission, related_name='uao_users')
    
    class Meta:
        verbose_name_plural = "UAOUsers"
    
class DAOUser(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dao_department', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='dao_users')
    user_permissions = models.ManyToManyField(Permission, related_name='dao_users')
    
    class Meta:
        verbose_name_plural = "DAOUsers"
    
class SenateUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='senate_users')
    user_permissions = models.ManyToManyField(Permission, related_name='senate_users')
    
    class Meta:
        verbose_name_plural = "SenateUsers"
    
    
    
class SAOUser(AbstractUser):
    faculty =  models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='sao_faculty', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='sao_users')
    user_permissions = models.ManyToManyField(Permission, related_name='sao_users')
    
    
    class Meta:
        verbose_name_plural = "SAOUsers"
    

class Current_Admission_Session(models.Model):
    
    session = models.CharField(max_length=20)
    

class ConcreteUser(ScreenUser, AbstractUser):
    pass

class ConcreteUser(StudentUser, AbstractUser):
    pass