from django.db import models

# Create your models here.
class Victim_Info (models.Model):
#  كٌ اسمك وعمرك إيميلك أو رقم جوالك أو حسابك في شبكات التواصل
    
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254)
    #كيف ضايقك؟
#(اشرح لي نوع الإيذاء وهل شتمكم أو هددكم أو طلب مال أو أجبركم على فعل معين..)

    description = models.TextField()
   #في أي برنامج إلكتروني ضايقك؟
#(اسم اللعبة أو التطبيق أو شبكة التواصل الاجتماعي مع رابطها)

    program = models.TextField()
  #  ممكن تصورلنا الشاشة؟ - رفع مرفقات
#(أحتاج منك أي دليل ضده) 

    files = models.ImageField(null = True)
#مين مضايقك؟
#اسمه أو جواله أو ايميله أو اسم حسابه مع الرابط)

    blackmailer_name = models.CharField(max_length=200, null=True, blank=True)
    blackmailer_email = models.EmailField(max_length=254 , null=True, blank=True)
    blackmailer_account = models.CharField(max_length=200, null=True, blank=True)

    Request_Status = models.oneToMany(Victim_Request_Status)

  
    def __str__(self):
        return self.name

class Victim_Request_Status(models.Model):
    
    # تاريخ الشكوى
    create_date = models.DateField(auto_now=False, auto_now_add=True)
   # استيفاء بيانات الشكوى
    approved = models.BooleanField(null=True)
    #التواصل مع المعتدي
    contact_blackmailer = models.BooleanField()
    #انقضاء المهلة
    timeـout = models.BooleanField()
    # النتيجه النهائيه
    results = models.TextField()

    def __str__(self):
        return self.completed

#نصائح للتغلب على المعتدين

class Resources(models.Model):
        
    name = models.TextField()
    url = models.URLField(max_length=200)
    source = models.TextField()

    def __str__(self):
        return self.name