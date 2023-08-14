from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver




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
    USER_TYPES = [
        ('DAO', 'DAO'),
        ('SAO', 'SAO'),
        ('SENATE', 'SENATE'),
        ('SCREEN', 'SCREEN'),
        ('STUDENT', 'STUDENT'),
        ('UAO', 'UAO'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    

class StudentUser(models.Model):
    
    RELIGION_CHOICES = [
    ('Christian', 'Christian'),
    ('Islam', 'Islam'),
    ('Traditional', 'Traditional'),
    ('Others', 'Others'),
    ]
    
    SEX_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
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
    
    def profile_picture_upload_path(instance, filename):
        return f'media/{instance.faculty.name}/{instance.department.name}/{instance.student.username}/{filename}'
    
    student = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, related_name='student_user', unique=True)
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_department', null=True, blank=True)
    faculty =  models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='student_faculty', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, default='Male')
    nationality = models.CharField(max_length=50, null=True, blank=True)
    place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    state_of_origin = models.CharField(max_length=100, null=True, blank=True)
    local_government = models.CharField(max_length=100, null=True, blank=True)
    permenant_address = models.TextField(null=True, blank=True)
    contact_address = models.TextField(null=True, blank=True)
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, default='Christian')
    next_of_kin_name = models.CharField(max_length=100, null=True, blank=True)
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
        return self.student.username

     
    
class ScreenUser(models.Model):
    screener = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, related_name='screener_user')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='screen_department', null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='screen_department', null=True, blank=True)
    students = models.ManyToManyField(StudentUser, related_name='screeners')
    
    
    class Meta:
        verbose_name_plural = "ScreenUsers"
        
    def __str__(self) -> str:
        return self.screener.username
        
    

class UAOUser(models.Model):
    uao = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, related_name='uao_user')
    signature = models.FileField(upload_to='media/uao/signature/')
    stamp = models.FileField(upload_to='media/uao/stamp/')
    students = models.ManyToManyField(StudentUser, related_name='all_students')
    
    class Meta:
        verbose_name_plural = "UAOUsers"
    
class DAOUser(models.Model):
    dao = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, related_name='dao_user')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dao_department', null=True, blank=True)
    students = models.ManyToManyField(StudentUser, related_name='sdept_students')
    
    class Meta:
        verbose_name_plural = "DAOUsers"
    
class SenateUser(models.Model):
    senate = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, related_name='senate_user')
    students = models.ManyToManyField(StudentUser, related_name='gen_students')
    
    class Meta:
        verbose_name_plural = "SenateUsers"
    
    
    
class SAOUser(models.Model):
    sao = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, related_name='sao_user')
    faculty =  models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='sao_faculty', null=True, blank=True)
    students = models.ManyToManyField(StudentUser, related_name='faculty_students')
    
    
    class Meta:
        verbose_name_plural = "SAOUsers"
    
class Current_Admission_Session(models.Model):
        session = models.CharField(max_length=10)
        
        def __str__(self) -> str:
            return self.session
        
        
@receiver(post_save, sender=StudentUser)
def add_student_to_screener(sender, instance, created, **kwargs):
    if created and instance.department:
        screen_user = ScreenUser.objects.filter(department=instance.department).first()
        doa_user = DAOUser.objects.filter(department=instance.department).first()
        print(screen_user)
        if screen_user:
            screen_user.students.add(instance)
        if doa_user:
            doa_user.students.add(instance)
            
            
            
@receiver(post_save, sender=StudentUser)
def add_student_to_faculty(sender, instance, created, **kwargs):
    if created and instance.faculty:
        sao_user = SAOUser.objects.filter(faculty=instance.faculty).first()
        if sao_user:
            sao_user.students.add(instance)
            
#Unfinshed codes        
@receiver(post_save, sender=DefaultUser)
def create_related_instance(sender, instance, created, **kwargs):
    if created and instance.user_type == 'STUDENT':
        StudentUser.objects.create(student=instance)
    elif created and instance.user_type == 'UAO':
        UAOUser.objects.create(uao=instance)
    # Add more cases for other user types if needed
    
    
post_save.connect(create_related_instance, sender=DefaultUser)

            

