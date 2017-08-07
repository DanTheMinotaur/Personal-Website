from django.db import models


class Project(models.Model):
    link_name = models.CharField(max_length=50)
    link_description = models.CharField(max_length=255, blank=True)
    link_url = models.URLField()
    link_image = models.ImageField(upload_to='site_images/homepage/')  # Check where this will save files to
    optional_class = models.CharField(max_length=40, blank=True)

    placement = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.link_name


class SkillGroup(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_description = models.CharField(max_length=250, blank=True)

    optional_icon = models.CharField(max_length=30, blank=True)
    optional_class = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.skill_name


class Skill(models.Model):
    # Icons in Technology Icons
    POSSIBLE_ICONS = (
        ('default', 'Customer Icon'),
        ('aftereffects', 'Aftereffects'),
        ('bridge', 'Bridge'),
        ('dreamweaver', 'Dreamweaver'),
        ('fireworks', 'Fireworks'),
        ('flash', 'Flash'),
        ('illustrator', 'Illustrator'),
        ('indesign', 'Indesign'),
        ('lightroom', 'Lightroom'),
        ('photoshop', 'Photoshop'),
        ('cockpit', 'Cockpit'),
        ('drupal', 'Drupal'),
        ('joomla', 'Joomla'),
        ('magento', 'Magento'),
        ('october', 'October'),
        ('wordpress', 'Wordpress'),
        ('visual-studio', 'Visual-Studio'),
        ('bootstrap', 'Bootstrap'),
        ('emmet', 'Emmet'),
        ('less', 'Less'),
        ('postcss', 'Postcss'),
        ('sass', 'Sass'),
        ('cassandra', 'Cassandra'),
        ('database', 'Database'),
        ('hadoop', 'Hadoop'),
        ('mariadb', 'Mariadb'),
        ('mongodb', 'Mongodb'),
        ('mysql-alt', 'Mysql-Alt'),
        ('mysql', 'Mysql'),
        ('postgres', 'Postgres'),
        ('sql', 'Sql'),
        ('sublime', 'Sublime'),
        ('express', 'Express'),
        ('grails', 'Grails'),
        ('grailsalt', 'Grailsalt'),
        ('laravel-alt', 'Laravel-Alt'),
        ('laravel', 'Laravel'),
        ('phonegap', 'Phonegap'),
        ('platter', 'Platter'),
        ('playframework', 'Playframework'),
        ('rails-alt', 'Rails-Alt'),
        ('rails', 'Rails'),
        ('jira-alt', 'Jira-Alt'),
        ('jira', 'Jira'),
        ('angular', 'Angular'),
        ('backbone', 'Backbone'),
        ('d3', 'D3'),
        ('ember', 'Ember'),
        ('jquery-alt', 'Jquery-Alt'),
        ('jquery', 'Jquery'),
        ('react', 'React'),
        ('c', 'C'),
        ('cplusplus', 'Cplusplus'),
        ('csharp', 'Csharp'),
        ('haskell', 'Haskell'),
        ('java', 'Java'),
        ('nodejs', 'Nodejs'),
        ('objectivec', 'Objectivec'),
        ('perl', 'Perl'),
        ('php-alt', 'Php-Alt'),
        ('php', 'Php'),
        ('python', 'Python'),
        ('ruby', 'Ruby'),
        ('scala', 'Scala'),
        ('debian', 'Debian'),
        ('fedora', 'Fedora'),
        ('freebsd', 'Freebsd'),
        ('gnome', 'Gnome'),
        ('java-duke', 'Java-Duke'),
        ('kde', 'Kde'),
        ('linux-mint', 'Linux-Mint'),
        ('netbsd', 'Netbsd'),
        ('rasbaerrypi', 'Rasbaerrypi'),
        ('redhat', 'Redhat'),
        ('solaris', 'Solaris'),
        ('suse', 'Suse'),
        ('ubuntu', 'Ubuntu'),
        ('autoit', 'Autoit'),
        ('browsersync', 'Browsersync'),
        ('confluence', 'Confluence'),
        ('dynamicweb', 'Dynamicweb'),
        ('babel', 'Babel'),
        ('webpack', 'Webpack'),
        ('osx', 'Osx'),
        ('codeignitor', 'Codeignitor'),
        ('composer', 'Composer'),
        ('zend', 'Zend'),
        ('apache', 'Apache'),
        ('jetty', 'Jetty'),
        ('memcached', 'Memcached'),
        ('nginx-alt', 'Nginx-Alt'),
        ('nginx', 'Nginx'),
        ('redis', 'Redis'),
        ('tomcat', 'Tomcat'),
        ('ec3', 'Ec3'),
        ('github-circle-alt', 'Github-Circle-Alt'),
        ('github-circle', 'Github-Circle'),
        ('github', 'Github'),
        ('google-code', 'Google-Code'),
        ('heroku', 'Heroku'),
        ('shell-alt', 'Shell-Alt'),
        ('shell', 'Shell'),
        ('shellscript', 'Shellscript'),
        ('opensource', 'Opensource'),
        ('bower', 'Bower'),
        ('grunt', 'Grunt'),
        ('gulp', 'Gulp'),
        ('selenium', 'Selenium'),
        ('git-squared', 'Git-Squared'),
        ('git', 'Git'),
        ('svn', 'Svn'),
        ('css-alt', 'Css-Alt'),
        ('css3-alt', 'Css3-Alt'),
        ('css3', 'Css3'),
        ('html5', 'Html5'),
        ('js', 'JavaScript'),
    )

    skill_title = models.CharField(max_length=50, blank=False)
    icon = models.CharField(max_length=20, choices=sorted(POSSIBLE_ICONS), blank=False, default='default')
    custom_icon = models.CharField(max_length=30, blank=True)
    skill_description = models.CharField(max_length=200, blank=True)
    optional_class = models.CharField(max_length=30, blank=True)

    placement = models.SmallIntegerField(default=1)

    skill_group = models.ForeignKey(SkillGroup, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.skill_title

