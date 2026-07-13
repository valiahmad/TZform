from django.db import models



class Service(models.Model):

    code = models.CharField(
        max_length=30,
        unique=True
    )

    title = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'نوع خدمت'
        verbose_name_plural = 'نوع خدمات'
    



class Tazkera(models.Model):

    # Applicant Information
    full_name = models.CharField(max_length=255, null=True, verbose_name='اسم و تخلص')
    father_name = models.CharField(max_length=100, null=True, verbose_name='اسم پدر')
    grandfather_name = models.CharField(max_length=100, null=True, verbose_name='اسم پدرکلان')

    place_of_birth = models.CharField(max_length=100, null=True, verbose_name='محل تولد')
    date_of_birth = models.CharField(max_length=10, null=True, verbose_name='تاریخ تولد')

    marital_status = models.CharField(max_length=30, null=True, verbose_name='حالت مدنی')

    mother_language = models.CharField(max_length=50, null=True, verbose_name='زبان مادری')

    permanent_address = models.CharField(max_length=100, null=True, verbose_name='سکونت اصلی')
    current_address = models.CharField(max_length=100, null=True, verbose_name='سکونت فعلی')

    phone = models.CharField(max_length=50, null=True, verbose_name='شماره تماس')

    # Physical Information

    height = models.CharField(max_length=20, null=True, verbose_name='قد')
    eye_color = models.CharField(max_length=50, null=True, verbose_name='رنگ چشم')
    eyebrow = models.CharField(max_length=50, null=True, verbose_name='رنگ ابرو')
    face_color = models.CharField(max_length=50, null=True, verbose_name='رنگ چهره')
    hair_color = models.CharField(max_length=50, null=True, verbose_name='رنگ مو')

    special_marks = models.CharField(max_length=50, null=True, verbose_name='نشانه های دیگر')


    # Identification
    PASSPORT = "passport"
    SARSHOMARI = "sarshomari"
    AMAYESH = "amayesh"
    DAFTARCHE = "daftarche"

    ID_CHOICES = [
        (PASSPORT, "پاسپورت اقامتی"),
        (SARSHOMARI, "برگه سرشماری"),
        (AMAYESH, "کارت آمایش"),
        (DAFTARCHE, "دفترچه اقامت ویژه"),
    ]
    id_type = models.CharField(max_length=20, choices=ID_CHOICES, null=True, verbose_name='مدرک اقامتی')
    id_number = models.CharField(max_length=50, null=True, verbose_name='شماره مدرک')


    services = models.ManyToManyField(
    Service,
    blank=True,
    verbose_name="نوع خدمات"
    )


    # Relatives Info
    full_name_r = models.CharField(max_length=255, null=True, verbose_name='اسم و تخلص نماینده')
    father_name_r = models.CharField(max_length=100, null=True, verbose_name='اسم پدر نماینده')
    grandfather_name_r = models.CharField(max_length=100, null=True, verbose_name='اسم پدرکلان نماینده')
    tazkera_id = models.CharField(max_length=100, null=True, verbose_name='شماره تذکره')
    phone_r = models.CharField(max_length=50, null=True, verbose_name='شماره تماس')
    marriage_id = models.CharField(max_length=50, null=True, verbose_name='شماره نکاح خط رسمی')
    kindship = models.CharField(max_length=50, null=True, verbose_name='نوع قرابت')




    issue_date = models.DateField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت",
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ثبت",
        null=True
    )

    
    
    # to display list
    def __str__(self):
        return f"{self.full_name},"



  
    class Meta:
        verbose_name = 'فرم تذکره'
        verbose_name_plural = 'فرم تذکره ها'



