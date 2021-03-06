from ModelsLibraries import *




# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=45, blank=False)
    last_name = models.CharField(max_length=45, blank=False)
    message = models.TextField(blank=False,max_length=1000)
    email=models.EmailField(blank=False)
    cellphone=models.IntegerField(blank=False)
    service_type=models.CharField(max_length=2, choices=SERVICES, default='DA')

    def __str__(self):
        name = "{} {}".format(self.first_name, self.last_name)
        return name




#----------------------------------------------------------
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=45, blank=False)
    photo = models.ImageField(upload_to="uploads/profiles/", max_length=45, blank=False)
    role = models.CharField(max_length=45, blank=True)
    administrator = models.BooleanField(default=False)
    bio = models.TextField(max_length=550, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    slug = models.SlugField(max_length=50, unique=True, blank=False)
    linkedin = models.URLField(blank=False, default="https://linkedin/company/angoapp")
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Persons"

    # def get_slug(self):
    #     name = self.name.lower()
    #     name = name.replace(" ", "-")
    #     return name

    def __str__(self):
        return self.name




#----------------------------------------------------------




class Project(models.Model):
    title = models.CharField(max_length=30, blank=False)
    type = models.CharField(max_length=15, blank=False)
    manager = models.ForeignKey(Person)
    client = models.CharField(max_length=15, blank=False)
    description = models.TextField()
    link = models.CharField(max_length=300, blank=True)
    artwork = models.ImageField(upload_to='uploads/projects/', max_length=45, blank=True)
    featured = models.BooleanField(default=False)
    publishedDate = models.DateTimeField(auto_now=False)
    slug = models.SlugField(max_length=50, unique=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = 'Portfolio Projects'

    def __str__(self):
        return self.title

    def uri(self):
        return reverse('project', args=[str(self.slug)])

    def get_author(self):
        return self.manager.name




#----------------------------------------------------------




class Article(models.Model):
    author = models.ForeignKey(Person)
    title = models.CharField(max_length=45, blank=False)
    content = models.TextField(blank=False)
    summary = models.TextField(blank=True, max_length=100)
    publishedDate = models.DateField(default=date.today)
    updatedDate = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = 'Documentation & Blog'

    def writer(self):
        return self.author.name

    def get_author(self):
        return self.author.name

    def uri(self):
        return reverse('doc', args=[str(self.slug)])

    def __str__(self):
        return self.title




#----------------------------------------------------------

#----------------------------------------------------------




class Partner(models.Model):
    name = models.CharField(max_length=45)
    link = models.URLField(max_length=250)
    image = models.ImageField(upload_to='uploads/partners/', max_length=45)
    
    def __str__(self):
        return self.name




#----------------------------------------------------------


# Similar to Color, Photo can be featured alongside Project.
# Multiple instances of Photo can also be created in the admin panel.
class Photo(models.Model):
    projectName = models.ForeignKey(Project)
    photo = models.ImageField(upload_to='uploads/projects/', max_length=45)

    def projectTitle(self):
        return self.projectName.title
#end Photo

#----------------------------------------------------------






class Message(models.Model):
    sender  = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    origin = models.CharField(max_length=200)

    def summary(self):
        return "Message about '{}' from '{}'".format(self.subject, self.sender)

    def __str__(self):
        return self.subject