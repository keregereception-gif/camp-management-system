from django.db import models

# 1. Справочник компаний
class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    
    def __str__(self):
        return self.name

# 2. Блоки (например, блок A, блок B)
class Block(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название блока")

    def __str__(self):
        return self.name

# 3. Комнаты
class Room(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name="Блок")
    room_number = models.CharField(max_length=50, verbose_name="Номер комнаты")
    capacity = models.IntegerField(verbose_name="Количество мест")

    def __str__(self):
        return f"Блок {self.block.name} - Комната {self.room_number}"

# 4. Сотрудники
class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО сотрудника")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания")
    position = models.CharField(max_length=100, verbose_name="Должность", blank=True, null=True)

    def __str__(self):
        return self.full_name

# 5. Заселение (связывает сотрудника и комнату)
class Accommodation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Комната")
    check_in_date = models.DateField(verbose_name="Дата заезда")
    check_out_date = models.DateField(verbose_name="Дата выезда (план)", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Проживает в данный момент")

    def __str__(self):
        return f"{self.employee.full_name} -> {self.room}"
        


# Create your models here.
