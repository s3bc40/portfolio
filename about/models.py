from django.db import models
from django.utils import timezone


class Person(models.Model):
    """
    Define the person concerned by the portfolio.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(null=True, max_length=254, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    twitter = models.URLField(verbose_name='Twitter URL', null=True, blank=True)
    linkedin = models.URLField(verbose_name='Linkedin URL', null=True, blank=True)
    github = models.URLField(verbose_name='GitHub URL', null=True, blank=True)
    instagram = models.URLField(verbose_name='Instragram URL', null=True, blank=True)
    facebook = models.URLField(verbose_name='Facebook URL', null=True, blank=True)

    def get_person_age(self):
        """
        Allows to get the actual age of :model:`about:Person`.

        :return: The age of :model:`about:Person`.
        :rtype: int
        """
        now = timezone.now().date()
        return now.year - self.birth_date.year - ((now.month, now.day) < (self.birth_date.month, self.birth_date.day))

    def is_defined_social_network(self):
        """
        Allows to know if one of the social network link is defined for a :model:`about:Person`.
        :return: True if one of social network is defined
        """
        return True if self.twitter or self.linkedin or self.github or self.instagram or self.facebook else False
