from django.db import models
from employees.models import Employee


class SensorEvent(models.Model):
    SENSOR_CHOICES = [
        ("RFID", "RFID"),
        ("FINGERPRINT", "Fingerprint"),
        ("FACE", "Face Recognition"),
        ("DOOR", "Door Sensor"),
        ("EXIT", "Exit Sensor"),
    ]

    EVENT_CHOICES = [
        ("CHECK_IN", "Check In"),
        ("CHECK_OUT", "Check Out"),
        ("ACCESS_GRANTED", "Access Granted"),
        ("ACCESS_DENIED", "Access Denied"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="sensor_events"
    )

    sensor_type = models.CharField(
        max_length=20,
        choices=SENSOR_CHOICES
    )

    event_type = models.CharField(
        max_length=20,
        choices=EVENT_CHOICES
    )

    device_id = models.CharField(
        max_length=50
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    processed = models.BooleanField(
        default=False
    )

    raw_data = models.JSONField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "Sensor Event"
        verbose_name_plural = "Sensor Events"

    def __str__(self):
        return f"{self.employee.employee_id} - {self.sensor_type}"