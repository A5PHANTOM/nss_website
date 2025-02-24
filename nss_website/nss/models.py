from django.db import models


# class Program(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     poster_image = models.ImageField(upload_to='program_images/', blank=True, null=True)
#     more_description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.title

# class ProgramPhoto(models.Model):
#     program = models.ForeignKey(Program, related_name='program_photos', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='program_photos/')


#     def __str__(self):
#         return f"Photo {self.id} for {self.program.title}"

# class MoreProgramPhoto(models.Model):
#     program = models.ForeignKey(Program, related_name='more_program_photos', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='more_program_photos/')



class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_image = models.ImageField(upload_to='program_images/', blank=True, null=True)
    more_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class ProgramPhoto(models.Model):
    program = models.ForeignKey(Program, related_name='program_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='program_photos/')

class MoreProgramPhoto(models.Model):
    program = models.ForeignKey(Program, related_name='more_program_photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='more_program_photos/')
