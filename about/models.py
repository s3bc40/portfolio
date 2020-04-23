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

    def __str__(self):
        return self.last_name + ' ' + self.first_name

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


class Skill(models.Model):
    """ Technical or personal/social skill acquired """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    fontawesome = models.CharField(max_length=30)
    frameworks = models.TextField(null=True, blank=True)
    libraries = models.TextField(null=True, blank=True)
    technical = models.BooleanField(verbose_name="Technical skill?")

    def __str__(self):
        return self.name


class Experience(models.Model):
    """ Define an abstract model in common of :model:`about:Experience` and :model:`about:Formation` """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    starting_date = models.DateField()
    ending_date = models.DateField(null=True, blank=True)
    resume = models.TextField()

    class Meta:
        abstract = True
        ordering = ['-starting_date']

    def __str__(self):
        return self.title

    def get_months_duration(self):
        """
        Allows to get the duration of work of :model:`about:Experience`.

        :return: The duration of :model:`about:Experience`.
        :rtype: basestring
        """
        if self.ending_date:
            months = (self.ending_date.year - self.starting_date.year) * 12 + \
                     self.ending_date.month - self.starting_date.month
            return months
        else:
            return 0


class Professional(Experience):
    """
    Define an experience linked to :model:`about:Person`.

    Subclass of :model:`about:Experience`
    """
    company = models.CharField(max_length=30)


class Formation(Experience):
    """
    Define a formation linked to :model:`about:Person`

    Subclass of :model:`about:Experience`
    """
    institute = models.CharField(max_length=30)
    level = models.IntegerField(verbose_name="Bachelor level")
