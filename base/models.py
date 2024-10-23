from django.db import models
from django.utils import timezone  # นำเข้า timezone

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)  # ชื่อเรื่อง
    body = models.TextField()  # เนื้อหาของโพสต์
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # รูปภาพที่อัปโหลด (อาจไม่ต้องใส่ก็ได้)
    timestamp = models.DateTimeField(default=timezone.now)  # เวลาที่โพสต์ถูกสร้าง (ใช้ default เป็นเวลาปัจจุบัน)

    def __str__(self):
        return self.title  # แสดงชื่อเรื่องใน admin
